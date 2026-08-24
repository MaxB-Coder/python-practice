from rest_framework import serializers

from .models import Category, Choice, Question


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["id", "question", "choice_text", "votes"]
        read_only_fields = ["votes"]


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "question_text", "pub_date", "category", "choices"]
        read_only_fields = ["choices"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "questions"]
        read_only_fields = ["questions"]
