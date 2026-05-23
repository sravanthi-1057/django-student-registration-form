from django.shortcuts import render

# Create your views here.
from .forms import StudentForm
from .models import Student

def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            Student.objects.create(
                fullname=form.cleaned_data['fullname'],
                email=form.cleaned_data['email'],
                mobile=form.cleaned_data['mobile'],
                dob=form.cleaned_data['dob'],
                gender=form.cleaned_data['gender'],
                department=form.cleaned_data['department'],
                year=form.cleaned_data['year'],
                rollno=form.cleaned_data['rollno'],
                address=form.cleaned_data['address'],
                state=form.cleaned_data['state'],
                pincode=form.cleaned_data['pincode'],
                skills=",".join(form.cleaned_data['skills']),
                mode=form.cleaned_data['mode'],
                resume=form.cleaned_data['resume'],
                about=form.cleaned_data['about'],
            )
            return render(request, 'studentapp/success.html')
    else:
        form = StudentForm()
    return render(request, 'studentapp/register.html', {'form': form})