from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    # /polls/questions/
    path("questions/", views.QuestionListView.as_view(), name="question_list"),
    # /polls/question/#/
    path(
        "question/<int:pk>/", views.QuestionDetailView.as_view(), name="question_detail"
    ),
    # /polls/question/#/results/
    path(
        "question/<int:pk>/results/",
        views.QuestionResultsView.as_view(),
        name="question_results",
    ),
    # /polls/question/#/vote/
    path("question/<int:question_id>/vote/", views.vote, name="question_vote"),
    # /polls/
    path("", views.CategoryListView.as_view(), name="category_list"),
    # /polls/category/#/
    path(
        "category/<int:pk>/", views.CategoryDetailView.as_view(), name="category_detail"
    ),
]
