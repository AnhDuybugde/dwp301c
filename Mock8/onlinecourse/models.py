"""Models for the OnlineCourse exam application."""

from django.conf import settings
from django.db import models


class Course(models.Model):
    """Course model used by lessons and enrollment."""

    name = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateField(null=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """Lesson model related to one course."""

    title = models.CharField(max_length=200)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Instructor(models.Model):
    """Instructor profile for the OnlineCourse application."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)


class Learner(models.Model):
    """Learner profile for the OnlineCourse application."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=200)
    social_link = models.URLField(max_length=200)

    def __str__(self):
        return str(self.user)


class Question(models.Model):
    """Exam question model."""

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    question_text = models.CharField(max_length=1000)
    grade = models.IntegerField(default=1)

    def __str__(self):
        return self.question_text

    def is_get_score(self, selected_ids):
        """Return this question's grade when all selected answers are correct."""
        all_answers = self.choice_set.all()
        correct_ids = set(
            all_answers.filter(is_correct=True).values_list("id", flat=True)
        )
        selected_ids = set(int(choice_id) for choice_id in selected_ids)
        return self.grade if correct_ids == selected_ids else 0


class Choice(models.Model):
    """Answer choice model for a question."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class Submission(models.Model):
    """Submission model storing selected choices for a learner."""

    enrollment = models.ForeignKey(
        "Enrollment",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    choices = models.ManyToManyField(Choice)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission for {self.enrollment}"


class Enrollment(models.Model):
    """Simple enrollment model for connecting users and courses."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} enrolled in {self.course}"
