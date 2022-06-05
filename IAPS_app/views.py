import random

from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from IAPS_app.models import UserType,warden_reg,medical_reg
from django.contrib.auth import login, authenticate
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        det = User.objects.get(id=1)
        det.last_name = 1
        det.save()

        if user is not None:

            login(request, user)
            if user.last_name == '1':

                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "warden":
                    return redirect('/warden')
                # elif UserType.objects.get(user_id=user.id).type == "health_officer":
                #     return redirect('/health_officer')
                else:
                    return redirect('/health_officer')

            else:

                return render(request, 'index.html', {'message': " User Account Not Authenticated"})
        else:

            return render(request, 'index.html', {'message': "Invalid Username or Password"})


class Jailer_Reg(TemplateView):
    template_name = 'jailer_reg.html'

    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        # designation = request.POST['designation']
        experience=request.FILES['experience']
        fi1=FileSystemStorage()
        filess=fi1.save(experience.name,experience)
        # r=random.randint[100,10000]
        # warden_id=request.POST['warden_id']
        email= request.POST['email']
        image=request.FILES['image']
        fi=FileSystemStorage()
        files=fi.save(image.name,image)
        username = request.POST['username']
        password = request.POST['password']
        con_password = request.POST['con_password']
        if password==con_password:
            if User.objects.filter(email=email,username=username):
                print ('pass')
                return render(request,'jailer_reg.html',{'message':"already added the username or email"})

            else:
                user = User.objects._create_user(username=username,password=password,email=email,first_name=name,is_staff='0',last_name='0')
                user.save()
                warden = warden_reg()
                warden.user = user
                # warden.designation = designation
                warden.experience=filess
                r = random.randint(1,100)
                warden.warden_id =r
                warden.image = files
                warden.con_password=con_password
                warden.save()
                usertype = UserType()
                usertype.user = user
                usertype.type = "warden"
                usertype.save()


                return render(request, 'jailer_reg.html', {'message': "successfully added"})
        else:
            return render(request, 'medical_reg.html', {'message': "password does not match"})





class Medical_Reg(TemplateView):
    template_name = 'medical_reg.html'

    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        experience = request.FILES['experience']
        fi1 = FileSystemStorage()
        filess = fi1.save(experience.name, experience)
        # designation = request.POST['designation']
        # department=request.POST['department']
        email= request.POST['email']
        image=request.FILES['image']
        fi=FileSystemStorage()
        files=fi.save(image.name,image)
        username = request.POST['username']
        password = request.POST['password']
        con_password = request.POST['con_password']
        if password == con_password:
            if User.objects.filter(email=email,username=username):
                print ('pass')
                return render(request,'medical_reg.html',{'message':"already added the username or email"})

            else:
                user = User.objects._create_user(username=username,password=password,email=email,first_name=name,is_staff='0',last_name='0')
                user.save()
                medical = medical_reg()
                medical.user = user
                # medical.designation = designation
                # medical.department =department
                medical.image = files
                medical.experience= filess
                medical.con_password=con_password
                medical.save()
                usertype = UserType()
                usertype.user = user
                usertype.type = "medical"
                usertype.save()

                return render(request, 'medical_reg.html', {'message':"successfully added"})
        else:
            return render(request, 'medical_reg.html', {'message': "password does not match"})


class Forgot_Password(TemplateView):
    template_name = 'forget_password.html'
    def get_context_data(self, **kwargs):
        context=super(Forgot_Password,self).get_context_data(**kwargs)
        warden=warden_reg.objects.filter(user__last_name='1').count()
        medical =medical_reg.objects.filter(user__last_name='1').count()
        admin=User.objects.get(is_superuser='1')
        context['warden'] = warden
        context['medical'] = medical
        context['admin']=admin
        return context
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        print(username)

        email= request.POST['email']
        print(email)
        user_id=self.request.user.id
        if User.objects.filter(last_name='1',username=username,email=email):
           user=User.objects.get(last_name='1',username=username,email=email)
           Type=UserType.objects.get(user_id=user.id)
           if Type.type=='warden':
              warden=warden_reg.objects.get(user_id=user.id)
              Password=warden.con_password
              email = EmailMessage(
              Password,
              'Your password',
              settings.EMAIL_HOST_USER,
              [user.email],
              )
              email.fail_silently = False
              email.send()
              return render(request,'index.html',{'message':"Send mail successfully"})
           elif Type.type=='medical':

              medical=medical_reg.objects.get(user_id=user.id)
              print(user)
              email = EmailMessage(
              medical.con_password,
              'Your password',
              settings.EMAIL_HOST_USER,
              [user.email],
               )
              email.fail_silently = False
              email.send()
              return render(request,'index.html',{'message':"Send mail successfully"})

        else:
           return render(request,'index.html',{'message':"Tis User Is Not Exist"})





