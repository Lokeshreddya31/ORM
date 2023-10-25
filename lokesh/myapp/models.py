from django.db import models
from django.contrib import admin
class foodball_player (models.Model):
    p_name=models.CharField(max_length=20)
    p_country=models.CharField(max_length=100)
    p_age=models.IntegerField()
    P_salary=models.IntegerField()
    p_email=models.EmailField()

class foodball_playerAdmin(admin.ModelAdmin):
   list_display=('p_name','p_country','P_salary','p_age','p_email')
