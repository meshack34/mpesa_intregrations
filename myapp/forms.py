from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100)
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea, label="Message")
from django import forms

class PaymentForm(forms.Form):
    phone_number = forms.CharField(label='Phone Number', max_length=15)
    amount = forms.IntegerField(label='Amount', min_value=1, max_value=250000)