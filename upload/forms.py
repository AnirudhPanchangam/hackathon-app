from django import forms
from django.forms import ModelForm
from core.models import VideoDetails
from .models import CoursesList
from itertools import chain
def get_choices():
    li = []
    ob = CoursesList.objects.all()
    for i in range(0,len(ob)):
        if str(ob[i].course) in chain(*li):
            pass
        else:
            li.append([str(ob[i].course),str(ob[i].course)])
    return li     

class UploadFileForm(forms.Form):
    file = forms.FileField() 
    course = forms.ChoiceField(choices = get_choices())
    vid_name = forms.CharField(max_length= 140)