"""Views for course exam submission and result display."""

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Choice, Course, Submission


@login_required
def submit(request, course_id):
    """Handle exam submission and save selected choices."""
    course = get_object_or_404(Course, pk=course_id)

    if request.method != "POST":
        return redirect("onlinecourse:course_details", course_id=course.id)

    selected_choice_ids = []
    for key, values in request.POST.lists():
        if key.startswith("choice_"):
            selected_choice_ids.extend(values)

    selected_choices = Choice.objects.filter(id__in=selected_choice_ids)
    submission = Submission.objects.create(
        user=request.user,
        course=course,
    )
    submission.choices.set(selected_choices)
    submission.save()

    return redirect(
        "onlinecourse:show_exam_result",
        course_id=course.id,
        submission_id=submission.id,
    )


@login_required
def show_exam_result(request, course_id, submission_id):
    """Display exam score, result message, and selected answers."""
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(
        Submission,
        pk=submission_id,
        course=course,
        user=request.user,
    )

    selected_choices = submission.choices.all()
    total_grade = 0
    correct_choices = []

    for choice in selected_choices:
        if choice.is_correct:
            total_grade += choice.question.grade
            correct_choices.append(choice)

    passed = total_grade >= 1
    context = {
        "course": course,
        "submission": submission,
        "selected_choices": selected_choices,
        "correct_choices": correct_choices,
        "grade": total_grade,
        "passed": passed,
    }

    return render(request, "onlinecourse/exam_result_bootstrap.html", context)
