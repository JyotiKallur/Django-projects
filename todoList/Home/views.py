from typing import ContextManager
from django.shortcuts import render, HttpResponse
from Home.models import Task

# Create your views here.
def Home(request):
    context = {'success':False, 'name':'Jyoti'}
    if request.method =="POST":
        #Handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success':True}
    
    return render(request, 'index.html',context)
    

def tasks(request):
    allTasks = Task.objects.all()
    #print(allTasks)
    #for item in allTasks:
        #print(item.taskTitle)
    context ={'tasks':allTasks}
    return render(request, 'tasks.html', context)
