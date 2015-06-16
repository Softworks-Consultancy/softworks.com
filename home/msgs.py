from django.core.mail import mail_admins, send_mail
import threading
from django.conf import settings

class EmailThread(threading.Thread):
    def __init__(self, subject, message):
        self.subject = subject
        self.message = message 
        threading.Thread.__init__(self)

    def run(self):
        #mail_admins(self.subject, self.message)
        send_mail(self.subject, self.message, settings.EMAIL_HOST_USER,
                  ["jeremy@softworks.com.my",])

def send_email(data, no_thread=False):
    '''
    send an email... by default on seperate thread
    setting no_thread = true, will send email on same thread
    i.e. normal operations... it's good for testing
    '''

    subject = "New contact request from softworks.com"
    message = '''
    A new request just came in.  Here are the details.
    From name: %s
    Email address: %s
    Phone: %s
    Interested in Service Type: %s
    Message: %s
    ''' % (data['name'], data['email'], data['phone'], 
           data['servicetype'], data['message'])
    if no_thread:
        send_mail(subject, message, settings.EMAIL_HOST_USER,
                  ["jeremy@softworks.com.my",])
    else:
        EmailThread(subject, message).start()

def post_to_slack(data):
    pass
