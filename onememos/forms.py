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
        fields = '__all__'
        # fileds = (
        #     "content",
        #     "writer",
        #     "write_date",
        # )
        
        