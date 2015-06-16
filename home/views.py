from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import viewsets
from rest_framework.response import Response
from .models import ContactRequest
from .serializers import ContactRequestSerializer
from rest_framework import status
from home.msgs import send_email, post_to_slack

@ensure_csrf_cookie
def index(request):
    return render_to_response('home/index.html',
                              context_instance=RequestContext(request))

class ContactRequestViewSet(viewsets.ModelViewSet):

    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer

    def create(self, *args, **kwargs):
        '''request.data should look like
        {'phone': 1234567, 'servicetype': 'automation', 
        'name': 'jeremy', 'email': 'j@j.com', 'message': 'please help me'}
        '''
        print(args[0].data)
        create_resp = super().create(*args, **kwargs)
        if (create_resp.status_code == status.HTTP_201_CREATED):
            send_email(args[0].data)
            post_to_slack(args[0].data)
        
        return create_resp



        
