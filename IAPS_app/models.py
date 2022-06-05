
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class warden_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField('images/',null=True)
    con_password=models.CharField(max_length=50,null=True)
    experience= models.FileField('file/',null=True)

class medical_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField('images/',null=True)
    con_password=models.CharField(max_length=50,null=True)
    experience = models.FileField('file/', null=True)

class add_prisoner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=50)
    crime = models.CharField(max_length=50)
    fir= models.FileField('file/',null=True)
    join_date = models.DateField(null=True)
    release_date = models.DateField(null=True)
    image=models.ImageField('images/',null=True)
    proof= models.FileField('file/',null=True)
    dob = models.DateField(null=True)


class add_prisonerr(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    warden = models.ForeignKey(warden_reg, on_delete=models.CASCADE,null=True)
    number = models.IntegerField(null=True)
    name = models.CharField(max_length=50,null=True)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=50,null=True)
    crime = models.CharField(max_length=50,null=True)
    fir= models.FileField('file/',null=True)
    join_date = models.DateField(null=True)
    release_date = models.DateField(null=True)
    image=models.ImageField('images/',null=True)
    proof= models.FileField('file/',null=True)
    status= models.CharField(max_length=100,null=True)


class add_complaints(models.Model):
    prisoner = models.ForeignKey(add_prisonerr, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    warden = models.ForeignKey(warden_reg, on_delete=models.CASCADE,null=True)

    number = models.IntegerField(null=True)
    name = models.CharField(max_length=50)
    date = models.DateField(null=True)
    complaint = models.CharField(max_length=50)
    status= models.CharField(max_length=100,null=True)
    action = models.CharField(max_length=50,null=True)

class parole_request(models.Model):
    prisoner = models.ForeignKey(add_prisonerr, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    warden = models.ForeignKey(warden_reg, on_delete=models.CASCADE,null=True)

    number = models.IntegerField(null=True)
    name = models.CharField(max_length=50)
    date = models.DateField(null=True)
    release_reason = models.CharField(max_length=50)
    parole_period = models.CharField(max_length=50)
    request_status = models.CharField(max_length=50,null=True)
    status= models.CharField(max_length=100,null=True)

class add_health_details(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    prisoner = models.ForeignKey(add_prisonerr, on_delete=models.CASCADE,null=True)
    height = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=50)
    allergies = models.CharField(max_length=50)
    deseases = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    bp = models.CharField(max_length=50)
    medication = models.CharField(max_length=50)
    reading_date = models.DateField(null=True)
    status= models.CharField(max_length=100,null=True)

class add_task(models.Model):
    warden = models.ForeignKey(warden_reg, on_delete=models.CASCADE,null=True)
    task_name = models.CharField(max_length=50)
    max = models.IntegerField(null=True)
    status= models.CharField(max_length=100,null=True)

class add_attendancee(models.Model):
    prisoner = models.ForeignKey(add_prisonerr, on_delete=models.CASCADE,null=True)
    number = models.CharField(max_length=50,null=True)
    dat = models.DateField(null=True)
    attendance=models.CharField(max_length=50)
    count = models.IntegerField(null=True)
    status= models.CharField(max_length=100,null=True)

class add_schedule(models.Model):
    prisoner = models.ForeignKey(add_prisonerr, on_delete=models.CASCADE,null=True)
    add_tas = models.ForeignKey(add_task, on_delete=models.CASCADE,null=True)
    number = models.CharField(max_length=50,null=True)
    week = models.IntegerField(null=True)
    task_name = models.CharField(max_length=50,null=True)
    dat = models.DateField(auto_now=True)
    status= models.CharField(max_length=100,null=True)


























