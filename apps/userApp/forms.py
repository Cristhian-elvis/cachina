from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegister(UserCreationForm):
    #telefono = forms.IntegerField(label='telefono')

    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password1',
                  'password2'
                  ]
        #help_texts = {k:"" for k in fields}
