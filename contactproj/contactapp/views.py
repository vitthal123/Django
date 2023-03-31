from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactData
from .forms import ContactForm

# Create your views here.

def Contact_View(request):
    if request.method=='POST':
        cform=ContactForm(request.POST)
        if cform.is_valid():
            name1=request.POST.get('name')
            mobile1=request.POST.get('mobile')
            email1=request.POST.get('email')
            location1=request.POST.get('location')
            course1=request.POST.get('course')

            data=ContactData(name=name1,mobile=mobile1,email=email1,location=location1,course=course1)
            data.save()
            cform=ContactForm()
            return render(request,'contact.html',{'abcd':cform})
        else:
            return HttpResponse("Form is Invalid")
    else:
        cform=ContactForm()
        return render(request,'contact.html',{'abcd':cform})
