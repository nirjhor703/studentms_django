from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student-list'),
    path('add/', views.student_add, name='student-add'),

    # AJAX fetch
    path('get-students/', views.get_students, name='get-students'),

    # CRUD actions
    path('save-students/', views.save_students, name='save-students'),
    path('update-students/', views.update_students, name='update-students'),

    # Edit page
    path('student-edit/<int:id>/', views.student_edit, name='student-edit'),

    # Delete action
    path('delete-students/', views.delete_students, name='delete-students'),
]