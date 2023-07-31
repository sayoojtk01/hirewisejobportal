from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import redirect,HttpResponseRedirect
import os
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.core.paginator import Paginator




# --------------MAIN PART----------------- #



def index(request):
    
    query1=post_job_tb.objects.filter(status="active").order_by('-id')
    paginator=Paginator(query1,6)
    page_num=request.GET.get('page',1)

    query1=paginator.page(page_num)
    return render(request,"main/index.html",{"data":query1})


def jobsearch(request):
    if request.method=="POST":
        q=request.POST['q']
        b=request.POST['b']

        if q and b:
            query1=post_job_tb.objects.filter(title__icontains=q,loca__icontains=b,status="active").order_by('-id')

        elif b:
            query1=post_job_tb.objects.filter(loca__icontains=b,status="active").order_by('-id')

        elif q:
            query1=post_job_tb.objects.filter(title__icontains=q,status="active").order_by('-id')

        
        else:
            query1=post_job_tb.objects.filter(status="active").order_by('-id')
        
        #pagination in django
        paginator=Paginator(query1,1)
        page_num=request.GET.get('page',1)
        query1=paginator.page(page_num)

        return render(request,"main/index.html",{"data":query1})
        
    else:
        #pagination in django
        paginator=Paginator(query1,1)
        page_num=request.GET.get('page',1)
        query1=paginator.page(page_num)

        query1=post_job_tb.objects.filter(status="active").order_by('-id')
        return render(request,"main/index.html",{"data":query1})




def job_cat(request):
    return render(request,"main/job-categories.html")



def job_grid(request):
    query1=post_job_tb.objects.filter(status="active").order_by('-id')


    #pagination in django
    paginator=Paginator(query1,1)
    page_num=request.GET.get('page',1)
    query1=paginator.page(page_num)

    return render(request,"main/job-grid-four.html",{"data":query1})



def jobjobsearch(request):
    if request.method=="POST":
        q=request.POST['q']
        b=request.POST['b']

        if q and b:
            
            query1=post_job_tb.objects.filter(title__icontains=q,loca__icontains=b,status="active").order_by('-id')

        elif b:
            query1=post_job_tb.objects.filter(loca__icontains=b,status="active").order_by('-id')

        elif q:
            query1=post_job_tb.objects.filter(title__icontains=q,status="active").order_by('-id')

        
        else:
            query1=post_job_tb.objects.filter(status="active").order_by('-id')

        #pagination in django
        paginator=Paginator(query1,1)
        page_num=request.GET.get('page',1)
        query1=paginator.page(page_num)
        
        return render(request,"main/job-grid-four.html",{"data":query1})
        
    else:
        #pagination in django
        paginator=Paginator(query1,1)
        page_num=request.GET.get('page',1)
        query1=paginator.page(page_num)

        query1=post_job_tb.objects.filter(status="active").order_by('-id')
        return render(request,"main/job-grid-four.html",{"data":query1})
    



def job_list(request):
    query1=post_job_tb.objects.filter(status="active").order_by('-id')
    return render(request,"main/job-list-three.html",{"data":query1})

def job_details(request):
    jobid=request.GET['jobid']
    query1=post_job_tb.objects.filter(id=jobid)
    return render(request,"main/job-detail-three.html",{"data":query1})


def job_apply(request):
    if request.session.has_key('id'):
        userid=request.session['id']
        jobid=request.GET['jobid']
        data=post_job_tb.objects.filter(id=jobid)
        for x in data:
            cmid=x.cid.id

        com=company_register_tb1.objects.get(id=cmid)

        user=applicant_register_tb.objects.get(id=userid)

        jobs=post_job_tb.objects.get(id=jobid)

        # for mail function
        user2=applicant_register_tb.objects.filter(id=userid)
        for i in user2:
            uname=i.uname
            umail=i.email

        

        # for mail function
        jobs2=post_job_tb.objects.filter(id=jobid)
        for x in jobs2:
            title=x.title
            comna=x.cid.cname


        # for alredy checking
        check=apply_job_tb.objects.filter(jid=jobid,uid=userid)
        if check:
            return HttpResponse("Already Applied")
        else:
            add=apply_job_tb(cmid=com,uid=user,jid=jobs,status="pending")
            add.save()


            # send mail
            subject = 'HireWIse Applied'
            message = f'Hi {uname} HireWIse apllication for, {title} ,{comna} Applied Successfully'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [umail, ] 
            send_mail( subject, message, email_from, recipient_list )


            return HttpResponse("Applied Successfully ")
    else:
        return HttpResponseRedirect('/candidate/')
        

def career(request):
    return render(request,"main/career.html")

def about(request):
    return render(request,"main/aboutus.html")

def services(request):
    return render(request,"main/services.html")

def contact(request):
    return render(request,"main/contact.html")




# ------------common login and logout-------------



def login(request):
    if request.method=="POST":
        lemail=request.POST['email']
        lpassword=request.POST['password']
        check=applicant_register_tb.objects.filter(email=lemail,password=lpassword)
        check2=company_register_tb1.objects.filter(email=lemail,password=lpassword)
        if check:
            for x in check:
                request.session["id"]=x.id
                request.session["uname"]=x.uname
                usid=x.id
                query1=applicant_register_tb.objects.filter(id=usid)
            return render(request,"main/candidate.html",{"data":query1})
        elif check2:
            for x in check2:
                request.session["mid"]=x.id
                request.session["cname"]=x.cname
                mid=x.id
                print(mid)
                query1=company_register_tb1.objects.filter(id=mid)
            return render(request,"company/myprofile.html",{"data1":query1})
        else:            
            return render(request,"main/login.html",{"erorr":"Unregistered please register"})
    else:
        return render(request,"main/login.html")
    
def logout(request):

    if request.session.has_key('id'):
        del request.session["id"]
        del request.session["uname"]
        return redirect("/login/")
    elif request.session.has_key('mid'):
        del request.session["mid"]
        del request.session["cname"]
        return redirect("/login/")
    else:
        return redirect("/")
    

    
    

    
# ------------------CANDIDATE----------------------


def register(request):
    if request.method=="POST":
        fname=request.POST['firstname1']
        lname=request.POST['lastname1']
        uname=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['confirmpassword']
        profile=request.FILES['profic']
        cv=request.FILES['resume']
       
        check=applicant_register_tb.objects.filter(email=email)
        check2=applicant_register_tb.objects.filter(uname=uname)
        if password==cpassword:
            if check:
                return render(request,"main/signup.html",{"error":"User already exist !"})
            elif check2:
                return render(request,"main/signup.html",{"error2":"User Name already exist ! Try Another"})
            else:
                add=applicant_register_tb(name=fname,lname=lname,uname=uname,email=email,password=password,
                                          profile=profile,cv=cv)
                add.save()
                return render(request,"main/login.html",{"success":"Registered Successfully Please Login !"})
        else:
            return render(request,"main/signup.html",{"error":"Passwords doesn't match !"})
    else:
        return render(request,"main/signup.html")
    


def candidate(request):
    if request.session.has_key('id'):
        if request.method=="POST":
            fname=request.POST['fname']
            lname=request.POST['lname']
            birth=request.POST['birth']
            location=request.POST['location']
            phone=request.POST['phone']
            website=request.POST['website']
            companyname=request.POST['companyname']
            designation=request.POST['designation']
            qualification=request.POST['qualification']
            language=request.POST['language']
            desc=request.POST['desc']
            mid=request.session['id']
            add=applicant_register_tb.objects.filter(id=mid).update(name=fname,lname=lname,dob=birth,loction=location,
                                                                    phone=phone,website=website,companyname=companyname,
                                                                    designation=designation,qualification=qualification,
                                                                    language=language,desc=desc)
            return HttpResponseRedirect('/candidate/')
            

        else:
            mid=request.session['id']
            query1= applicant_register_tb.objects.filter(id=mid)
            return render(request,"main/candidate.html",{"data":query1})
    else:
        return HttpResponseRedirect('/login/')
    

def applied_job(request):
    if request.session.has_key('id'):
        return render(request,"main/cand_applied_jobs.html")
    else:
        return HttpResponseRedirect('/login/')
    

def cand_settings(request):
    if request.session.has_key('id'):
        return render(request,"main/cand_settings.html")
    else:
        return HttpResponseRedirect('/login/')



def candsociallink(request):
    if request.session.has_key('id'):
        linkedin=request.POST['linkedin']
        github=request.POST['github']
        dribbble=request.POST['dribbble']
        pinterest=request.POST['pinterest']
        mid=request.session['id']
        add=applicant_register_tb.objects.filter(id=mid).update(linkedin=linkedin,
                                                                github=github,dribbble=dribbble,pinterest=pinterest)
        return HttpResponseRedirect('/candidate/')
    else:
        return HttpResponseRedirect('/login/')
    


def cand_resume(request):
    if request.session.has_key('id'):
        if request.method=="POST":
            mid=request.session['id']
            ad_cv=request.FILES["cv"]
            oldrec=applicant_register_tb.objects.filter(id=mid)
            updrec=applicant_register_tb.objects.get(id=mid)
            for x in oldrec:
                cvurl=x.cv.url
                pathtocv=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+cvurl
                if os.path.exists(pathtocv):
                    os.remove(pathtocv)
                    print('Successfully deleted')
            updrec.cv=ad_cv
            updrec.save()

            return HttpResponseRedirect('/cand_resume/',{"msg":"Resume Updated Successfully !"})
        else:
            mid=request.session['id']
            query1= applicant_register_tb.objects.filter(id=mid)
            return render(request,"main/cand_resume.html",{"data":query1})
    else:
        return HttpResponseRedirect('/login/')







# ------------------COMPANY----------------------



def companyregister(request):
    if request.method=="POST":
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        uname=request.POST['username']
        email=request.POST['email']
        cname=request.POST['companyname']
        ctype=request.POST['select']
        password=request.POST['password']
        cpassword=request.POST['confirmpassword']
        logo=request.FILES['logo']
        cover=request.FILES['cover']
       
        check=company_register_tb1.objects.filter(email=email)
        check2=company_register_tb1.objects.filter(uname=uname)
        if password==cpassword:
            if check:
                return render(request,"main/signup.html",{"error":"User already exist !"})
            elif check2:
                return render(request,"main/signup.html",{"error2":"User Name already exist ! Try Another"})
            else:
                add=company_register_tb1(name=fname,lname=lname,uname=uname,cname=cname,ctype=ctype,email=email,password=password,
                                        logo=logo,cover=cover)
                add.save()
                return render(request,"main/login.html")
        else:
            return render(request,"main/signup.html",{"error":"Passwords doesn't match !"})
    else:
        return render(request,"main/signup.html")
    


# def company(request):
#     if request.session.has_key('mid'):
#         mid=request.session['mid']
#         query=company_register_tb1.objects.filter(id=mid)
#         return render(request,"company/company.html",{"data1":query})
#     else:
#         return HttpResponseRedirect('/login/')

def company(request):
    if request.session.has_key('mid'):
        mid=request.session['mid']
        q= company_register_tb1.objects.filter(id=mid)
        query2=post_job_tb.objects.filter(cid=mid)
        return render(request,"company/company.html",{"data":q,"data2":query2})
    else:
        return HttpResponseRedirect('/login/')

def company_dash(request):
    if request.session.has_key('mid'):
        mid=request.session['mid']
        query1=company_register_tb1.objects.filter(id=mid)
        query2=apply_job_tb.objects.filter(cmid=mid,status="pending")

        paginator=Paginator(query2,15)
        page_num=request.GET.get('page',1)
        query2=paginator.page(page_num)


        return render(request,"company/dashboard.html",{"data":query1,"data2":query2})
    else:
        return HttpResponseRedirect('/login/')
    


def job_post(request):
    if request.session.has_key('mid'):
        if request.method=="POST":
            # mid=request.request.session.session_key
            mid=request.session['mid']
            title=request.POST['title']
            desc=request.POST['desc']
            cat=request.POST['cat']
            type=request.POST['type']
            salary=request.POST['salary']
            min=request.POST['min']
            max=request.POST['max']
            skills=request.POST['skills']
            qualification=request.POST['qualification']
            exp=request.POST['exp']
            require=request.POST['require']
            nos=request.POST['nos']
            loca=request.POST['loca']
            post=timezone.now().date()
            enddate=request.POST['endate']
            com=company_register_tb1.objects.get(id=mid)
            add=post_job_tb(title=title,desc=desc,cat=cat,type=type,salary=salary,min=min,max=max,skills=skills,qualification=qualification,
                            exp=exp,require=require,nos=nos,loca=loca,cid=com,postdate=post,lastdata=enddate,status="active")
            add.save()
            return render(request,"company/job-post.html",{"msg":"Post Job Succesussfully"})

        else:    
            return render(request,"company/job-post.html")
    else:
        return HttpResponseRedirect('/login/')
    


def myprofile(request):
    if request.session.has_key('mid'):
        if request.method=="POST":
            
            companyname=request.POST['companyname']
            companytype=request.POST['companytype']
            companysize=request.POST['companysize']
            location=request.POST['location']
            website=request.POST['website']
            facebook=request.POST['facebook']
            twitter=request.POST['twitter']
            linkedin=request.POST['linkedin']
            pinterest=request.POST['pinterest']
            dribble=request.POST['dribble']
            behance=request.POST['behance']
            workingfield=request.POST['workingfield']
            description=request.POST['description']
            mid=request.GET['regid']
            checkbox=request.POST["imgup"]
            checkbox2=request.POST["imgup2"]

            if checkbox == "yes":
                ad_image=request.FILES["logo"]
                oldrec=company_register_tb1.objects.filter(id=mid)
                updrec=company_register_tb1.objects.get(id=mid)
                for x in oldrec:
                    imageurl=x.logo.url
                    pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imageurl
                    if os.path.exists(pathtoimage):
                        os.remove(pathtoimage)
                        print('Successfully deleted1')
                updrec.logo=ad_image
                updrec.save()
                print("-----------------1-----------------")

            if checkbox2 == "yes":
                ad_image2=request.FILES["cover"]
                oldrec=company_register_tb1.objects.filter(id=mid)
                updrec=company_register_tb1.objects.get(id=mid)
                for x in oldrec:
                    imageurl=x.cover.url
                    pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imageurl
                    if os.path.exists(pathtoimage):
                        os.remove(pathtoimage)
                        print('Successfully deleted2')
                updrec.cover=ad_image2
                updrec.save()
                print("-----------------2-----------------")


            add=company_register_tb1.objects.filter(id=mid).update(cname=companyname,ctype=companytype,
                        size=companysize,location=location,website=website,twitter=twitter,facebook=facebook,linkedin=linkedin,
                        pinterest=pinterest,dribble=dribble,behance=behance,working=workingfield,description=description)
            return HttpResponseRedirect('/myprofile/')
        else:
            mid=request.session['mid']
            query=company_register_tb1.objects.filter(id=mid)
            
            return render(request,"company/myprofile.html",{"data1":query})
    else:
        return HttpResponseRedirect('/login/')
    


def com_joblist(request):
    if request.session.has_key('mid'):
        mid=request.session['mid']
        # q= company_register_tb1.objects.filter(id=mid)
        query2=post_job_tb.objects.filter(cid=mid)
        return render(request,"company/com_joblist.html",{"data":query2})
    else:
        return HttpResponseRedirect('/login/')
    


def com_settings(request):
    if request.session.has_key('mid'):
        return render(request,"company/com_settings.html")
    else:
        return HttpResponseRedirect('/login/')


def contact2(request):
    if request.session.has_key('mid'):
        return render(request,"company/contact2.html")
    else:
        return HttpResponseRedirect('/login/')


def passwordchange(request):
    if request.session.has_key('mid'):
        if request.method=="POST":
            mid=request.session['mid']
            oldpsd=request.POST['oldpassword']
            psd=request.POST['newpassword']
            cpsd=request.POST['confirmpassword']
            check=company_register_tb1.objects.filter(password=oldpsd)
            if psd == cpsd :
                if check:
                    add=company_register_tb1.objects.filter(id=mid).update(password=psd)
                    return HttpResponseRedirect(request,"company/com_settings.html",{"error":"Change Password Successfully"})
                else:
                    return render(request,"company/com_settings.html",{"error":"Old Password Is Not Match!"})
            else:
                return render(request,"company/com_settings.html",{"error":"Passwords Are Not Match!"})
    else:
        return HttpResponseRedirect('/login/')
    

def comdelete(request):
    if request.session.has_key('mid'):
        mid=request.session['mid']
        del request.session["mid"]
        del request.session["cname"]
        data=company_register_tb1.objects.filter(id=mid).delete()
        data2=post_job_tb.objects.filter(mid=mid).delete()
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect('/login/')
    

def job_del(request):
    if request.session.has_key('mid'):
        jobid=request.GET['jobid']
        data2=post_job_tb.objects.filter(id=jobid).update(status="deactive")
        return HttpResponseRedirect("/company/")
    else:
        return HttpResponseRedirect('/login/')


def shortlisting(request):
    if request.session.has_key('mid'):
        mid=request.session['mid']
        # userid=request.GET["userid"]
        jobid=request.GET["jobid"]
        data2=apply_job_tb.objects.filter(id=jobid).update(status="shortlisted")

        # # for mail function
        # data=applicant_register_tb.objects.filter(id=userid)
        # for x in data:
        #     umail=x.email
        #     uname=x.uname

        jobs=apply_job_tb.objects.filter(id=jobid)
        for x in jobs:
            title=x.jid.title
            com=x.cmid.cname
            umail=x.uid.email
            uname=x.uid.uname

        subject = 'Shortlisted'
        message = f'Hi {uname} HireWIse apllication for, {title} ,{com} Was Shortlisted'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [umail, ] 
        send_mail( subject, message, email_from, recipient_list ) 



        return HttpResponseRedirect("/company_dash/")
    else:
        return HttpResponseRedirect('/login/')
    
def rejected(request):
    if request.session.has_key('mid'):
        mid=request.session['mid']
        jobid=request.GET["jobid"]
        data2=apply_job_tb.objects.filter(id=jobid).update(status="rejected")

        jobs=apply_job_tb.objects.filter(id=jobid)
        for x in jobs:
            title=x.jid.title
            com=x.cmid.cname
            umail=x.uid.email
            uname=x.uid.uname

        subject = 'Application update'
        message = f'Hi {uname} apllication for, {title} ,Unfortunately,  {com}  has decided not to move forward with your application at this time.While we wish we had better news, continuing to search and apply for jobs will help you maintain your momentum.Best of luck,The HireWise team'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [umail, ] 
        send_mail( subject, message, email_from, recipient_list ) 


        return HttpResponseRedirect("/company_dash/")
    else:
        return HttpResponseRedirect('/login/')
    

def viewshortlisted(request):
    if request.session.has_key('mid'):
        mid=request.session['mid']
        
        query2=apply_job_tb.objects.filter(cmid=mid,status="shortlisted")

        paginator=Paginator(query2,15)
        page_num=request.GET.get('page',1)
        query2=paginator.page(page_num)

        return render(request,"company/shortlisted.html",{"data2":query2})
    else:
        return HttpResponseRedirect('/login/')
    

def setinterview(request):
    if request.session.has_key('mid'):

        if request.method=="POST":
            jobid=request.GET["jobid"]
            time=request.POST['time']
            date=request.POST['date']
            location=request.POST['location']
            require=request.POST['require']
            msg=request.POST['msg']
            lin=request.POST['type']
            applyid=apply_job_tb.objects.get(id=jobid)

            data=apply_job_tb.objects.filter(id=jobid)
            for x in data:
                comid=x.cmid.id
                usid=x.uid.id
                joid=x.jid.id

            com_data=company_register_tb1.objects.get(id=comid)
            usr_data=applicant_register_tb.objects.get(id=usid)
            job_data=post_job_tb.objects.get(id=joid)

            add=interview_tb(aplyid=applyid,date=date,time=time,
                             require=require,msg=msg,loca=location,link=lin,
                             cmid=com_data,uid=usr_data,jid=job_data)
            
            add.save()



            jobs=apply_job_tb.objects.filter(id=jobid)
            for x in jobs:
                title=x.jid.title
                com=x.cmid.cname
                umail=x.uid.email
                uname=x.uid.uname


            if lin=='online':

                subject = 'Interview Invitation'
                message = f'Hi online'
                email_from = settings.EMAIL_HOST_USER 
                recipient_list = [umail, ] 
                send_mail( subject, message, email_from, recipient_list ) 

            else:
                subject = 'Interview Invitation'
                message = f'Hi offline'
                email_from = settings.EMAIL_HOST_USER 
                recipient_list = [umail, ] 
                send_mail( subject, message, email_from, recipient_list ) 


            data2=apply_job_tb.objects.filter(id=jobid).update(status="setinterview")
            return HttpResponseRedirect("/viewshortlisted/")
        else:
        
            jobid=request.GET["jobid"]
            query2=apply_job_tb.objects.filter(id=jobid)
            return render(request,"company/interview.html",{"data2":query2})
    else:
        return HttpResponseRedirect('/login/')
    



def viewinterview(request):
    if request.session.has_key('mid'):
        mid=request.session['mid']
        
        query2=interview_tb.objects.filter(cmid=mid)

        paginator=Paginator(query2,15)
        page_num=request.GET.get('page',1)
        query2=paginator.page(page_num)

        return render(request,"company/viewinterviewcand.html",{"data2":query2})
    else:
        return HttpResponseRedirect('/login/')
    


def allcandidate(request):
    if request.session.has_key('mid'):
        mid=request.session['mid']
        query2=apply_job_tb.objects.filter(cmid=mid)

        paginator=Paginator(query2,15)
        page_num=request.GET.get('page',1)
        query2=paginator.page(page_num)
        
        
        return render(request,"company/allcandidates_apply.html",{"data2":query2})
    else:
        return HttpResponseRedirect('/login/')