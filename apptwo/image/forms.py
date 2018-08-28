from django import forms
from image.models import sign_up

class user_sign(forms.ModelForm):
    class Meta():
        model = sign_up
        fields = ('__all__')
