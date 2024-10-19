from django import forms

class LoginForm(forms.Form):
    user_id = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control custom-login-box',
            'placeholder': 'MSSV của bạn',
            'id': 'floatingInput',
        }),
        label="Tài khoản"
    )
    user_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control custom-login-box',
            'placeholder': 'Mật khẩu của bạn',
            'id': 'floatingPassword',
        }),
        label="Mật khẩu"
    )
