"""PracaMgr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import django.contrib.auth.views
from app import views, forms

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),

    url(r'^semesters/$', views.semesters, name='semesters'),
    url(r'^semesters/properties/$', views.semester_properties, name='semester_properties'),
    url(r'^semesters/create/$', views.create_semester, name='create_semester'),

    url(r'^students/$', views.students, name='students'),
    url(r'^students/details/$', views.student_details, name='student_details'),
    url(r'^students/create/$', views.create_student, name='create_student'),

    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login/login.html',
            'authentication_form': forms.CustomAuthenticationForm,
            'extra_context':
            {
                'title': 'Logowanie',
            }
        },
        name='login'),
    url(r'^logout/$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/home/',
        },
        name='logout'),

    url(r'^admin/', admin.site.urls),
]
