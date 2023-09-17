from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .models import Question, Choice, Vote
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


class IndexView(generic.ListView):
    """Generic view for the index page."""
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """Generic view for the detail page."""
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
    
    def get(self, request, **kwargs):
        """Handle GET requests."""
        try:
            self.object = self.get_object()
        except Http404:
            # Handle the case where the object is not found
            messages.error(request, "Poll not found.")
            return redirect('polls:index')

        if not self.object.is_published():
            messages.error(request, "This question is not published yet.")
            return redirect('polls:index')

        if not self.object.can_vote():
            messages.error(request, "Voting for this poll is not allowed.")
            return redirect('polls:index')
        question = get_object_or_404(Question, pk=kwargs['pk'])
        user = request.user

        if user.is_authenticated:
            try:
                selected_choice = question.choice_set.get(vote__user=user)
            except Choice.DoesNotExist:
                selected_choice = None

            context = {
                'question': question,
                'selected_choice': selected_choice,
            }
            return render(request, 'polls/detail.html', context)
        else:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)


class ResultsView(generic.DetailView):
    """Generic view for the results page."""
    model = Question
    template_name = 'polls/results.html'


def index(request: HttpRequest) -> HttpResponse:
    """View for the index page."""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    """View for the detail page."""
    # question = get_object_or_404(Question, pk=question_id)
    # user = request.user

    # try:
    #     selected_choice = user.vote_set.get(choice__question=question)
    # except Choice.DoesNotExist:
    #     selected_choice = 'cat'

    # context = {
    #     'question': question,
    #     'selected_choice': selected_choice,
    # }
    # return render(request, 'polls/detail.html', context)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    """View for the results page."""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

@login_required
def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    """View for the voting page."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'message': 'You didn\'t select a choice.',
        })
    
    this_user = request.user
    
    try:
        # Try to find a vote by this user for this question
        vote = Vote.objects.get(user=this_user, choice__question=question)
        # Update the user's vote
        vote.choice = selected_choice
    except Vote.DoesNotExist:
        # If no matching vote, create a new one
        vote = Vote(user=this_user, choice=selected_choice)
    
    vote.save()
    messages.success(request, f"Your vote for {selected_choice.choice_text} has been saved.")
    # Redirect to the results page after voting
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
