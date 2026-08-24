from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register("categories", views.CategoryViewSet)
router.register("choices", views.ChoiceViewSet)
router.register("questions", views.QuestionViewSet)

urlpatterns = [path("", include(router.urls))]
