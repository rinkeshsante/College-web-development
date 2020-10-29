
from django.db import models
from django.contrib.auth import get_user_model
from safedelete.models import SafeDeleteModel



class Department(SafeDeleteModel):
    name = models.CharField(max_length=40,unique =True)

    def __str__(self):
    	return self.name


class Lab(SafeDeleteModel):
    code = models.CharField(max_length=10 ,unique =True)
    name = models.CharField(max_length=50)
    lab_number = models.IntegerField(default=0)
    lab_area = models.IntegerField(default=0)  # in sq ft
    lab_capacity = models.IntegerField(default=0)
    intercom_no = models.IntegerField(default=0)
    lab_incharge = models.ForeignKey(
        get_user_model(), 
        null=True,
        on_delete=models.SET_NULL,
        )
    department = models.ForeignKey(
        'Department',
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.code
    
    class Meta:
        permissions =[
            ('sub_admin','sub_admin_status'),
            ('teacher','teacher'),
        ]


    


class Equipment(SafeDeleteModel):
    name = models.CharField(max_length=100)
    # Qty = models.IntegerField()
    equipment_no = models.CharField(max_length=10,unique =True)
    code = models.CharField(max_length=100)
    bill_no = models.CharField(max_length=10)
    supplier = models.TextField()
    invoice = models.CharField(max_length=20,unique =True)
    date = models.DateField(auto_now_add=True)
    gi_no = models.IntegerField(unique =True)
    rate = models.FloatField()
    department = models.ForeignKey(
        'Department',
        null=True,
        on_delete=models.SET_NULL,
    )
    Status = models.CharField(max_length=60)
    lab = models.ForeignKey(
        'Lab',
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name


    class Meta:
        permissions =[
            ('sub_admin','sub_admin_status'),
            ('teacher','teacher'),
        ]


# class LabEquipmentMapping(models.Model):
#     lab = models.ForeignKey(
#         'Lab',
#         on_delete=models.CASCADE,
#         related_name='equipnments',
#     )
#     equipment = models.ForeignKey(
#         'Equipment',
#         on_delete=models.CASCADE,
#         unique =True,
#     )
#
#     def __str__(self):
#         return str(self.lab)+'  '+ str(self.equipment)


class Software(SafeDeleteModel):
    name = models.CharField(max_length=100)
    Licenced_Qty = models.IntegerField(null=True)
    software_no = models.CharField(max_length=10,unique =True)
    code = models.CharField(max_length=30)
    bill_no = models.CharField(max_length=10)
    supplier_or_site = models.TextField()
    invoice = models.CharField(max_length=20,unique =True)
    date = models.DateField(auto_now_add=True)
    gi_no = models.IntegerField(unique =True)
    rate = models.FloatField()
    department = models.ForeignKey(
        'Department',
        null=True,
        on_delete=models.SET_NULL,
    )
    Status = models.CharField(max_length=60,default='Ok')

    def __str__(self):
        return self.name



class ComputerSoftwareMapping(SafeDeleteModel):
    equipment = models.ForeignKey(
        'Equipment',
        null=True,
        on_delete=models.SET_NULL,
    )
    software = models.ForeignKey(
        'Software',
        null=True,
        on_delete=models.SET_NULL,
    )
    def __str__(self):
        return str(self.equipment)+'  '+ str(self.software)


class LabFacultyMapping(SafeDeleteModel):
    lab = models.ForeignKey(
        'Lab',
        null=True,
        on_delete=models.SET_NULL,
    )
    faculty = models.ForeignKey(
        get_user_model(), 
        null=True,
        on_delete=models.SET_NULL,
    )
    subject = models.CharField(max_length=50)
    batch = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    semester = models.IntegerField()
    total_load = models.CharField(max_length=10)
    subject_department = models.ForeignKey(
        'Department',
        null=True,
        on_delete=models.SET_NULL,
        related_name='subject_department'
    )
    faculty_department = models.ForeignKey(
        'Department',
        null=True,
        on_delete=models.SET_NULL,
        related_name='faculty_department'

    )

    def __str__(self):
        return str(self.lab)+'  '+ str(self.subject)
