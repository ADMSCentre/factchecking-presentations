from django import forms


class DemographicsForm(forms.Form):
    age = forms.CharField()
    gender = forms.CharField()
    education = forms.CharField()
    country = forms.CharField()
    political = forms.CharField()
    websites = forms.CharField()
    capability = forms.CharField()
    shared = forms.CharField()
    debunked = forms.CharField(required=False)


class QuestionnaireForm(forms.Form):
    cmq_1 = forms.CharField()
    cmq_2 = forms.CharField()
    cmq_3 = forms.CharField()
    cmq_4 = forms.CharField()
    cmq_5 = forms.CharField()
    bos_1 = forms.CharField()
    bos_2 = forms.CharField()
    bos_3 = forms.CharField()
    bos_4 = forms.CharField()
    bos_5 = forms.CharField()
    bos_6 = forms.CharField()


class TaskResponseForm(forms.Form):
    veracity = forms.CharField()
    q1 = forms.CharField()
    q2 = forms.CharField(max_length=2048)
    q3_1 = forms.CharField()
    q3_2 = forms.CharField()
    q3_3 = forms.CharField()

