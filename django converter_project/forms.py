#-*- coding: utf-8 -*-

from django import forms


SCHEME_CHOICES =( 
    ("1", "To English"), 
    ("2", "To Hindi"), 
    ("3", "To Marathi"), 
)
class InputForm(forms.Form):
    Enter_Number = forms.DecimalField(label="Enter Number", max_digits=13, required=False)
    choices = forms.TypedChoiceField(label="Select Scheme of your choice", choices = SCHEME_CHOICES,required=False)
    
    

    



    