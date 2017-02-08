# ticket/forms.py

from django import forms

from .validators import has_duplicates


class TicketForm(forms.Form):
    first_name = forms.CharField(label='First Name', required=True,
                                 min_length=1, max_length=128)
    last_name = forms.CharField(label='Last Name', required=True,
                                min_length=1, max_length=128)
    white1 = forms.IntegerField(label='1st Number', required=True,
                                min_value=1, max_value=69)
    white2 = forms.IntegerField(label='2nd Number', required=True,
                                min_value=1, max_value=69)
    white3 = forms.IntegerField(label='3rd Number', required=True,
                                min_value=1, max_value=69)
    white4 = forms.IntegerField(label='4th Number', required=True,
                                min_value=1, max_value=69)
    white5 = forms.IntegerField(label='5th Number', required=True,
                                min_value=1, max_value=69)
    red1 = forms.IntegerField(label='Power Ball', required=True,
                              min_value=1, max_value=26)

    def clean(self):
        cleaned_data = super(TicketForm, self).clean()
        white_balls = [cleaned_data.get('white1'),
                       cleaned_data.get('white2'),
                       cleaned_data.get('white3'),
                       cleaned_data.get('white4'),
                       cleaned_data.get('white5')]
        if has_duplicates(white_balls):
            raise forms.ValidationError(
                "White ball values must be unique! Please remove duplicates.")
