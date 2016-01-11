import datetime

from django.core.urlresolvers import reverse
from django.utils import timezone
from django.test import TestCase

from madeit.models import Thread, Comment

# Create your tests here.
def create_thread(thread_title, thread_text, days, votes, user):
    """
    Creates a thread with the given `thread_title` and 'thread_text' 
    published the given number of `days` offset to now.
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Thread.objects.create(thread_title=thread_title,
                                    thread_text=thread_text,
                                    pub_date=time,
                                    votes=votes,
                                    user=user)
                                    
def create_comment(thread, comment_text, days, votes, user):
    """
    Creates a thread with the given a thread and 'comment_text' 
    published the given number of `days` offset to now.
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Comment.objects.create(thread=thread,
                                    comment_text=comment_text,
                                    pub_date=time,
                                    votes=votes,
                                    user=user)


class QuestionViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the
        index page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )