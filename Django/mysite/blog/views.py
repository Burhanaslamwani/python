from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Heading, Body, User
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from django import forms

class ImageUploadForm(forms.Form):

    image = forms.ImageField()

def index(request):
    latest_heading_list = Heading.objects.order_by('-pub_date')[:2]
    template = loader.get_template('blog/index.html')
    st = request.POST
    #print(st['bd'])
    #print(st['hd'])
    #sb = request.POST['bd']
    if request.POST:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            oldstr = form.cleaned_data['image']
            print(oldstr,"dddddddddddddddddddddddddddddddddddddd")
            #newstr = oldstr.replace("blog/static/", "")
            q = Heading(heading_text=st.get('hd'), pub_date=timezone.now(), body_text = st.get('bd'), model_pic = form.cleaned_data['image'])
            q.save()
      #print(q.id,"dddddddddddddddddddddddddddddddddddddd...............")
      #p = Body()

    #  q.body_set.create(body_text=st.get('bd'))
      #q.save()
    #q.save()
     #p = Body(body_text=st.get('bd'))
     #print(p.id,"fffffffffffffffffffffffffffffffff")
    #p.save()
        #st = request.POST['hd']
    #else:
        #print("<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    #print(st)
    context = {
        'latest_heading_list': latest_heading_list,
    }
    return HttpResponse(template.render(context, request))

def flight(request):
    return render(request,'blog/flight.html')

def flightrate(request):
    return render(request,'blog/flightrate.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        q = User(email=email, password=password)
        q.save()
    return render(request,'blog/index2.html')

def news(request):
    latest_heading_list = Heading.objects.order_by('-pub_date')[:10]
    template = loader.get_template('blog/news.html')
    st = request.POST


    context = {
        'latest_heading_list': latest_heading_list,
    }
    return HttpResponse(template.render(context, request))
def detail(request, heading_id):
    #try:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        heading = Heading.objects.get(pk=heading_id)

        #body = Body.objects.get(pk=heading_id)
    #xcept Heading.DoesNotExist:
        #raise Http404("Question does not exist")
        return render(request, 'blog/detail.html', {'heading': heading})
def ajx(request):

    if request.method == "POST":

            #email = request.POST['email']
            #password = request.POST['password']

        print("fffffffffffffffffffffffffffffffffffffffffffffffffffff")
        email2 = request.POST['email1']
        password2 = request.POST['password1']
        match_email = User.objects.filter(email=email2)
        match_password = User.objects.filter(password=password2)
        if match_email and match_password:
            return HttpResponse("logged in")
        else:
            return HttpResponse("DoesNotExist")

        #try:



     #except User.DoesNotExist:
            # Unable to find a user, this is fine
         #return email
    #    if User.objects.search(email):
    #        print('true')
        #raise Exception('This email address is already in use.')



    return render(request,'blog/ajx.html')

# Create your views here.
