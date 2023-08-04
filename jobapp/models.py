from django.db import models


from datetime import datetime

from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
   

class company_register_tb1(models.Model):
    name=models.CharField(max_length=255)
    lname=models.CharField(max_length=225)
    uname=models.CharField(max_length=225)
    uname=models.CharField(max_length=225)
    cname=models.CharField(max_length=225)
    ctype=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    password = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    pinterest = models.CharField(max_length=255)
    dribble = models.CharField(max_length=255)
    behance = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="images/")
    cover = models.ImageField(upload_to="images/")
    working = models.CharField(max_length=255)
    description = models.CharField(max_length=255)



class post_job_tb(models.Model):
    cid= models.ForeignKey(company_register_tb1, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    desc=models.CharField(max_length=225)
    cat=models.CharField(max_length=225)
    type=models.CharField(max_length=225)
    salary=models.CharField(max_length=225)
    min=models.CharField(max_length=225)
    max=models.CharField(max_length=225)
    skills=models.CharField(max_length=225)
    qualification=models.CharField(max_length=225)
    exp=models.CharField(max_length=225)
    require=models.CharField(max_length=225)
    nos=models.CharField(max_length=225)
    loca=models.CharField(max_length=225)
    postdate=models.CharField(max_length=225)
    lastdata=models.DateField()
    status=models.CharField(max_length=255,default="active")

    




class applicant_register_tb(models.Model):
    name=models.CharField(max_length=255)
    lname=models.CharField(max_length=225)
    uname=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    password = models.CharField(max_length=255)
    profile=models.ImageField(upload_to="userprofile/")
    cv=models.FileField(upload_to="cv/")
    dob=models.CharField(max_length=225)
    loction=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    website=models.CharField(max_length=225)
    companyname=models.CharField(max_length=225)
    designation=models.CharField(max_length=225)
    qualification=models.CharField(max_length=225)
    language=models.CharField(max_length=225) 
    desc=models.CharField(max_length=225)
    linkedin=models.CharField(max_length=225)
    github=models.CharField(max_length=225)
    dribbble=models.CharField(max_length=225)
    pinterest=models.CharField(max_length=225)
    




class apply_job_tb(models.Model):
    cmid= models.ForeignKey(company_register_tb1, on_delete=models.CASCADE)
    uid= models.ForeignKey(applicant_register_tb, on_delete=models.CASCADE)
    jid= models.ForeignKey(post_job_tb, on_delete=models.CASCADE)
    status=models.CharField(max_length=255,default="pending")
    date=models.DateField()


class interview_tb(models.Model):
    aplyid=models.ForeignKey(apply_job_tb, on_delete=models.CASCADE)
    cmid= models.ForeignKey(company_register_tb1, on_delete=models.CASCADE)
    uid= models.ForeignKey(applicant_register_tb, on_delete=models.CASCADE)
    jid= models.ForeignKey(post_job_tb, on_delete=models.CASCADE)
    date=models.DateField(max_length=225)
    time=models.CharField(max_length=225)
    require=models.CharField(max_length=225)
    msg=models.CharField(max_length=225)
    loca=models.CharField(max_length=225)
    link=models.CharField(max_length=225)

    

@receiver(post_save,sender=post_job_tb)
def update_status_on_lastdata(sender, instance, **kwargs):
    if instance.lastdata < str(timezone.now().date()):
        instance.status = "deactive"
        instance.save()