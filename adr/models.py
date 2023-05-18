from django.db import models
from django.contrib.auth.models import User
from jsignature.fields import JSignatureField


# Create your models here.

class AdrCheck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.BigAutoField(primary_key=True, blank=True)
    first_name = models.CharField(max_length=25)
    second_name = models.CharField(max_length=25)
    adr_card = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)
    truck_plate1 = models.CharField(max_length=25)
    truck_plate2 = models.CharField(max_length=25)
    ORIGIN = [
        ("Österreich", "A-Österreich"),
        ("Kroatien", "HR-Kroatien"),
        ("Slowakei", "SK-Slowakei"),
        ("Deutschland", "D-Deutschland"),
        ("Rumänien", "RO-Rumänien"),
        ("Polen", "PL-Polen"),
        ("Bulgarien", "BG-Bulgarien"),
        ("Tschechien", "CZ-Tschechien"),
        ("Ungarn", "H-Ungarn"),
        ("Griechenland", "EL/GR-Griechenland"),
        ("Italen", "I-Italen"),
        ("Dänemark", "DK-Dänemark"),
        ("Estland", "EST-Estland"),
        ("Finnland", "Finnland"),
        ("Frankreich", "F-Frankreich"),
        ("Irland", "IRL-Irland"),
        ("Lettland", "LV-Lettland"),
        ("Litauen", "LT-Litauen"),
        ("Luxemburg", "L-Luxemburg"),
        ("Malta", "M-Malta"),
        ("Niederlande", "NL-Niederlande"),
        ("Portugal", "P-Portugal"),
        ("Schweden", "S-Schweden"),
        ("Spanien", "E-Spanien"),
        ("Zypern", "CY-Zypern"),
    ]

    truck_origin = models.CharField(max_length=20, choices=ORIGIN, blank=True)
    TRUCK_TYPE = [
        ("Sattelzug", "Sattelzug"),
        ("Motorwagen", "Motorwagen")
    ]
    type = models.CharField(max_length=20, choices=TRUCK_TYPE,blank=True)
    TRUCK_ART = [
        ("Planne", "Planne"),
        ("Aufbau ohne Kühler", "Aufbau ohne Kühler"),
        ("Aufbau mit Kühler", "Aufbau mit Kühler"),
    ]
    FIELD_1 = [
        ("1", "1"),
        ("2", "2"),
    ]
    truck_art = models.CharField(max_length=18, choices=TRUCK_ART, blank=True)
    field1 = models.CharField(default="1", choices=FIELD_1, max_length=1, blank=True,null=True)
    field2 = models.CharField(max_length=25, null=True, blank=True)
    field3 = models.CharField(max_length=25, null=True, blank=True)
    check_1 = models.BooleanField(default=False)
    check_2 = models.BooleanField(default=False)
    check_3 = models.BooleanField(default=False)
    check_4 = models.BooleanField(default=False)
    check_5 = models.BooleanField(default=False)
    check_6 = models.BooleanField(default=False)
    check_7 = models.BooleanField(default=False)
    check_8 = models.BooleanField(default=False)
    check_9 = models.BooleanField(default=False)
    check_10 = models.BooleanField(default=False)
    check_11 = models.BooleanField(default=False)
    check_12 = models.BooleanField(default=False)
    check_13 = models.BooleanField(default=False)
    check_14 = models.BooleanField(default=False)
    check_15 = models.BooleanField(default=False)
    check_16 = models.BooleanField(default=False)
    check_17 = models.BooleanField(default=False)
    check_18 = models.BooleanField(default=False)
    check_19 = models.BooleanField(default=False)
    check_20 = models.BooleanField(default=False)
    check_21 = models.BooleanField(default=False)
    check_22 = models.BooleanField(default=False)
    check_23 = models.BooleanField(default=False)
    check_24 = models.BooleanField(default=False)
    check_25 = models.BooleanField(default=False)
    check_26 = models.BooleanField(default=False)
    check_27 = models.BooleanField(default=False)
    check_28 = models.BooleanField(default=False)
    check_29 = models.BooleanField(default=False)
    check_30 = models.BooleanField(default=False)
    check_31 = models.BooleanField(default=False)
    check_32 = models.BooleanField(default=False)
    check_33 = models.BooleanField(default=False)
    check_34 = models.BooleanField(default=False)
    check_35 = models.BooleanField(default=False)
    check_36 = models.BooleanField(default=False)
    check_37 = models.BooleanField(default=False)
    check_38 = models.BooleanField(default=False)
    check_39 = models.BooleanField(default=False)
    check_40 = models.BooleanField(default=False)
    check_41 = models.BooleanField(default=False)
    check_42 = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    signature = JSignatureField(null=True, blank=True)

    def __str__(self):
        return self.truck_plate1

    class Meta:
        ordering = ['complete']


# class SignatureModel(JSignatureFieldsMixin):
    # signature = JSignatureField(null=True, blank=True)
    # check_id = models.OneToOneField(AdrCheck, on_delete=models.CASCADE, null=True, blank=True, primary_key=False)
