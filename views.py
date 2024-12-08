from django.shortcuts import render

from PhysioApp.forms import AppointmentForm


# Create your views here.
def index(request):
    return render(request,'index.html')
def feature(request):
    return render(request,'feature.html')
def blog(request):
    return render(request,'blog.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def testimonial(request):
    return render(request,'testimonial.html')
def services(request):
    return render(request, 'services.html')
def team(request):
    return render(request,'team.html')
def appointment(request):
    return render(request,'appointment.html')







