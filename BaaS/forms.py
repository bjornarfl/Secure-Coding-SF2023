from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, PaymentInfo, Subscription

#extends the default user creation form to use email instead of username
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser        
        fields = ('email', 'first_name', 'last_name')

class PaymentInfoCreationForm(forms.ModelForm):
    class Meta:
        model = PaymentInfo
        fields = ('title', 'card_number', 'expiration_year', 'expiration_month', 'cvv')

class SubscriptionUpdateForm(forms.ModelForm):
    start_time = forms.DateField(required=False)
    class Meta:
        model = Subscription
        fields = ('subscriptiontype', 'auto_renewal', 'start_time', 'payment')
