from django import forms
from django.contrib.auth.forms import UserCreationForm
from onememos.models import Users, OneMemo


class RegisterForm(UserCreationForm):
    # username = forms.CharField(max_length=30, required=False, help_text="Optional.")
    # email = forms.EmailField(max_length=254, help_text="Required. Inform a valid email address.")
    class Meta:
        model = Users
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

class MemoForm(forms.ModelForm):
    class Meta:
        model = OneMemo
        exclude = ['writer',]

    def save(self, request, commit=True):
        instance = super(MemoForm, self).save(commit=False)
        instance.writer = request.user.username
        if commit:
            instance.save()
        return instance
    
    def update_form(self, request, memo_id):
        instance = super(MemoForm, self).save(commit=False) 
        OneMemo.objects.filter(pk=memo_id).update(content=instance.content)