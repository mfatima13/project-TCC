from django.urls import path, include

from rest_framework.routers import DefaultRouter

from team import views

router = DefaultRouter()
router.register('team', views.TeamViewSet)
router.register('members', views.MembersViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]