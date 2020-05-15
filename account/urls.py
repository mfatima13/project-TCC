from django.urls import path, include

from rest_framework.routers import DefaultRouter

from account import views

router = DefaultRouter()
router.register('users', views.UserlistCreate)
router.register('update', views.UserUpdateDelete)

urlpatterns = [
    path('', include(router.urls)),
]