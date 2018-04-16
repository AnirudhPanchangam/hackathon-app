from django import forms


class  SelectCourseForm(forms.Form):
    course = forms.ChoiceField(choices=(('agriculture','Agriculture'),('apticulture','Apti-Culture'),
    ('horticulture','Horticulture'),('hydroponics','Hydroponics')
    ))