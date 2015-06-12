from django.test import TestCase
from django.core.urlresolvers import resolve
from django.test.client import RequestFactory
import json

from .views import index 
from .models import User


class IndexViewTest(TestCase):

    def test_root_url_resolves_to_index_view(self):
        r = resolve('/')
        self.assertEquals(r.func, index)

    def test_index_html_content(self):
        request_factory = RequestFactory()
        request = request_factory.get('/')
        request.session = {}
        with self.assertTemplateUsed("home/index.html"):
            index(request)


class LoginViewTest(TestCase):

    def setUp(self):
        self.test_user = User.objects.create_user(
            email="j@j.com", username='testuser', password='password')
        self.test_user.save()

    # redirection handled by AngularJS,  how to test?
    def test_success_login_redirects_user(self):
        pass


class RegisterViewTest(TestCase):
    pass


class LogoutViewTest(TestCase):
    pass


class UserModelTest(TestCase):

    def setUp(self):
        self.test_user = User.objects.create(
            email="j@j.com", username='testuser', password='password')
        self.test_user.save()


class StudentModelTest(TestCase):
    pass


class CounsellorViewTest(TestCase):
    pass
