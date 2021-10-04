from django.contrib import admin
from django.urls import path ,include
from home import views
#import home1

# Django admin header customization
admin.site.site_header =" Login to Developer JSD"
admin.site.site_title = "Welcome to JSD Website"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    path('', views.home, name='home'),
   # path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact')

]
