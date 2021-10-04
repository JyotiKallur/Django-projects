from django.shortcuts import render,HttpResponse
from home.models import Contact


# Create your views here.
def home(request):
    context = {'name':'Jyoti', 'course':'Django'}
    return render(request,'home.html',context)
    #return HttpResponse("Thi is my home page ")

#def about(request):
    #return HttpResponse("Thi is my about page ")

def projects(request):
    return render(request,'projects.html')
    #return HttpResponse("Thi is my project page")

def contact(request):
    if request.method =="POST":
        print("This is Post")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print("The data has been written to the db")

    return render(request,'contact.html')
    #return HttpResponse("Thi is my contact page")

