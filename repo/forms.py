from  django.forms import  ModelForm
from .models import Lab,Equipment,Software,ComputerSoftwareMapping,LabFacultyMapping

class LabForm(ModelForm):
    class Meta:
        model = Lab
        fields ='__all__'

class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields ='__all__'

class SoftwareForm(ModelForm):
    class Meta:
        model = Software
        fields ='__all__'


class ComputerSoftwareMappingForm(ModelForm):
    class Meta:
        model = Software
        fields ='__all__'