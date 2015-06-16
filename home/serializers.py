from .models import ContactRequest
from rest_framework import serializers


class ContactRequestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ContactRequest 
        fields = ('name', 'email', 'phone', 'servicetype', 'message')

