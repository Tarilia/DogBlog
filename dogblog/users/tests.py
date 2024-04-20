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


class TestProfileUser(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.user = get_user_model().objects.get(username='User1_test')
        self.new_user = {'username': 'User_new_test',
                         'first_name': 'User_new',
                         'last_name': 'User_new_last'}
        self.url = reverse('profile')

    def test_profile_user(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.url, '/users/profile/')
        self.assertIsInstance(response.context['form'], ProfilUserForm)

        self.client.force_login(self.user)
        response = self.client.post(self.url, self.new_user)

        self.assertEquals(self.url, '/users/profile/')
        self.assertRedirects(response, reverse('profile'), 302)
        self.assertEqual(response['Location'], '/users/profile/')
        self.assertIs(response.resolver_match.func.view_class,
                      ProfileUserView)


class TestDeleteUser(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()

    def test_delete_users(self):
        del_user = \
            get_user_model().objects.get(username='User2_test')
        response = self.client.get(reverse('delete_users',
                                           kwargs={'pk': del_user.pk}))

        self.assertEqual(response.status_code, 302)
        self.assertIs(response.resolver_match.func.view_class,
                      DeleteUserView)
        self.assertEqual(response['Location'], '/users/login/')

        self.client.force_login(del_user)
        response = self.client.post(reverse('delete_users',
                                            kwargs={'pk': del_user.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertIs(response.resolver_match.func.view_class,
                      DeleteUserView)
        self.assertEqual(response['Location'], '/')
        self.assertFalse(get_user_model().objects.filter
                         (username='User2_test').exists())
