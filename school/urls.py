from django.urls import path
from . import views

urlpatterns = [
    path('api/lead/', views.LeadListCreate.as_view()),
    path('api/lead/<int:pk>/', views.LeadDetails.as_view()),

    path('api/officestaff/', views.OfficestaffListCreate.as_view()),
    path('api/officestaff/<int:pk>/', views.OfficestaffdDetails.as_view()),

    path('api/teacher/', views.TeachersListCreate.as_view()),
    path('api/teacher/<int:pk>/', views.TeachersDetails.as_view()),

    path('api/student/', views.StudentsListCreate.as_view()),
    path('api/student/<int:pk>/', views.StudentDetails.as_view()),

    path('api/parent/', views.ParentsListCreate.as_view()),
    path('api/parent/<int:pk>/', views.ParentDetails.as_view()),
]
