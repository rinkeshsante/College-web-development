from django.forms import ModelForm
from .models import Lab, Equipment, Software, Computer, Purchase


class LabForm(ModelForm):
    class Meta:
        model = Lab
        fields = '__all__'


class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'


class SoftwareForm(ModelForm):
    class Meta:
        model = Software
        fields = '__all__'


class ComputerForm(ModelForm):
    class Meta:
        model = Computer
        fields = '__all__'


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
