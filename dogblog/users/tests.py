from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from dogblog.users.forms import CreateUserForm, ProfilUserForm
from dogblog.users.views import CreateUserView, ProfileUserView, DeleteUserView


class TestStatusAndHtml(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.get(username='User_test')

    def test_status_code(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse("create_users"))
        self.assertEqual(response.status_code, 200)


class TestCreateUser(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()
        self.new_user = {"first_name": "User3", "last_name": "User3_last",
                         "username": "User3_test", "password1": "Password3",
                         "password2": "Password3"}

    def test_create_user(self):

        response = self.client.get(reverse('create_users'))
        self.assertEquals(reverse('create_users'), '/users/create/')
        self.assertIsInstance(response.context['form'], CreateUserForm)
        self.assertIs(response.resolver_match.func.view_class,
                      CreateUserView)
