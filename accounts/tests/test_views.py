from django.test import TestCase
from unittest.mock import patch
from accounts.models import Token
import accounts


class SendLoginEmailViewTest(TestCase):

    def send_login_mail_POST(self):
        return self.client.post('/accounts/send_login_email', data={
           'email':'p.leonard.example@gmail.com'
        })

    def test_creates_toek_associated_with_email(self):
        response = self.send_login_mail_POST()
        token = Token.objects.first()
        self.assertEqual(token.email, 'p.leonard.example@gmail.com')

    @patch('accounts.views.send_mail')
    def test_sends_link_to_login_using_token_uid(self,mock_send_mail):
        self.send_login_mail_POST()

        token = Token.objects.first()
        expected_url = 'http://testserver/accounts/login?token={uuid}'.format(
            uuid=token.uid
        )
        (subject, body, from_email, to_list), kwargs = mock_send_mail.call_args
        self.assertIn(expected_url, body)

    def test_redirects_to_home_page(self):
        response = self.send_login_mail_POST()
        self.assertRedirects(response,'/')

    @patch('accounts.views.send_mail')
    def test_sends_mail_to_address_from_post(self,mock_send_mail):
        self.send_login_mail_POST()

        self.assertEqual(mock_send_mail.called, True)
        (subject, body, from_email, to_list), kwargs = mock_send_mail.call_args
        self.assertEqual(subject,'Your login link for Superlists')
        self.assertEqual(from_email,'p.leonard.example@gmail.com')
        self.assertEqual(to_list,['p.leonard.example@gmail.com'])

    def test_add_success_message(self):
        response = self.client.post('/accounts/send_login_email', data={
           'email':'p.leonard.example@gmail.com'
        }, follow=True)

        message = list(response.context['messages'])[0]
        self.assertEqual(
            message.message,
            "Check your email, we've sent you a link you can use to log in."
        )
        self.assertEqual(message.tags, "success")
                                    
class LoginViewTest(TestCase):

        def test_redirects_to_home_page(self):
            response = self.client.get('/accounts/login?token=abcd123')
            self.assertRedirects(response,'/')