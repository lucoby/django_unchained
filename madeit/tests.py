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


class MadeitIndexViewTests(TestCase):
    def test_index_view_with_no_threads(self):
        """
        If no threads exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('madeit:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There doesn't appear to be any threads here.")
        self.assertQuerysetEqual(response.context['latest_thread_list'], [])

    def test_index_view_with_a_past_thread(self):
        """
        Threads with a pub_date in the past should be displayed on the
        index page.
        """
        create_thread(thread_title="Past thread", 
                        thread_text="Past thread.", 
                        days=-30, 
                        votes=0, 
                        user="guest")
        response = self.client.get(reverse('madeit:index'))
        self.assertQuerysetEqual(
            response.context['latest_thread_list'],
            ['<Thread: Past thread.>']
        )
        
class MadeitThreadViewTests(TestCase):
    def test_detail_view_with_no_comments(self):
        """
        The detail view of a question with a pub_date in the future should
        return a 404 not found.
        """
        thread = create_thread(thread_title="Past thread", 
                                thread_text="Past thread.", 
                                days=-30, 
                                votes=0, 
                                user="guest")
        response = self.client.get(reverse('madeit:thread',
                                   args=(thread.id,)))
        self.assertContains(response, thread.thread_text,
                            status_code=200)
        self.assertContains(response, "There doesn't appear to be any comments here.",
                            status_code=200)

    def test_detail_view_with_comments(self):
        """
        The detail view of a question with a pub_date in the past should
        display the question's text.
        """
        thread = create_thread(thread_title="Past thread", 
                                thread_text="Past thread.", 
                                days=-30, 
                                votes=0, 
                                user="guest")
        comment = create_comment(thread=thread, 
                                comment_text="Past comment.", 
                                days=-29, 
                                votes=0, 
                                user="guest")
        response = self.client.get(reverse('madeit:thread',
                                  args=(thread.id,)))
        self.assertContains(response, "Past comment.",
                            status_code=200)