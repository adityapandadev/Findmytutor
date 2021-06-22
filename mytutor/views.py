from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from mytutor.models import Tutor, Question
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http.response import HttpResponseRedirect
from django.db.models import Q
from django.core.mail import send_mail

# Create your views here.
def contact(req):
    sub = "Tutor :: %s " % req.POST.get("uname")
    body = "Phone No = %s\nEMail = %s\nMessage = %s " % (req.POST.get("phone_no"), req.POST.get("email"),  req.POST.get("msg"))
    send_mail(
        sub,
        body,
        req.POST.get("email"),
        ['adityapanda0021@gmail.com'],
        fail_silently=False,
    )
    return HttpResponseRedirect("/mytutor/home?msg=Submited Successfully")



class HomeView(TemplateView):
    template_name = "mytutor/home.html"
    
class TutorListView(ListView):
    model = Tutor
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return Tutor.objects.filter(Q(name__icontains = si)| Q(subject__icontains = si)| Q(adress__icontains = si)).order_by("-id")
             


class TutorDetailView(DetailView):
    model = Tutor

class QuestionCreate(CreateView):
    model = Question
    fields = ["question"]
    def form_valid(self, form):
        self.object = form.save()
        self.object.asked_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class QuestionListView(ListView):
    model = Question

class QuestionDetailView(DetailView):
    model = Question
    
class ContactView(TemplateView):
    template_name = "mytutor/contact.html"

