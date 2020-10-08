from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Courses

# Create your views here.

def index (request):
    Courses_item = Courses.objects
    context = {'Courses_item': Courses_item}
    return render (request, 'courses/index.html', context)

def detail(request,Course_id):
    course_detail = get_object_or_404(Courses,pk = Course_id)

    return render(request,'courses/detail.html',{'course_detail': course_detail})
