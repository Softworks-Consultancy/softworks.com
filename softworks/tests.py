from django.test import TestCase
from .views import Partial, PrivatePartial
from django.test.client import RequestFactory
from django.contrib.auth.models import User


# reverse('mrcesar.views.Partial', kwargs={'template_name': 'deadlines/'})
class PartialViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_partial_resolves_correctly(self):
        request = self.factory.get('/partials/intro/')
        # additional params can go after request
        response = Partial.as_view()(request, template_name='intro/')
        self.assertEqual(response.status_code, 200)

    def test_partial_response_content(self):
        request = self.factory.get('/partials/home/')
        # additional params can go after request
        response = Partial.as_view()(request, template_name='intro/')
        with self.assertTemplateUsed("mrcesar/partials/intro.html"):
            response.render()


class PrivatePartialViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="test", password="test")
        self.assertTrue(self.client.login(username="test", password="test"))

    def tearDown(self):
        self.user.delete()

    def test_private_partial_resolves_correctly(self):


        request = self.factory.get('/private_parts', kwargs={'template_name' :
                                                             'home'})
        request.user = self.user
        response = PrivatePartial.as_view()(request, template_name='home/')
        self.assertEqual(response.status_code, 200)

    def test_private_partial_response_content(self):
        request = self.factory.get('/private_parts/home/')
        # No session when using request factory
        request.user = self.user
        # additional params can go after request
        response = PrivatePartial.as_view()(request, template_name='home/')
        with self.assertTemplateUsed("mrcesar/private_partials/home.html"):
            response.render()
