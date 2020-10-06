from django.urls import path, include

from rest_framework.routers import DefaultRouter, SimpleRouter

from project import views

router = SimpleRouter()
router.register('task', views.TaskViewSet)
router.register('task-create', views.TaskView)
router.register('todos', views.TodoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
