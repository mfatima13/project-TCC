from django.urls import path, include

from rest_framework.routers import DefaultRouter

from project import views

router = DefaultRouter()
router.register('task', views.TaskViewSet)
router.register('task-create', views.TaskView)
router.register('todos', views.TodoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
