from django.urls import path, include

from rest_framework.routers import DefaultRouter

from team import views

router = DefaultRouter()
router.register('list', views.TeamListCreate)
router.register('update-delete', views.TeamDeleteUpdate)

urlpatterns = [
    path('', include(router.urls)),
]