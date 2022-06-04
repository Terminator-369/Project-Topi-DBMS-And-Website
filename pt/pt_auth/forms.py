from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import PtAccount, Collection, Donor
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = PtAccount
        fields = ("username", "email", "address", "team", "phone_no",'name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = PtAccount
        fields = ("username", "email", "address", "team", "phone_no", "name")

class DonorPaymentForm(ModelForm):
    class Meta:
        model = Collection
        fields = '__all__'
    # def __init__(self, *args, **kwargs):
    #     super(DonorPaymentForm, self).__init__(*args, **kwargs)
    #     Donor = kwargs.get('instance')
    #     donor_name = Donor.name
    #     self.fields['donor'].initial = donor_name  # this will show the first name in the html page when i request the instance

class CreateDonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'