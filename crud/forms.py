from django import forms
from .models import User

class Userform(forms.ModelForm):
    
    class Meta:
        model=User
        fields='__all__'

    def __init__(self,*args,**kwargs):
        super(Userform,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label="Select"
        self.fields['mobile'].required=False