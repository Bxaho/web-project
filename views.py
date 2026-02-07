from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student
from django.contrib.auth.decorators import login_required

def index(request):
    students = Student.objects.all()
    edit_student = None
    open_modal = False

    # Check if editing
    edit_id = request.GET.get("edit")
    if edit_id:
        edit_student = get_object_or_404(Student, id=edit_id)
        open_modal = True  # flag to open edit modal after reload

    if request.method == "POST":
        # Add student
        if 'add_student' in request.POST:
            if not request.user.is_authenticated:
                return redirect(f'/accounts/login/?next=/')

            name = request.POST.get("name")
            rollno = request.POST.get("rollno")
            email = request.POST.get("email")
            contact = request.POST.get("contact")
            faculty = request.POST.get("faculty")

            if name and rollno and faculty:
                Student.objects.create(
                    name=name, rollno=rollno, email=email, contact=contact, faculty=faculty
                )
                messages.success(request, "Student added successfully!")
            else:
                messages.error(request, "Name, Roll No, and Faculty are required.")
            return redirect('/')

        # Edit student
        elif 'edit_student' in request.POST:
            if not request.user.is_authenticated:
                student_id = request.POST.get("student_id")
                return redirect(f'/accounts/login/?next=/?edit={student_id}')

            student_id = request.POST.get("student_id")
            if not student_id:
                messages.error(request, "Invalid student ID.")
                return redirect('/')

            student = get_object_or_404(Student, id=student_id)
            student.name = request.POST.get("name")
            student.rollno = request.POST.get("rollno")
            student.email = request.POST.get("email")
            student.contact = request.POST.get("contact")
            student.faculty = request.POST.get("faculty")
            student.save()
            messages.success(request, "Student updated successfully!")
            return redirect('/')

    return render(request, 'index.html', {
        'students': students,
        'edit_student': edit_student,
        'open_modal': open_modal
    })


@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully!")
    return redirect('/')
