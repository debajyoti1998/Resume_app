from django import forms
from .models import Resume


GENDER_CHOICE=(
    ('male','male'),
    ('female','female')
)
class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICE,widget=forms.RadioSelect)

    class Meta:
        model=Resume
        fields=['name','email','DOB','address','state','city','gender','profile_image']
        # widgets={'name':forms.TextInput(attrs={'class':'form-control'})}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'DOB':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'})
        }