from django.contrib import admin
from .models import applicant_register_tb, company_register_tb1

# Register your models here.


admin.site.register(applicant_register_tb)
admin.site.register(company_register_tb1)