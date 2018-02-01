from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from django import forms
from xml.dom import minidom
import xml.etree.ElementTree as ET
import csv
# Create your views here.
def index(request):
    tree = ET.parse("C:/Users/burhan/Desktop/clnical trials xml/NCT00001193.xml")
    root = tree.getroot()
    cit_head = []
    count = 0
    for ref in root.findall('keyword'):
        cit = []
        #if count==0:
        #    citation = ref.find('citation').tag
        #    cit_head.append(citation)
        #    pm_id = ref.find('PMID').tag
        #    cit_head.append(pm_id)
        #    count = count + 1
        citation = ref.text
        cit_head.append(citation)
        #pm_id = ref.find('PMID').text
        #cit_head.append(pm_id)
    print(cit_head)








    #xmldoc = minidom.parse('C:/Users/burhan/Desktop/clnical trials xml/NCT00001193.xml')
    #readbitlist = xmldoc.getElementsByTagName('readbit')
    #values = []
    #return HttpResponse(open('C:/Users/burhan/Desktop/clnical trials xml/NCT00001193.xml').read())
    return render(request, 'ClinicalTrialSearch/index.html')
    #return render(request,'blog/flightrate.html')
