from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from students.models import Student
from teachers.models import Teacher
from subjects.models import Subject
from classes.models import ClassModel

def student_list(request):
    students = Student.objects.all().order_by('id')
    return render(request, 'students/student_list.html', {'students': students})

@csrf_exempt
def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        status = request.POST.get('status', 'Active')

        if not name or not email:
            return JsonResponse({'status': 'error', 'message': 'Name and Email are required!'})

        Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            status=status
        )
        return JsonResponse({'status': 'success', 'message': 'Student added successfully!'})

@csrf_exempt
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone', '')
        student.address = request.POST.get('address', '')
        student.status = request.POST.get('status', 'Active')
        student.save()
        return JsonResponse({'status': 'success', 'message': 'Student updated successfully!'})

@csrf_exempt
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return JsonResponse({'status': 'success', 'message': 'Student deleted successfully!'})



from django.shortcuts import render

def home(request):
    context = {
        'student_count': Student.objects.count(),
        'teacher_count': Teacher.objects.count(),
        'subject_count': Subject.objects.count(),
        'class_count': ClassModel.objects.count(),
    }
    return render(request, 'home.html', context)