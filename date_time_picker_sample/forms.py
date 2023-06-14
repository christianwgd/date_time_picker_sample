from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import forms

from date_time_picker_sample.models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['name', 'timestamp']
        widgets = {
            'timestamp': DateTimePickerInput()
        }