from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms

from date_time_picker_sample.models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['name', 'timestamp']
        widgets = {
            'timestamp': DateTimePickerInput(
                options={
                    # https://getdatepicker.com/4/Options/#format
                    'format': 'MM/DD/YYYY HH:mm',
                    # https://getdatepicker.com/4/Options/#stepping
                    'stepping': 10,
                    'showClose': True,
                    'showClear': True
                }
            )
        }


class ItemModalForm(BSModalModelForm):

    class Meta:
        model = Item
        fields = ['name', 'timestamp']
        widgets = {
            'timestamp': DateTimePickerInput(
                options={
                    # https://getdatepicker.com/4/Options/#format
                    'format': 'DD.MM.YYYY HH:mm',
                    # https://getdatepicker.com/4/Options/#stepping
                    'stepping': 10,
                    'showClose': True,
                    'showClear': True
                }
            )
        }