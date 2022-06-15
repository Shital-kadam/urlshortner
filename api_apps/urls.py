from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import  DefaultRouter
from api_apps.views import StudentViewSet as StudentView
from api_apps.views import TeacherViewSet as TeacherView



router= DefaultRouter()
router.register(r'student',StudentView)
router.register(r'Teacher',TeacherView)

urlpatterns = [
    path('',include(router.urls)),

    # path('',signUp),
    ]
