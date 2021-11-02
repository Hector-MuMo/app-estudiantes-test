"""escuela URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings
from estudiantes.views import ShowStudents, DetailStudent, CreateStudent, ShowClasses, DetailClass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estudiantes/', ShowStudents.as_view()),
    path('estudiantes/<pk>', DetailStudent.as_view()),
    path('estudiantes/nuevoEstudiante/', CreateStudent.as_view()),
    path('clases/', ShowClasses.as_view()),
    path('clases/<pk>', DetailClass.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()