from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Category, Choice, Question


class CategoryApiTests(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="tester", password="pw")
        self.category = Category.objects.create(name="Sport")

    def test_anonymous_can_list_categories(self) -> None:
        response = self.client.get(reverse("category-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_anonymous_post_rejected(self) -> None:
        response = self.client.post(
            reverse("category-list"), data={"name": "New"}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_post_accepted(self) -> None:
        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            reverse("category-list"), data={"name": "Science"}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Category.objects.filter(name="Science").exists())

    def test_category_detail_should_return_expected_fields(self) -> None:
        response = self.client.get(reverse("category-detail", args=[self.category.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(set(response.data.keys()), {"id", "name", "questions"})
        self.assertEqual(response.data["name"], "Sport")

    def test_validation_failure_should_return_expected_fields(self) -> None:
        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            reverse("category-list"), data={"name": "Sport"}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)
        self.assertEqual(Category.objects.filter(name="Sport").count(), 1)


class ChoiceApiTests(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username="tester", password="pw")
        category = Category.objects.create(name="Sport")
        question = Question.objects.create(
            question_text="Fastest?", pub_date=timezone.now(), category=category
        )
        self.choice = Choice.objects.create(question=question, choice_text="Yes")

    def test_votes_not_writeable(self) -> None:
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(
            reverse("choice-detail", args=[self.choice.id]),
            data={"votes": 999},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.choice.refresh_from_db()
        self.assertEqual(self.choice.votes, 0)
