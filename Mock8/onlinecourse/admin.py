"""Admin configuration for the OnlineCourse application."""

from django.contrib import admin
from .models import (
    Choice,
    Course,
    Enrollment,
    Instructor,
    Learner,
    Lesson,
    Question,
    Submission,
)


class QuestionInline(admin.StackedInline):
    """Display questions inline with lessons."""

    model = Question
    extra = 1


class ChoiceInline(admin.StackedInline):
    """Display answer choices inline with questions."""

    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """Admin page for questions and their choices."""

    fieldsets = [
        (None, {"fields": ["course", "lesson", "question_text", "grade"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "course", "lesson", "grade"]
    search_fields = ["question_text"]


class LessonAdmin(admin.ModelAdmin):
    """Admin page for lessons and their questions."""

    fieldsets = [
        (None, {"fields": ["course", "title", "content"]}),
    ]
    inlines = [QuestionInline]
    list_display = ["title", "course"]
    search_fields = ["title", "content"]


admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Enrollment)
admin.site.register(Instructor)
admin.site.register(Learner)
