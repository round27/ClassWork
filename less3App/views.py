from django.shortcuts import render
from .models import Student
# Create your views here.
def index(request):
    students = Student.objects.all()
    context = {'title': 'Welcome', 'students': students}
    return render(request, 'index.html', context)
