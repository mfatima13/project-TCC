from django.urls import path, include

from rest_framework.routers import DefaultRouter

from users import views

router = DefaultRouter()
router.register('users', views.UserVeiwSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
