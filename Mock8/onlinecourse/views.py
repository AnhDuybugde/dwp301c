"""Views for course exam submission and result display."""

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Choice, Course, Enrollment, Question, Submission


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

    enrollment, _created = Enrollment.objects.get_or_create(
        user=request.user,
        course=course,
    )
    selected_choices = Choice.objects.filter(id__in=selected_choice_ids)
    submission = Submission.objects.create(
        enrollment=enrollment,
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
    enrollment = get_object_or_404(
        Enrollment,
        user=request.user,
        course=course,
    )
    submission = get_object_or_404(
        Submission,
        pk=submission_id,
        enrollment=enrollment,
    )

    selected_ids = list(submission.choices.values_list("id", flat=True))
    questions = Question.objects.filter(course=course)
    selected_question_map = {
        choice.id: choice.question_id
        for choice in submission.choices.select_related("question")
    }
    total_score = 0
    possible_score = 0

    for question in questions:
        selected_for_question = [
            choice_id
            for choice_id in selected_ids
            if selected_question_map.get(choice_id) == question.id
        ]
        total_score += question.is_get_score(selected_for_question)
        possible_score += question.grade

    passed = total_score >= max(1, possible_score // 2)
    context = {
        "course": course,
        "selected_ids": selected_ids,
        "grade": total_score,
        "possible": possible_score,
        "passed": passed,
    }

    return render(request, "onlinecourse/exam_result_bootstrap.html", context)
