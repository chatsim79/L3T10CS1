from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice
from django.shortcuts import render

# Create your views here

class IndexView(generic.ListView):
    template_name = 'polls/poll.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    """ 
    This function defines the exception process
    for voting in a poll. The question model is called 
    and rendered. If no question exists, a 404 is dispalyed
    an exception is generated if no choice is selected
    before using the vote button, whereby a messgae will be
    displayed and the user will be allowed to select.
    when a valid selection is made, 1 count is added to the vote 
    tally and the user is redirected to the results page.

    :param Question: Stored question in db
    :param question id: id of Question

    :rtype: results screen if vote success
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
    )
    except (KeyError, Choice.DoesNotExist):
    # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id,))
    )