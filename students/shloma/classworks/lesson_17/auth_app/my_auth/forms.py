from django import forms
from .models import MyUser


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = "__all__"
        widgets = {"password": forms.PasswordInput()}

        # also works
        # fields = ["login", "password", "email"]
        # exclude = []

    def clean(self):
        super(self.__class__, self).clean()

        login = self.cleaned_data.get("login")
        users_logins = MyUser.objects.filter(login=login)

        if users_logins:
            # self._errors["login"] = self.error_class(["This login is already in use. Please supply a different login"])
            self.add_error("login", "This login is already in use. Please supply a different login")

        email = self.cleaned_data.get("email")
        users_email = MyUser.objects.filter(email=email)

        if users_email:
            self.add_error("email", "This email address is already in use. Please supply a different email address.")

        return self.cleaned_data


class SignInForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ["login", "password"]
        widgets = {"password": forms.PasswordInput()}

    def clean(self):
        super(self.__class__, self).clean()

        login = self.cleaned_data.get("login")

        user = MyUser.objects.filter(login=login).first()

        if not user:
            self.add_error("login", f"Unknown user '{login}'. Check your login or register at first")
            return self.cleaned_data

        password = self.cleaned_data.get("password")

        if password != user.password:
            self.add_error("password", "Wrong password!")

        return self.cleaned_data

