from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from .models import *
from .forms import *

# Create your views here.

@ensure_csrf_cookie
@login_required(login_url='/login/')
def home(request):

    context = {
        'title':'Home',
    }
    return render(request, 'app/index.html', context)


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