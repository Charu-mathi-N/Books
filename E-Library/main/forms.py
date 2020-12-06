from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


BOOK_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 15)]

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class CartAddBookForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=BOOK_QUANTITY_CHOICES,
                                coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

