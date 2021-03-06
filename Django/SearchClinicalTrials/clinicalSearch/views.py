from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import Context, loader
import xml.etree.ElementTree as ET
import datetime
import glob
from . models import ClinicalStudy,Condition,Outcome,Mesh,Location,Intervention
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os

class Index(View):

    def post(self,request):
        pass
    
    def get(self, request):
        template = loader.get_template('clinicalSearch/index.html')
        os.chdir("C:/Users/burhan/Desktop/clinical tials/SearchClinicalTrials/clinicalSearch/media");
        files =  [file for file in glob.glob('*.xml')]
        for file in files:
            print("Processing File: " , file)
            tree = ET.parse(file)
            root = tree.getroot()
            # open a file for writing

            resident_head = []

            count = 0
            cites_list = []
            pmid_list = []

            # for elt in tree.iter():
            #    print("%s: '%s'" % (elt.tag, elt.text))


            #create model instance
            clinicalSearchModel=ClinicalStudy()


            #insert org_id
            for data in root.findall('id_info'):
                try:
                    clinicalSearchModel.org_study_id=data.find('org_study_id').text
                except Exception:
                        print('No tag')
                try:
                    clinicalSearchModel.nct_id = data.find('nct_id').text
                except Exception:
                        print('No tag')

            #insert official title,source
            try:
                official_title = root.find('official_title').text
                clinicalSearchModel.official_title=official_title
            except Exception:
                    print('No tag')
            try:
                clinicalSearchModel.source = root.find('source').text
            except Exception:
                    print('No tag')
            try:
                clinicalSearchModel.overall_status = root.find('overall_status').text
            except Exception:
                    print('No tag')
            try:
                clinicalSearchModel.start_date = root.find('start_date').text
            except Exception:
                    print('No tag')
            try:
                clinicalSearchModel.completion_date = root.find('completion_date').text
            except Exception:
                    print('No tag')
            try:
                clinicalSearchModel.study_type = root.find('study_type').text
            except Exception:
                    print('No tag')
            try:
                clinicalSearchModel.no_of_arms = root.find('number_of_arms').text
            except Exception:
                print('No tag')
            # clinicalSearchModel.start_date = datetime.datetime.strptime(root.find('start_date').text, "%B %Y").date()
            # clinicalSearchModel.completion_date = datetime.datetime.strptime(root.find('completion_date').text, "%B %Y").date()
            try:
                clinicalSearchModel.no_of_enrollment = root.find('enrollment').text
            except Exception:
                    print('No tag')
            try:
                clinicalSearchModel.result_first_posted_date = root.find('results_first_posted').text
            except Exception:
                    print('No tag')
            try:
                clinicalSearchModel.last_updated_date = root.find('last_update_posted').text
            except Exception:
                    print('No tag')
            try:
                clinicalSearchModel.verification_date = root.find('verification_date').text
            except Exception:
                    print('No tag')


            #eligibility
            for data in root.findall('eligibility'):
                try:
                    clinicalSearchModel.eligibility_sampling_method = data.find('sampling_method').text
                except Exception:
                        print('No tag')
                try:
                    clinicalSearchModel.eligibility_gender = data.find('gender').text
                except Exception:
                        print('No tag')
                try:
                    clinicalSearchModel.eligibility_min_age = data.find('minimum_age').text
                except Exception:
                        print('No tag')
                try:
                    clinicalSearchModel.eligibility_max_age = data.find('maximum_age').text
                except Exception:
                        print('No tag')
                for x in data.findall('study_pop'):
                    try:
                        clinicalSearchModel.eligibility_study_pop = x.find('textblock').text
                    except Exception:
                            print('No tag')
                for x in data.findall('criteria'):
                    try:
                        clinicalSearchModel.eligibility_criteria = x.find('textblock').text
                    except Exception:
                            print('No tag')

            for data in root.findall('overall_official'):
                try:
                    clinicalSearchModel.overall_official_name = data.find('last_name').text
                except Exception:
                        print('No tag')
                try:
                    clinicalSearchModel.overall_official_role = data.find('role').text
                except Exception:
                        print('No tag')
                try:
                    clinicalSearchModel.overall_official_affiliation = data.find('affiliation').text
                except Exception:
                        print('No tag')


            # insert sponsor
            for data in root.findall('sponsors'):
                for x in data.findall('lead_sponsor'):
                    try:
                        clinicalSearchModel.lead_sponsor_agency = x.find('agency').text
                    except Exception:
                            print('No tag')
                    try:
                        clinicalSearchModel.lead_sponsor_agency_class=x.find('agency_class').text
                    except Exception:
                            print('No tag')


            # insert brief textblock
            for data in root.findall('brief_summary'):
                try:
                    textblock = data.find('textblock').text
                    clinicalSearchModel.brief_summary = textblock
                except Exception:
                        print('No tag')

            # insert description textblock
            for data in root.findall('detailed_description'):
                try:
                    clinicalSearchModel.detail_description = data.find('textblock').text
                except Exception:
                        print('No tag')
            clinicalSearchModel.save()
            #b=Outcome(clinicalStudyId_id=clinicalSearchModel.pk)
            for data in root.findall('secondary_outcome'):
                b=Outcome(clinicalStudyId_id=clinicalSearchModel.pk)

                #c.outcome_set.create(outcome_type="secondary_outcome", measure=data.find('measure').text, timeFrame=data.find('time_frame').text, description=data.find('description').text)
                try:
                    b.outcome_type = "secondary_outcome"
                except Exception:
                    print("No tag")
                try:
                    b.measure = data.find('measure').text
                except Exception:
                    print("No tag")
                try:
                    b.timeFrame=data.find('time_frame').text
                except Exception:
                    print("No tag")
                try:
                    b.description=data.find('description').text
                except Exception:
                    print("No tag")
                b.save()

            #insert primary outcomes and secondary outcome
            c = get_object_or_404(ClinicalStudy, pk=clinicalSearchModel.pk)
            #b = get_object_or_404(ClinicalStudy, pk=clinicalSearchModel.pk)

            for data in root.findall('intervention_browse'):
                b=Mesh(clinicalStudyId_id=clinicalSearchModel.pk)
                try:
                    b.mesh_name=data.find('mesh_term').text
                except Exception:
                        print('No tag')
                b.save()
            for data in root.findall('condition_browse'):
                #c.mesh_set.create(mesh_name=data.find('mesh_term').text)
                b=Mesh(clinicalStudyId_id=clinicalSearchModel.pk)
                try:
                    b.mesh_name=data.find('mesh_term').text
                except Exception:
                        print('No tag')
                b.save()
            for data in root.findall('primary_outcome'):
                b=Outcome(clinicalStudyId_id=clinicalSearchModel.pk)

                #c.outcome_set.create(outcome_type="secondary_outcome", measure=data.find('measure').text, timeFrame=data.find('time_frame').text, description=data.find('description').text)
                try:
                    b.outcome_type = "primary_outcome"
                except Exception:
                    print("No tag")
                try:
                    b.measure = data.find('measure').text
                except Exception:
                    print("No tag")
                try:
                    b.timeFrame=data.find('time_frame').text
                except Exception:
                    print("No tag")
                try:
                    b.description=data.find('description').text
                except Exception:
                    print("No tag")
                b.save()

            # insert primary outcomes and secondary outcome
            for data in root.findall('condition'):
                b=Condition(clinicalStudyId_id=clinicalSearchModel.pk)

                try:
                    b.condition_name=data.text
                except Exception:
                        print('No tag')
                b.save()
            for data in root.findall('intervention'):
                b=Intervention(clinicalStudyId_id=clinicalSearchModel.pk)
                try:
                    b.intervention_name=data.find("intervention_name").text
                except Exception:
                        print('No tag')
                try:
                    b.intervention_type=data.find("intervention_type").text
                except Exception:
                        print('No tag')
                try:
                    b.intervention_description=data.find("description").text
                except Exception:
                        print('No tag')
                b.save()

                #c.intervention_set.create(intervention_name=data.find("intervention_name").text , intervention_type=data.find("intervention_type").text , intervention_description=data.find("description").text)
            for data in root.findall('location'):
                for x in data.findall('facility'):
                    b=Location(clinicalStudyId_id=clinicalSearchModel.pk)
                    try:
                        b.location_name = x.find('name').text
                    except Exception:
                            print('No tag')

                    for y in x.findall('address'):
                        try:
                            b.location_city = y.find('city').text
                        except Exception:
                            print('No tag')
                        try:
                            b.location_state = y.find('state').text
                        except Exception:
                            print('No tag')
                        try:
                            b.location_zip = y.find('zip').text
                        except Exception:
                            print('No tag')
                        try:
                            b.location_country = y.find('country').text
                        except Exception:
                            print('No tag')
                #b.location_name=name_facility
                #b.location_city=city
                #b.location_state=state
                #b.location_zip=zip_code
                #b.location_country=country
                b.save()






        context = {}
        return HttpResponse(template.render(context, request))
class Result(View):
    def post(self, request):
        pass

    def get(self, request):
        template = loader.get_template('clinicalSearch/result.html')
        #print(match_email.nct_id)
        #heading = ClinicalStudy.objects.get(nct_id)

        context = {}
        return HttpResponse(template.render(context, request))


class Detail(View):
    def post(self, request):
        pass
    def get(self, request, rec_id):
        template = loader.get_template('clinicalSearch/detail.html')
        print(rec_id, "========================")
        det = ClinicalStudy.objects.get(nct_id=rec_id)
        #idd = list([data.id for data in det])
        #print(det.id)
        mesh_data = Mesh.objects.filter(clinicalStudyId_id=det.id)
        location_data = Location.objects.filter(clinicalStudyId_id=det.id)
        intervention_data = Intervention.objects.filter(clinicalStudyId_id=det.id)
        #outcome_data = Outcome.objects.get(clinicalStudyId_id=det.id)
        #condition_data = Condition.objects.get(clinicalStudyId_id=det.id)



        context = {'det': det, 'mesh_data': mesh_data,'location_data':location_data,'intervention_data':intervention_data}
        return HttpResponse(template.render(context, request))


class SearchNct(View):
    def post(self, request):
        template = loader.get_template('clinicalSearch/result.html')

        nctid = request.POST["nct-id"]
        rec = ClinicalStudy.objects.filter(nct_id=nctid)

        context = {"rec":rec}
        return HttpResponse(template.render(context, request))


    def get(self, request):
        pass


class SearchLoc(View):
    def post(self, request):
        template = loader.get_template('clinicalSearch/result.html')
        mesh = request.POST["name"]
        rec = ClinicalStudy.objects.raw("SELECT 1 as id, c.* from clinicalsearch_clinicalstudy c, clinicalsearch_mesh m where c.id =m.clinicalStudyId_id and m.mesh_name=\'" + mesh+"\'")
        #print(rec.nct_id)
        context = {"rec":rec}
        if rec:
            #context = {"match_email":match_email}
            print("true")
        else:
            print("false")
        return HttpResponse(template.render(context, request))
    def get(self, request):
        pass



class SearchCon(ListView):

    # def dispatch(self,request,*args,**kwargs):
    #     # model = ClinicalStudy
    #     # template_name = "clinicalSearch/result.html"
    #     # paginate_by = 10
    #     # rec2 = ClinicalStudy()
    #     me = request.POST["name"]
    #     #print(mesh,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    #     return super(SearchCon, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        pass
        #template = loader.get_template('clinicalSearch/result.html')
        #
        # if request.POST:
        #     #print(me,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.")
        #     mesh = request.POST["name"]
        #     rec = ClinicalStudy.objects.raw("SELECT 1 as id, c.* from clinicalsearch_clinicalstudy c, clinicalsearch_mesh m where c.id =m.clinicalStudyId_id and m.mesh_name=\'" + mesh+"\'")
        # page = request.POST.get('page', 1)
        # paginator = Paginator(list(rec), 10)
        # #context = {"rec":rec}
        # try:
        #     users = paginator.page(page)
        # except PageNotAnInteger:
        #     users = paginator.page(1)
        # except EmptyPage:
        #     users = paginator.page(paginator.num_pages)
        #     print(users)
        #
        # print(users,"==================")
        # if rec:
        #     #context = {"match_email":match_email}
        #     print("true")
        # else:
        #     print("false")
        # context = {"users":users}
        # #return HttpResponse(context,request)
        # return render(request, 'clinicalSearch/result.html', { 'users': users })



    def get(self, request):
        #template = loader.get_template('clinicalSearch/result.html')




       if 'mesh' in request.session:
           mesh=request.session['mesh']
       else:
           mesh = request.GET["name"]
           request.session['mesh'] = request.GET["name"]

       page = request.GET.get('page', 1)
       rec = ClinicalStudy.objects.raw("SELECT 1 as id, c.* from clinicalsearch_clinicalstudy c, clinicalsearch_mesh m where c.id =m.clinicalStudyId_id and m.mesh_name=\'" + mesh+"\'")
        #rec = ClinicalStudy.objects.all()
       page = request.GET.get('page', 1)
       paginator = Paginator(list(rec), 10)
        #context = {"rec":rec}
       try:
            users = paginator.page(page)
       except PageNotAnInteger:
            users = paginator.page(1)
       except EmptyPage:
            users = paginator.page(paginator.num_pages)
            print(users)

       print(users,"==================")
       if rec:
            #context = {"match_email":match_email}
            print("true")
       else:
            print("false")
       context = {"users":users}
        #return HttpResponse(context,request)
       return render(request, 'clinicalSearch/result.html', { 'users': users })

#match_email = ClinicalStudy.objects.filter(nct_id=nctid)
#match = Mesh.objects.filter(mesh_name=mesh)

#mesh = ClinicalStudy.objects.filter(pk=match_email.id)
#match_email = ClinicalStudy.objects.all()
#print(match_email.nct_id)
#match = Mesh.objects.filter(id=match_email["clinicalStudyId_id"] )
#print(match_email["clinicalStudyId_id"])
# surreal_publishers = list([book.clinicalStudyId_id for book in match])
# print(surreal_publishers)
# match_email = ClinicalStudy.objects.filter(id=surreal_publishers[0] )
# surreal = list([book.official_title for book in match_email])
# print(surreal)
#for rec in ClinicalStudy.objects.raw("SELECT 1 as id, c.official_title,c.source,c.nct_id from clinicalsearch_clinicalstudy c, clinicalsearch_mesh m where c.id =m.clinicalStudyId_id and m.mesh_name='Melphalan'"):
    # print (rec.nct_id)
#print(rec.nct_id)
