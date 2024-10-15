from django.shortcuts import render
from .models import Course, Skill
# Create your views here.
def abaut(request):
    courses= Course.objects.all()
    skills = Skill.objects.all()
    return render(request, 'abaut/abaut.html', {'courses': courses, 'skills': skills })

