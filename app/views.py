from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from .models import *
from .forms import *


@ensure_csrf_cookie
@login_required(login_url='/login/')
def home(request):
    context = {
        'title':'Home',
    }
    return render(request, 'app/index.html', context)


def semesters(request):
    if request.is_ajax():
        semesters = Semester.objects.all().order_by("name")
        response = []
        for semester in semesters:
            semester_json = {}
            semester_json['name'] = semester.name
            semester_json['start_date'] = semester.start_date.strftime('%d.%m.%Y')
            semester_json['end_date'] = semester.end_date.strftime('%d.%m.%Y')
            semester_json['active'] = semester.active
            response.append(semester_json)

        return HttpResponse(
            json.dumps(response),
            content_type="application/json"
        )

    else:
        raise Http404()


def create_semester(request):
    if request.is_ajax():
        if request.method == 'POST':
            form = SemesterForm(data=request.POST)
            response = {}
            if form.is_valid():
                active_sem = Semester.objects.get(active=True)
                active_sem.active = False
                active_sem.save()

                sem = Semester()
                sem.name = "{0}{1}".format(form.cleaned_data['academic_year'], form.cleaned_data['sem_type'])
                sem.sem_type = form.cleaned_data['sem_type']
                sem.start_date = form.cleaned_data['start_date']
                sem.end_date = form.cleaned_data['end_date']
                sem.save()

                response['result'] = 'Utworzono nowy semestr!'
                response['error'] = False
            else:
                response['result'] = 'Nie udało się utworzyć semestru! Wprowadzono błędne dane'
                response['error'] = True

            return HttpResponse(
                json.dumps(response),
                content_type="application/json"
            )

    else:
        raise Http404()


def students(request):
    if request.is_ajax():
        students = Student.objects.all().order_by("surname")
        response = []
        for student in students:
            student_json = {}
            student_json['id'] = student.id
            student_json['name'] = student.name
            student_json['surname'] = student.surname
            response.append(student_json)

        return HttpResponse(
            json.dumps(response),
            content_type="application/json"
        )

    else:
        raise Http404()


def create_student(request):
    if request.is_ajax():
        if request.method == 'POST':
            form = StudentForm(data=request.POST)
            response = {}
            if form.is_valid():
                form.save()
                response['result'] = 'Pomyślnie dodano studenta!'
                response['error'] = False
            else:
                response['result'] = 'Błędne dane!'
                response['error'] = True

            return HttpResponse(
                json.dumps(response),
                content_type="application/json"
            )
        # else:
        #     form= StudentForm()
        #
        #     response = HttpResponse()
        #     response.write("<form action=\"/ajax/students/create/\" method=\"post\" id=\"id_students_form\">")
        #     response.write("<div id=\"result_box\"></div>")
        #
        #     for field in form:
        #         response.write("<div class=\"ui-field-contain\">")
        #         response.write("{0}{1}".format(field.label_tag(), field))
        #         response.write("</div>")
        #
        #     response.write("<input type=\"submit\" value=\"Dodaj\">")
        #     response.write("</form>")
        #
        #     return response

    else:
        raise Http404()


def student_details(request):
    if request.is_ajax():
        student = Student.objects.get(pk = request.GET['id'])
        response = {}
        response['name'] = student.name
        response['surname'] = student.surname

        return HttpResponse(
            json.dumps(response),
            content_type="application/json"
        )

    else:
        raise Http404()
