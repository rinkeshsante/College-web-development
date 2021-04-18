from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
# from safedelete.models import SafeDeleteModel
from datetime import date


class Department(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    Dep_admin = models.OneToOneField(
        get_user_model(),
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
    )

    def __str__(self):
        return self.Name


class UserDepartmentMapping(models.Model):
    User = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    Is_Sub_Admin = models.BooleanField(default=False)
    Department = models.ForeignKey(
        'Department',
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return str(self.User) + str(self.Department)


class Issue(models.Model):
    Header = models.CharField(max_length=100)
    Info = models.TextField()
    Date_YYYYMMDD = models.DateField(auto_now_add=True)
    Is_Solved = models.BooleanField(default=False)
    Creator = models.ForeignKey(get_user_model(),
                                on_delete=models.SET_NULL,
                                null=True)

    def __str__(self):
        return self.Header


class Room(models.Model):
    Room_no = models.CharField(max_length=10)
    Name = models.CharField(max_length=100)
    Area_In_sq_m = models.IntegerField(default=0)  # in sq ft
    Seating_Capacity = models.IntegerField(default=0)
    Total_cost = models.FloatField(default=0)
    Other_Data = models.TextField(null=True, blank=True)
    Department = models.ForeignKey(
        'Department',
        null=True,
        on_delete=models.SET_NULL,
    )

    No_of_Fans = models.IntegerField(default=0)
    No_of_AC = models.IntegerField(default=0)
    No_of_Light_Sounce = models.IntegerField(default=0)

    def __str__(self):
        return self.Name


class ClassRoom(Room):
    Teaching_Tools = models.TextField()
    is_stepped_Room = models.BooleanField(default=False)
    No_of_benches = models.IntegerField(default=0)


class Cabin(Room):
    Details = models.TextField(null=True, blank=True)
    No_of_Tables = models.IntegerField(default=0)
    Intercom_No = models.IntegerField(default=0,
                                      null=True,
                                      blank=True)


class Laboratory(Room):
    Extension_No = models.IntegerField(default=0, null=True, blank=True)
    Intercom_No = models.IntegerField(default=0,
                                      null=True,
                                      blank=True)
    Practicals_conducted_Odd_SEM = models.CharField(
        max_length=300, default='None')
    Practicals_conducted_Even_SEM = models.CharField(
        max_length=300, default='None')

    Lab_Incharge = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='lab_incharge'
    )

    Lab_Assistant_1 = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='lab_assistant_1'
    )

    Lab_Assistant_2 = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='lab_assistant_2'
    )


class Purchase(models.Model):
    # bill_no = models.CharField(max_length=10, unique=True)
    Invoice_No = models.CharField(max_length=100, unique=True)
    Supplier_Info = models.TextField()
    Date_YYYYMMDD = models.DateField(default=date.today, null=True, blank=True)
    Rate_With_VAT = models.FloatField()
    Total_Cost_With_VAT = models.FloatField()
    GI_No = models.IntegerField(null=True, blank=True)

    Remark = models.CharField(max_length=100, default='ok')

    def __str__(self):
        return self.Invoice_No


class Item(models.Model):
    Name = models.TextField()
    Equipment_No = models.CharField(max_length=100, unique=True)
    Code = models.CharField(max_length=100, unique=True)
    Status = models.CharField(max_length=100)

    Department = models.ForeignKey(
        'Department',
        null=True,
        on_delete=models.SET_NULL,
    )

    Location = models.ForeignKey(
        'Laboratory',
        null=True,
        on_delete=models.SET_NULL,
    )

    Invoice = models.ForeignKey(
        'Purchase',
        null=True,
        on_delete=models.SET_NULL,
    )

    Other_Info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Name


class Equipment(Item):
    pass

    def __str__(self):
        return self.Name


class Computer(Item):
    RAM = models.IntegerField()
    Storage_in_GB = models.IntegerField()
    Processor = models.CharField(max_length=100)

    Installed_Softwares = models.ManyToManyField("Software", blank=True)

    def __str__(self):
        return self.Name


class Software(models.Model):
    Name = models.TextField()
    Licenced_Qty = models.IntegerField(null=True, blank=True)
    Software_No = models.IntegerField(unique=True)
    Code = models.CharField(max_length=100, unique=True)
    GI_No = models.IntegerField(unique=True)
    Status = models.CharField(max_length=100, default='Ok')

    Invoice = models.ForeignKey(
        'Purchase',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
    )

    def __str__(self):
        return self.Name
