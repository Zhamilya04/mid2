from django.shortcuts import render, redirect
from courses.forms import CourseRegistrationForm
from courses.models import Course
from .models import FavoriteCourse

def register_course(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.students.add(request.user)
            course.save()
            return redirect('home')
    else:
        form = CourseRegistrationForm()
    return render(request, 'register_course.html', {'form': form})


def add_favorite_course(request, course_id):
course = Course.objects.get(id=course_id)
favorite_course = FavoriteCourse(user=request.user, course=course)
favorite_course.save()
return redirect('course_detail', course_id=course_id)