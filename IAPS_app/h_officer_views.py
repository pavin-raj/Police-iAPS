from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from IAPS_app.models import add_prisonerr,add_health_details


class IndexView(TemplateView):
    template_name = 'health_officer/h_officer_index.html'

class Prisoner_View(TemplateView):
    template_name = 'health_officer/view_prisoner.html'

    def get_context_data(self, **kwargs):
        context = super(Prisoner_View,self).get_context_data(**kwargs)

        view_prisoner = add_prisonerr.objects.filter(status=1)

        context['view_prisoner'] = view_prisoner
        return context

class Add_Health_Details(TemplateView):
    template_name = 'health_officer/add_health_details.html'

    def post(self , request,*args,**kwargs):

        id = request.GET['id']

        print(id)
        prisoner = add_prisonerr.objects.get(pk=id)
        prisoner.status='0'
        prisoner.save()
        height = request.POST['height']
        blood_group = request.POST['blood_group']
        allergies = request.POST['allergies']
        deseases = request.POST['deseases']
        weight = request.POST['weight']
        bp = request.POST['bp']
        medication = request.POST['medication']
        reading_date = request.POST['reading_date']
        user = User.objects.get(id=self.request.user.id)

        health = add_health_details()

        health.prisoner_id=id
        health.height = height
        health.blood_group=blood_group
        health.allergies =allergies
        health.deseases = deseases
        health.weight = weight
        health.bp = bp
        health.medication = medication
        health.reading_date = reading_date
        health.status = 'added'
        health.user = user
        health.save()



        return render(request, 'health_officer/add_health_details.html', {'messages': "successfully added"})




class View_Health(TemplateView):
    template_name = 'health_officer/view_health.html'

    def get_context_data(self, **kwargs):
        context = super(View_Health,self).get_context_data(**kwargs)

        view_health = add_prisonerr.objects.filter(status=0)

        context['view_health'] = view_health
        return context

class View_Update_Health(TemplateView):
    template_name = 'health_officer/view_update_health.html'

    def get_context_data(self, **kwargs):
        id= self.request.GET['id']
        print(id)
        context = super(View_Update_Health,self).get_context_data(**kwargs)


        view_health_details = add_health_details.objects.filter(prisoner_id=id)
        print(view_health_details)
        context['view_health_details'] = view_health_details
        return context
    def post(self,request,*args,**kwargs):
        id=request.POST['id']
        print(id)
        Weight=request.POST['weight']
        Bp=request.POST['bp']
        Medication=request.POST['medication']
        Readingdate=request.POST['reading_date']
        view_health_details = add_health_details.objects.get(prisoner_id=id)
        view_health_details.weight=Weight
        view_health_details.bp=Bp
        view_health_details.medication=Medication
        view_health_details.reading_date=Readingdate
        view_health_details.save()
        return redirect(request.META['HTTP_REFERER'])









