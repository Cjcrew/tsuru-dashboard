from django.forms import EmailField
from django.forms.widgets import PasswordInput
from django.test import TestCase
from django.test.client import RequestFactory

from auth.views import login
from auth.forms import LoginForm

class LoginViewTest(TestCase):
    def test_login_expected_template_view(self):
        request = RequestFactory().get('/')
        response = login(request)
        self.assertEqual('auth/login.html', response.template_name)

class LoginFormTest(TestCase):
	def test_login_should_have_username_and_password_fields(self):
		self.assertIn('username', LoginForm.base_fields)
		self.assertIn('password', LoginForm.base_fields)

	def test_widget_for_password_field_should_be_password(self):
		field = LoginForm.base_fields['password']
		self.assertIsInstance(field.widget, PasswordInput)

	def test_username_should_have_at_most_60_characters(self):
		field = LoginForm.base_fields['username']
		self.assertEqual(60, field.max_length)

	def test_password_should_have_at_least_6_characters(self):
		field = LoginForm.base_fields['password']
		self.assertEqual(6, field.min_length)

	def test_username_field_should_accept_only_email_values(self):
		field = LoginForm.base_fields['username']
		self.assertIsInstance(field, EmailField)