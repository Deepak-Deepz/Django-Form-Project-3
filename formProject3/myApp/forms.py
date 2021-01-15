from django import forms
from django.core import validators
class SignupForm(forms.Form):
    name = forms.CharField()
    roll = forms.IntegerField()
    email = forms.EmailField()
    phone = forms.CharField()
    comments = forms.CharField(widget = forms.Textarea)
    AreUAnEngineeringStudent = forms.BooleanField()
    password = forms.CharField(widget = forms.PasswordInput)
    repassword = forms.CharField(label="Pls Re-enter the password",widget = forms.PasswordInput)
    def clean(self):
        entire_data = super().clean()
        n = entire_data['name']
        if(len(n)>10):
            raise forms.ValidationError("Number of Characters Must be less than 10")
        r = entire_data["roll"]
        if(r<0):
            raise forms.ValidationError("Negative roll number is invalid")
        p = entire_data['password']
        rp = entire_data['repassword']
        if(p!= rp):
            raise forms.ValidationError("Miss match in password")
