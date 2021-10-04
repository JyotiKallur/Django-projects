# Creating website
from django .http import HttpResponse
from django.shortcuts import render

#code for video:6

#def index(request):
    #return HttpResponse("Hello Jyoti Kallur")
   # return HttpResponse('''<h1>Hello Jyoti Kallur</h1><a href="https://www.bing.com/search?q=amazon.in&pc=COS2&ptag=D042321-N0640AF75BAE01A83A43AB87F&form=CONBDF&conlogo=CT3331983 "> Amazon prime</a>''')#using html code

#def about(request):
    #return HttpResponse("About Jyoti Kallur")

#code for video 7
def index(request):
    params = {'name':'Jyoti','place':'Mars'}
    return render(request,'index.html',params)
    #return HttpResponse("Home")

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("captalize first<a href ='/'>back</a>")
'''
def newlineremove(request):
    return HttpResponse("newline remove")

def spaceremove(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("char count")'''