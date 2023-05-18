from django import forms
from .models import AdrCheck

TRUCK_ART = [
    ("P", "Planne"),
    ("K", "Aufbau ohne Kühler"),
    ("KK", "Aufbau mit Kühler"),
]

TRUCK_TYPE = [
    ("SZ", "Sattelzug"),
    ("MW", "Motorwagen")
]

FIELD_1 = [
    ("1", "1"),
    ("2", "2"),
]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)


class AdrCheckForm(forms.ModelForm):
    required_css_class = 'required-field'
    # adr_card = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))

    class Meta:
        model = AdrCheck
        fields = ['first_name', 'second_name', 'truck_plate1', 'truck_plate2', 'adr_card', 'truck_origin',
                  'type', 'truck_art', 'check_1', 'check_2', 'check_3', 'check_4', 'check_5', 'check_6', 'check_7',
                  'check_8', 'check_9', 'check_10', 'check_11', 'check_12', 'check_13', 'check_14', 'check_15',
                  'check_16', 'check_17', 'check_18', 'check_19', 'check_20', 'check_21', 'check_22', 'check_23',
                  'check_24', 'check_25', 'check_26', 'check_27', 'check_28', 'check_29', 'check_30', 'check_31',
                  'check_32', 'check_33', 'check_34', 'check_35', 'check_36', 'check_37', 'check_38', 'check_39',
                  'complete', 'field1', 'field2', 'signature', 'field3', 'check_40', 'check_41', 'check_42']
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'second_name': forms.TextInput(attrs={"class": "form-control"}),
            'truck_plate1': forms.TextInput(attrs={"class": "form-control"}),
            'truck_plate2': forms.TextInput(attrs={"class": "form-control"}),
            'adr_card': forms.TextInput(attrs={"class": "form-control"}),
            'truck_origin': forms.Select(attrs={'class': 'form-control'}),
            'field1': forms.Select(attrs={"class": "form-control"}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'truck_art': forms.Select(attrs={'class': 'form-control'}),
        }
