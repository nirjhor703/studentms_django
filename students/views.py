from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.utils import timezone
from students.models import Student
from teachers.models import Teacher
from subjects.models import Subject
from classes.models import ClassModel


# Utility: Convert SQL rows → dict
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


# -------------------------
# LIST PAGE
# -------------------------
def student_list(request):
    cursor = connection.cursor()

    sql = """
        SELECT 
            id,
            name,
            email,
            phone,
            address,
            status,
            created_at,
            updated_at
        FROM students
        ORDER BY id ASC
    """

    cursor.execute(sql)
    students = dictfetchall(cursor)

    return render(request, "students/student_list.html", {
        "students": students
    })


# -------------------------
# RENDER ADD PAGE
# -------------------------
def student_add(request):
    return render(request, "students/add.html")


# -------------------------
# RENDER EDIT PAGE
# -------------------------
def student_edit(request, id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE id=%s", [id])
    student = dictfetchall(cursor)[0]

    return render(request, "students/edit.html", {
        "student": student
    })


# -------------------------
# AJAX: GET STUDENTS (like subjects)
# -------------------------
@csrf_exempt
def get_students(request):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT
            id,
            name,
            email,
            phone,
            address,
            status,
            created_at,
            updated_at
        FROM students
        ORDER BY id ASC
    """)
    students = dictfetchall(cursor)

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({"students": students})


# -------------------------
# SAVE NEW STUDENT
# -------------------------
@csrf_exempt
def save_students(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        status = request.POST.get("status")

        created_at = timezone.now()
        updated_at = timezone.now()

        try:
            cursor = connection.cursor()
            sql = """
                INSERT INTO students
                    (name, email, phone, address, status, created_at, updated_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            params = [name, email, phone, address, status, created_at, updated_at]
            cursor.execute(sql, params)

            return JsonResponse({"status": "success", "message": "Student saved successfully!"})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "failed", "message": "Invalid request"})


# -------------------------
# UPDATE STUDENT
# -------------------------
@csrf_exempt
def update_students(request):
    if request.method == "POST":
        sid = request.POST.get("student_id")

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        status = request.POST.get("status")

        updated_at = timezone.now()

        try:
            cursor = connection.cursor()
            sql = """
                UPDATE students
                SET 
                    name = %s,
                    email = %s,
                    phone = %s,
                    address = %s,
                    status = %s,
                    updated_at = %s
                WHERE id = %s
            """
            params = [name, email, phone, address, status, updated_at, sid]
            cursor.execute(sql, params)

            return JsonResponse({"status": "success", "message": "Student updated successfully!"})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "failed", "message": "Invalid request"})


# -------------------------
# DELETE STUDENT
# -------------------------
@csrf_exempt
def delete_students(request):
    if request.method == "POST":
        sid = request.POST.get("student_id")

        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM students WHERE id=%s", [sid])

            return JsonResponse({"status": "success", "message": "Student deleted successfully!"})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "failed", "message": "Invalid request"})

def home(request):
    context = {
        'student_count': Student.objects.count(),
        'teacher_count': Teacher.objects.count(),
        'subject_count': Subject.objects.count(),
        'class_count': ClassModel.objects.count(),
    }
    return render(request, 'home.html', context)
