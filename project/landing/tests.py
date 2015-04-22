from django.test import TestCase
from landing.models import Emails


class Emails(TestCase):

    def test_not_correct_email(self):

        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)
