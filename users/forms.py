from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, forms


class UserCreateForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email",)

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):

    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'password': forms.PasswordInput(),
    }



