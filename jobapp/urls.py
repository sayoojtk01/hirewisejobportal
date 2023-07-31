from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('job_cat/', views.job_cat),
    path('job_grid/', views.job_grid),
    path('job_list/', views.job_list),
    path('job_details/', views.job_details),
    path('job_apply/', views.job_apply),
    path('career/', views.career),
    path('about/', views.about),
    path('services/', views.services),
    path('contact/', views.contact),
    path('jobsearch/', views.jobsearch),
    path('jobjobsearch/', views.jobjobsearch),
    


    # ----------------All Action---------------
    path('login/', views.login),
    path('logout/', views.logout),
    



    # ------------------Candidate--------------------------
    path('cregister/', views.companyregister),
    path('candidate/', views.candidate),
    path('applied_job/', views.applied_job),
    path('cand_settings/', views.cand_settings),
    path('candsociallink/', views.candsociallink),
    path('cand_resume/', views.cand_resume),

    # cand_resume


    # ----------------company---------------
    path('register/', views.register),
    path('job_post/', views.job_post),
    path('company/', views.company),
    path('company_dash/', views.company_dash),
    # path('clogout/', views.clogout),
    path('myprofile/', views.myprofile),
    path('com_joblist/', views.com_joblist),
    path('com_settings/', views.com_settings),
    path('contact2/', views.contact2),
    path('passwordchange/', views.passwordchange),
    path('comdelete/', views.comdelete),
    path('job_del/', views.job_del),
    path('shortlisting/', views.shortlisting),
    path('rejected/', views.rejected),
    path('viewshortlisted/',views.viewshortlisted),
    path('setinterview/',views.setinterview),
    path('viewinterview/',views.viewinterview),
    path('allcandidate/',views.allcandidate),


]


