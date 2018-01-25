from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Heading, Body, User
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages

def index(request):
    latest_heading_list = Heading.objects.order_by('-pub_date')[:10]
    template = loader.get_template('blog/index.html')
    st = request.POST
    #print(st['bd'])
    #print(st['hd'])
    #sb = request.POST['bd']
    if request.POST:
      q = Heading(heading_text=st.get('hd'), pub_date=timezone.now(), body_text = st.get('bd'))

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

        match = User.objects.filter(email=email)
        if match:

            #messages.info(request, 'Your password already exists!')
            return HttpResponse("Email already exists")
            #return render('ajx.html', message='Save complete')
        else:
            User.objects.create(
            email = email,
            password = password
            )

            return HttpResponse("new user created")

     #except User.DoesNotExist:
            # Unable to find a user, this is fine
         #return email
    #    if User.objects.search(email):
    #        print('true')
        #raise Exception('This email address is already in use.')



    return render(request,'blog/ajx.html')

# Create your views here.
