from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from mytutor import views
from django.views.generic.base import RedirectView
urlpatterns = [ 
    path('home/', views.HomeView.as_view()),
    path('tutor/', views.TutorListView.as_view()),
    path('contact/', views.ContactView.as_view()),
    path('tutor/<int:pk>', views.TutorDetailView.as_view()),    

    path('question/', views.QuestionListView.as_view()),
    path('question/<int:pk>', views.QuestionDetailView.as_view()),        
    path('question/create/', views.QuestionCreate.as_view(success_url="/mytutor/question")),
   
    path('contact/submit', views.contact),
    path('', RedirectView.as_view(url="home/")),    
]
