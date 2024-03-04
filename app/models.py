from django.db import models
from django.utils.text import slugify

from account.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def is_correct_check(self, pk):
        return self.answer_set.filter(pk=pk, is_correct=True).exists()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Result(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    total_question = models.IntegerField(default=0)
    total_correct = models.IntegerField(default=0)
    score = models.FloatField(default=0)

    def __str__(self):
        return self.user.phone

    def save(self, *args, **kwargs):
        self.score = self.total_correct * 100 / self.total_question
        return super().save(*args, **kwargs)

    @property
    def is_passed(self):
        return self.score >= 60

    @property
    def is_failed(self):
        return self.score < 60
