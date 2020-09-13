from django import forms


class MyLoginForm(forms.Form):

    username = forms.CharField(label="用户名", min_length=5,
    		widget=forms.TextInput(attrs={'class': 'form-control'}))

    password = forms.CharField(label="密码", min_length=8,
                widget=forms.TextInput(attrs={'class': 'form-control', 'type': "password"}))
