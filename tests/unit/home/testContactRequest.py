from django.test import TestCase
from home.views import ContactRequestViewSet
from home.models import ContactRequest
from rest_framework.test import APITestCase
from rest_framework import status
from mock import Mock, patch
from django.core import mail
from home import msgs

class SendMsgsTest(TestCase):

    data = {'name':'jeremy',
        'email':'j@j.com',
        'phone': '1234567',
        'servicetype':'automation',
        'message':'please help me',
       } 

    def test_send_email(self):
        mail.outbox = []
        msgs.send_email(self.data,True)
        self.assertEqual(len(mail.outbox),1)
        mailmsg = mail.outbox[0]

        self.assertIn("New contact request from softworks.com",
                        mailmsg.subject)
        self.assertIn("From name: jeremy", mailmsg.body)
        

class ContactRequestTest(APITestCase):

    data = {'name':'jeremy',
        'email':'j@j.com',
        'phone': '1234567',
        'servicetype':'automation',
        'message':'please help me',
       } 

    def testContactRequestView(self):
        response = self.client.post("/api/v1/contact/", self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #enusre use is stored in db
        cr = ContactRequest.objects.get(email=self.data['email'])
        self.assertEqual(cr.phone, self.data['phone'])


    @patch('home.views.post_to_slack')
    @patch('home.views.send_email')
    def testContactRequestView_sendmsg(self, email_mock, slack_mock):
        cr = self.data.copy()
        cr['email']="test@test.com"
        response = self.client.post("/api/v1/contact/", cr, format='json')

        self.assertEqual(email_mock.call_count, 1)
        self.assertEqual(slack_mock.call_count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    @patch('home.views.post_to_slack')
    @patch('home.views.send_email')
    def testContactRequestView_only_sendsmsg_onsuccess(self, email_mock,
                                                       slack_mock):
        response = self.client.post("/api/v1/contact/", None, format='json')

        self.assertEqual(email_mock.call_count, 0)
        self.assertEqual(slack_mock.call_count, 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)







