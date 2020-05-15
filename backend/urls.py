from django.contrib import admin
from django.urls import path, include

# Create a router and register our viewsets with it.
#router = DefaultRouter()

urlpatterns = [
    path('accounts-api/', include('account.urls')),
    path('team-api/', include('team.urls')),
    #path('project-api/', include('project.urls')),
    path('admin/', admin.site.urls),
]

admin.site.site_header = 'GP Devs'
admin.site.index_title = 'Administração'
admin.site.site_title = 'Bem Vindo ao GP'
