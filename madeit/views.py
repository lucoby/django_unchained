from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from madeit.models import Comment, Thread


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'madeit/index.html'
    context_object_name = 'latest_Thread_list'

    def get_queryset(self):
        """Return the last five published Threads."""
        return Thread.objects.order_by('-pub_date')[:10]


class ThreadView(generic.DetailView):
    model = Thread
    template_name = 'madeit/thread.html'

# def thread_vote(request, Thread_id):
#     p = get_object_or_404(Thread, pk=Thread_id)
#     try:
#         selected_Comment = p.Comment_set.get(pk=request.POST['Comment'])
#     except (KeyError, Comment.DoesNotExist):
#         # Redisplay the Thread voting form.
#         return render(request, 'madeit/thread.html', {
#             'Thread': p,
#             'error_message': "You didn't select a Comment.",
#         })
#     else:
#         selected_Comment.votes += 1
#         selected_Comment.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('madeit:results', args=(p.id,)))
        