from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
import datetime

from IAPS_app.models import add_prisonerr,add_complaints,parole_request,add_attendancee,add_task,add_schedule
from django.shortcuts import render,redirect


class IndexView(TemplateView):
    template_name = 'warden/warden_index.html'

class Add_Prisoner(TemplateView):
    template_name = 'warden/add_prisoner.html'

    def post(self , request,*args,**kwargs):
        number= request.POST['number']
        name = request.POST['name']
        dob= request.POST['dob']
        age = request.POST['age']
        address = request.POST['address']
        crime = request.POST['crime']
        fir=request.FILES['fir']
        fi=FileSystemStorage()
        filess=fi.save(fir.name,fir)
        join_date = request.POST['join_date']
        release_date = request.POST['release_date']
        image=request.FILES['image']
        fii=FileSystemStorage()
        filesss=fii.save(image.name,image)

        proof=request.FILES['proof']
        fiii=FileSystemStorage()
        files=fiii.save(proof.name,proof)
        if add_prisonerr.objects.filter(number=number):
            print ('pass')
            return render(request,'warden/add_prisoner.html',{'message':"already added the number"})
        else:
            user = User.objects.get(id=self.request.user.id)
            prisonerr = add_prisonerr()
            prisonerr.number = number
            prisonerr.name = name
            prisonerr.dob= dob
            prisonerr.age = age
            prisonerr.address = address
            prisonerr.crime = crime
            prisonerr.fir = filess
            prisonerr.join_date = join_date
            prisonerr.release_date = release_date
            prisonerr.image= filesss
            prisonerr.proof = files
            prisonerr.status = 1
            prisonerr.user = user
            prisonerr.save()


            return render(request, 'warden/add_prisoner.html', {'message': "successfully added"})

class View_Prisoner(TemplateView):
    template_name = 'warden/view_prisoner.html'
    def get_context_data(self, **kwargs):
        context = super(View_Prisoner,self).get_context_data(**kwargs)

        view_prisoner = add_prisonerr.objects.filter(status='1')

        context['view_prisoner'] = view_prisoner
        return context

class View_Details(TemplateView):
    template_name = 'warden/view_details.html'
    # def dispatch(self, request,*args, **kwargs):
    #     id1= self.request.GET['id']
    #     view_details = add_prisonerr.objects.get(id=id1)
    #
    #     return render(request,'warden/view_details.html',{'view':view_details})
    def get_context_data(self, **kwargs):
        id1= self.request.GET['id']
        print(id1)
        context = super(View_Details,self).get_context_data(**kwargs)

        view_details = add_prisonerr.objects.filter(id=id1)
        context['view_details'] = view_details
        return context

class Add_Complaints(TemplateView):
    template_name = 'warden/complaints.html'
    def get_context_data(self, **kwargs):

        context = super(Add_Complaints,self).get_context_data(**kwargs)

        prisoner = add_prisonerr.objects.all()
        context['prisoner'] = prisoner
        return context
    def post(self , request,*args,**kwargs):
        number = request.POST['number']
        name = request.POST['name']
        date = request.POST['date']
        complaint = request.POST['complaint']
        pri=add_prisonerr.objects.get(number=number)
        prisoner_id=pri.id
        complaints = add_complaints()
        complaints.number = number
        complaints.name=name
        complaints.date=date
        complaints.status='added'
        complaints.complaint=complaint
        complaints.prisoner_id=prisoner_id
        complaints.save()


        return render(request, 'warden/warden_index.html', {'message': "add successfully"})

class View_Actions(TemplateView):
    template_name = 'warden/action_view.html'
    def get_context_data(self, **kwargs):
        context = super(View_Actions,self).get_context_data(**kwargs)

        actions = add_complaints.objects.all()



        context['actions'] = actions
        return context

class Parole_Request(TemplateView):
    template_name = 'warden/parole_request.html'
    def get_context_data(self, **kwargs):
        context = super(Parole_Request,self).get_context_data(**kwargs)

        request = add_prisonerr.objects.all()



        context['request'] = request
        return context

    def post(self , request,*args,**kwargs):
        number = request.POST['number']
        name = request.POST['name']
        date = request.POST['date']
        release_reason = request.POST['release_reason']
        parole_period = request.POST['parole_period']
        pri=add_prisonerr.objects.get(number=number)
        prisoner_id=pri.id
        p_request = parole_request()
        p_request.number = number
        p_request.name=name
        p_request.date=date
        p_request.release_reason=release_reason
        p_request.parole_period=parole_period


        p_request.status='added'

        p_request.prisoner_id=prisoner_id
        p_request.save()


        return render(request, 'warden/warden_index.html', {'message': "request successfully"})

class Parole_Request_View(TemplateView):
    template_name = 'warden/parole_request_view.html'

    def get_context_data(self, **kwargs):
        context = super(Parole_Request_View,self).get_context_data(**kwargs)

        parole_request_view = parole_request.objects.all()



        context['parole_request_view'] = parole_request_view
        return context

class Add_Task(TemplateView):
    template_name = 'warden/add_task.html'

    def post(self , request,*args,**kwargs):
        task_name = request.POST['task_name']
        max = request.POST['max']
        add_tasks = add_task()
        add_tasks.task_name = task_name
        add_tasks.max = max
        add_tasks.save()
        return render(request, 'warden/add_task.html', {'message': " successfully added"})

class View_Task(TemplateView):
    template_name = 'warden/view_task.html'

    def get_context_data(self, **kwargs):
        context = super(View_Task,self).get_context_data(**kwargs)

        view_task = add_task.objects.all()

        context['view_task'] = view_task
        return context

class Add_Attendance(TemplateView):
    template_name = 'warden/add_attendance.html'


    def get_context_data(self, **kwargs):

        context = super(Add_Attendance,self).get_context_data(**kwargs)

        add_attendance = add_prisonerr.objects.all()

        context['add_attendance'] = add_attendance
        return context


    def post(self , request,*args,**kwargs):

            attendance = request.POST['attendance']
            num = request.POST['number']
            # currentDate = datetime.datetime.strptime('0/08/2015','%d/%m/%Y').date()
            currentDate = str(datetime.datetime.today()).split()[0]

            if add_attendancee.objects.filter(status='added',number=num,dat=currentDate):
                print ('pass')
                return render(request,'warden/add_attendance.html',{'message':"Attendance Already Added"})

            else:

                add_atten = add_attendancee()

                add_atten.attendance= attendance
                add_atten.number=num

                add_atten.status = 'added'
                add_atten.dat = currentDate

                add_atten.save()
                add=add_attendancee.objects.filter(number=num,attendance='present').count()
                print(add)
                # if add_attendancee.objects.filter(attendance='present'):
                #     cn= add_attendancee.objects.all()
                #
                #     count=0
                #     while cn.count is not 0:
                #
                #         count+=1
                #
                #
                #         add_atten.count = count
                #
                #
                #         add_atten.save()
                #
                #         return redirect(request.META['HTTP_REFERER'])
                #
                #
                #
                # else:
                #
                #     add_atten.save()
                return render(request,'warden/add_attendance.html',{'message':"Add Attendance Successfully"})

class Salary_View(TemplateView):
    template_name = 'warden/salary.html'

    def get_context_data(self, **kwargs):

        context = super(Salary_View,self).get_context_data(**kwargs)

        salary = add_prisonerr.objects.all()
        attendance=add_attendancee.objects.all()

        ls = [i.number for i in salary]
        lis=[]
        dat=[]
        for i in ls :

            a= add_attendancee.objects.filter(number=i,attendance='present').count()
            dat.append(a)
            a=a*100
            lis.append(a)
        x= list(map(lambda f,g,h:{'i':f,'j':g,'k':h},salary,lis,dat))
        print(list(x))
        context['salary'] = salary
        context['data'] = x
        return context


class Attendance_View(TemplateView):
    template_name = 'warden/attendance_view.html'
    def get_context_data(self, **kwargs):

        context = super(Attendance_View,self).get_context_data(**kwargs)

        salary = add_prisonerr.objects.all()
        attendance=add_attendancee.objects.all()

        ls = [i.number for i in salary]
        lis=[]
        dat=[]
        for i in ls :

            a= add_attendancee.objects.filter(number=i,attendance='present').count()
            dat.append(a)
            a=a*100
            lis.append(a)
        x= list(map(lambda f,g,h:{'i':f,'j':g,'k':h},salary,lis,dat))
        print(list(x))
        context['salary'] = salary
        context['data'] = x
        return context

class Add_Schedule(TemplateView)    :
    template_name = 'warden/add_schedule.html'

    def get_context_data(self, **kwargs):

        context = super(Add_Schedule,self).get_context_data(**kwargs)

        add_sche = add_prisonerr.objects.all()
        add_ta = add_task.objects.all()

        context['add_sche'] = add_sche
        context['add_ta'] = add_ta
        return context
    def post(self , request,*args,**kwargs):
        number = request.POST['number']

        task_name= request.POST['task_name']
        pri=add_prisonerr.objects.get(number=number)
        prisoner_id=pri.id
        a=add_task.objects.filter(task_name=task_name).count()
        print(a)
        ma=add_task.objects.get(task_name=task_name)
        print(ma)
        print(max)
        if ma.max > a:
            # currentDate = str(datetime.datetime.today()).split()[0]
            if add_schedule.objects.filter(number=number):

                return render(request,'warden/warden_index.html',{'message':"Task already added"})


            else:
                add_sched= add_schedule()
                add_sched.number= number

                add_sched.task_name=task_name
                add_sched.prisoner_id=prisoner_id


            # add_sched.id=add_tas_id
                add_sched.save()
                messages = "Task Scheduled"
                return render(request,'warden/warden_index.html',{'message':messages})
        else:
            messages = "Maximum Reached"
            return render(request,'warden/warden_index.html',{'message':messages})


class View_Schedule(TemplateView):
    template_name = 'warden/view_schedule.html'

    def get_context_data(self, **kwargs):

        context = super(View_Schedule,self).get_context_data(**kwargs)

        view_schedule = add_task.objects.all()

        context['view_schedule'] = view_schedule
        return context
class View_Scheduled_Task(TemplateView):
    template_name = 'warden/view_schedule_task.html'

    def get_context_data(self, **kwargs):

        task_name= self.request.GET['task_name']
        context = super(View_Scheduled_Task,self).get_context_data(**kwargs)

        view_schedule_task = add_schedule.objects.filter(task_name=task_name)

        context['view_schedule_task'] = view_schedule_task
        return context


class Update_Schedule(TemplateView):
    template_name = 'warden/update_schedule.html'
    def get_context_data(self, **kwargs):

        context = super(Update_Schedule,self).get_context_data(**kwargs)

        add_sche = add_prisonerr.objects.all()
        add_ta = add_task.objects.all()

        context['add_sche'] = add_sche
        context['add_ta'] = add_ta
        return context

    def post(self,request,*args,**kwargs):
        number= request.POST['number']
        task_name = request.POST['task_name']

        update_sche = add_schedule.objects.get(number=number)
        update_sche.task_name=task_name

        update_sche.save()
        update_sche.save()
        messages = "Task updated"
        return render(request,'warden/warden_index.html',{'message':messages})

class Update_Task(TemplateView):
    template_name = 'warden/update_task.html'
    def post(self,request,*args,**kwargs):
        task_name = request.GET['task_name']
        max= request.POST['max']
        update_tas= add_task.objects.get(task_name=task_name)
        update_tas.max= max
        update_tas.save()
        return redirect(request.META['HTTP_REFERER'])





class update_view_details(TemplateView):
    template_name = 'warden/update_view_details.html'
    def get_context_data(self, **kwargs):
        id1= self.request.GET['id']
        print(id1)
        context = super(update_view_details,self).get_context_data(**kwargs)

        view_details = add_prisonerr.objects.filter(id=id1)
        context['view_details'] = view_details
        return context
    def post(self,request,*args,**kwargs):
        join_date = request.POST['join_date']
        release_date = request.POST['release_date']
        id= request.POST['prison_id']
        prisonerr = add_prisonerr.objects.get(id=id)
        prisonerr.join_date = join_date
        prisonerr.release_date = release_date
        prisonerr.save()
        return redirect(request.META['HTTP_REFERER'])



class date_wise_view(TemplateView):
    template_name = 'warden/date_wise_view.html'
    def post(self,request,*args,**kwargs):
        join_date = request.POST['from_date']
        release_date = request.POST['to_date']
        prisonerr = add_prisonerr.objects.filter(release_date__range=(join_date,release_date))
        print(prisonerr)
        return render(request,'warden/date_wise_view.html',{'view_prisoner':prisonerr})

class Remove_Prisoner(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        warden = add_prisonerr.objects.get(pk=id)
        warden.status='remove'
        warden.save()
        return render(request,'warden/warden_index.html',{'message':"Account Removed"})
















