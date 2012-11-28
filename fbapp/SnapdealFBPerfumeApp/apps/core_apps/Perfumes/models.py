from django.db import models
from django.contrib import admin



class PerfumeLinkDetail(models.Model):
    GENDER = (
        ('M','male'),
        ('F','female'),
        )
    weblink = models.URLField(null=True,  blank=True)
    gender = models.CharField(max_length=2, choices=GENDER)
    description = models.TextField(null=True, blank=True)
    is_enabled = models.BooleanField(default=False)
    create_date = models.DateField(auto_now_add=True)
    caption=models.CharField(max_length=200,null=True, blank=True)
    title=models.CharField(max_length=200,null=True, blank=True)
    link_weight = models.CharField(max_length=200,null=False, blank=False)
    image_link =  models.URLField(null=True,  blank=True)



def __unicode__(self):
        return self.weblink

class Question(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    def __unicode__(self):
        return self.title
class Option(models.Model):
    question = models.ForeignKey(Question, null=True, blank=True)
    description = models.CharField(max_length=100, null=False, blank=False)
    weight = models.DecimalField(null=True, blank=True,max_digits=5, decimal_places=2)

def __unicode__(self):
        return self.description

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(PerfumeLinkDetail)



