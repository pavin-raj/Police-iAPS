from django.views.generic import TemplateView
from IAPS_app.models import warden_reg,medical_reg,add_complaints, add_prisonerr,parole_request,add_health_details
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.base import View



class IndexView(TemplateView):
    template_name = 'admin/admin_index.html'

class Jailer_Approvel(TemplateView):
    template_name = 'admin/jailer_approvel.html'

    def get_context_data(self, **kwargs):
        context = super(Jailer_Approvel,self).get_context_data(**kwargs)

        warden = warden_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['warden'] = warden
        return context

class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})

class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})

class Jailer_View(TemplateView):
    template_name = 'admin/jailer_view.html'
    def get_context_data(self, **kwargs):
        context = super(Jailer_View,self).get_context_data(**kwargs)

        app_warden = warden_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['app_warden'] = app_warden
        return context
class Medical_Approve(TemplateView):
    template_name = 'admin/medical_approve.html'

    def get_context_data(self, **kwargs):
        context = super(Medical_Approve,self).get_context_data(**kwargs)

        medical = medical_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['medical'] = medical
        return context

class Medical_View(TemplateView):
    template_name = 'admin/medical_view.html'

    def get_context_data(self, **kwargs):
        context = super(Medical_View,self).get_context_data(**kwargs)

        app_medical = medical_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['app_medical'] = app_medical
        return context

class Complaint_View(TemplateView):
    template_name = 'admin/view_complaints.html'

    def get_context_data(self, **kwargs):
        context = super(Complaint_View,self).get_context_data(**kwargs)

        view_com = add_complaints.objects.filter(status='added')

        context['view_com'] = view_com
        return context


    def post(self , request,*args,**kwargs):
        # complaint = actions.objects.get(user_id=self.request.id)
        id = request.POST['id']
        action = request.POST['action']
        act = add_complaints.objects.get(id=id)
        # act.complaint=complaint
        act.action= action




        act.status = 'replied'
        act.save()


        return redirect(request.META['HTTP_REFERER'])

# class Action(TemplateView):
#     template_name = 'admin/action.html'
#     def post(self , request,*args,**kwargs):
#         # complaint = actions.objects.get(user_id=self.request.id)
#         action = request.POST['action']
#         act = actionss()
#         # act.complaint=complaint
#         act.action= action
#         act.status="replyed"
#         act.save()
#         return render(request,'admin/action.html')


class View_Prisoner(TemplateView):
    template_name = 'admin/prisoner_view.html'
    def get_context_data(self, **kwargs):
        context = super(View_Prisoner,self).get_context_data(**kwargs)

        view_prisonerr = add_prisonerr.objects.all()

        context['view_prisonerr'] = view_prisonerr
        return context

class Prisoner_Details(TemplateView):
    template_name = 'admin/prisoner_details.html'
    # def dispatch(self, request,*args, **kwargs):
    #     id1= self.request.GET['id']
    #     view_details = add_prisonerr.objects.get(id=id1)
    #
    #     return render(request,'warden/view_details.html',{'view':view_details})
    def get_context_data(self, **kwargs):
        id1= self.request.GET['id']
        print(id1)
        context = super(Prisoner_Details,self).get_context_data(**kwargs)

        view_detailss = add_prisonerr.objects.filter(id=id1)
        context['view_detailss'] = view_detailss
        return context

class Parole_Request_View(TemplateView):
    template_name = 'admin/parole_request_view.html'

    def get_context_data(self, **kwargs):
        context = super(Parole_Request_View,self).get_context_data(**kwargs)

        view_parole = parole_request.objects.filter(status='added')

        context['view_parole'] = view_parole
        return context

    def post(self , request,*args,**kwargs):
        # complaint = actions.objects.get(user_id=self.request.id)
        id = request.POST['id']
        request_status = request.POST['request_status']
        act = parole_request.objects.get(id=id)
        # act.complaint=complaint
        act.request_status= request_status




        act.status = 'replied'
        act.save()
        return redirect(request.META['HTTP_REFERER'])

class View_Health(TemplateView):
    template_name = 'admin/view_health.html'

    def get_context_data(self, **kwargs):
        context = super(View_Health,self).get_context_data(**kwargs)

        view_health = add_prisonerr.objects.all()

        context['view_health'] = view_health
        return context

class View_Health_Details(TemplateView):
    template_name = 'admin/view_health_details.html'

    def get_context_data(self, **kwargs):
        id= self.request.GET['id']
        print(id)
        context = super(View_Health_Details,self).get_context_data(**kwargs)


        view_health_details = add_health_details.objects.filter(prisoner_id=id)
        print(view_health_details)
        context['view_health_details'] = view_health_details
        return context











