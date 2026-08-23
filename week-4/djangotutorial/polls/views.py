from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Category, Choice, Question


class QuestionListView(generic.ListView):
    template_name = "polls/question_list.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = "polls/question_detail.html"


class QuestionResultsView(generic.DetailView):
    model = Question
    template_name = "polls/question_results.html"


class CategoryListView(generic.ListView):
    model = Category
    template_name = "polls/category_list.html"
    context_object_name = "category_list"


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = "polls/category_detail.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/question_detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse("polls:question_results", args=(question.id,))
        )
