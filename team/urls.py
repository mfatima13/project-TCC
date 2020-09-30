from django.urls import path, include

from rest_framework.routers import DefaultRouter

from team import views

router = DefaultRouter()
router.register('team-lc', views.TeamListCreate)
router.register('team-du', views.TeamDeleteUpdate)
router.register('members-lc', views.MembersLC)
router.register('members-du', views.MembersDeleteUpdate)

urlpatterns = [
    path('', include(router.urls)),
    
]