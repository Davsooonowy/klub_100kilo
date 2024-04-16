from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, MinLengthValidator, RegexValidator


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, validators=[MinLengthValidator(1)])
    last_name = forms.CharField(max_length=30, validators=[MinLengthValidator(1)])
    phone_number = forms.CharField(max_length=15, validators=[
        RegexValidator(r'^\d{9}$', message="Numer telefonu musi mieć dokładnie 9 cyfr.")
    ])
    email = forms.EmailField(max_length=254, validators=[EmailValidator()])
    password = forms.CharField(widget=forms.PasswordInput, validators=[
        MinLengthValidator(8),
        RegexValidator(r'[A-Za-z0-9@#$%^&+=]',
                       message="Hasło musi zawierać co najmniej jedną literę, jedną cyfrę i jeden znak specjalny.")
    ])

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(validators=[EmailValidator()])
    password = forms.CharField(widget=forms.PasswordInput)