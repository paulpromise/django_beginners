from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SignupPageTest(TestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testuser@email.com",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )

        self.assertEqual(response.status_code, 302)

        self.assertEqual(get_user_model().objects.count(), 1)

        user = get_user_model().objects.first()

        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@email.com")