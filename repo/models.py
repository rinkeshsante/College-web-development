from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
# from safedelete.models import SafeDeleteModel


class Department(models.Model):
    Name = models.CharField(max_length=40, unique=True)
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
    Header = models.CharField(max_length=40)
    Info = models.TextField()
    Date = models.DateField(auto_now_add=True)
    Is_Solved = models.BooleanField(default=False)
    Creator = models.ForeignKey(get_user_model(),
                                on_delete=models.SET_NULL,
                                null=True)

    def __str__(self):
        return self.Header


class Lab(models.Model):
    # code = models.CharField(max_length=5, unique=True)
    Lab_Number = models.IntegerField(default=0, unique=True)
    Name = models.CharField(max_length=20, unique=True)
    Lab_Area_In_sqft = models.IntegerField(default=0)  # in sq ft
    Lab_Capacity = models.IntegerField(default=0)
    Intercom_No = models.IntegerField(default=0,
                                      unique=True,
                                      null=True,
                                      blank=True)
    Lab_Incharge = models.ForeignKey(
        get_user_model(),
        null=True,
        on_delete=models.SET_NULL,
    )
    Department = models.ForeignKey(
        'Department',
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.Name


class Purchase(models.Model):
    # bill_no = models.CharField(max_length=10, unique=True)
    Invoice_No = models.CharField(max_length=20, unique=True)
    Supplier_Info = models.TextField()
    Date = models.DateField(auto_now_add=True)
    Rate_With_VAT = models.FloatField()
    Total_Cost_With_VAT = models.FloatField()
    GI_No = models.IntegerField(unique=True)

    Remark = models.CharField(max_length=60, default='ok')

    def __str__(self):
        return self.Invoice_No


class Equipment(models.Model):
    Name = models.CharField(max_length=100)
    Equipment_No = models.CharField(max_length=10, unique=True)
    Code = models.CharField(max_length=10, unique=True)
    # gi_no = models.IntegerField(unique=True)
    Status = models.CharField(max_length=60)

    Department = models.ForeignKey(
        'Department',
        null=True,
        on_delete=models.SET_NULL,
    )

    Location = models.ForeignKey(
        'Lab',
        null=True,
        on_delete=models.SET_NULL,
    )
    Invoice = models.ForeignKey(
        'Purchase',
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.Name


class Computer(models.Model):
    Name = models.CharField(max_length=100)
    Equipment_No = models.CharField(max_length=10, unique=True)
    Code = models.CharField(max_length=100, unique=True)
    # gi_no = models.IntegerField(unique=True)
    Status = models.CharField(max_length=60)
    RAM = models.IntegerField()
    Storage_in_GB = models.IntegerField()
    Other_Info = models.TextField(max_length=200)

    Department = models.ForeignKey(
        'Department',
        null=True,
        on_delete=models.SET_NULL,
    )

    Installed_Softwares = models.ManyToManyField("Software",
                                                 blank=True,
                                                 null=True)

    Location = models.ForeignKey(
        'Lab',
        null=True,
        on_delete=models.SET_NULL,
    )
    Invoice = models.ForeignKey(
        'Purchase',
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.Name


class Software(models.Model):
    Name = models.CharField(max_length=100)
    Licenced_Qty = models.IntegerField(null=True, blank=True)
    Software_No = models.IntegerField(unique=True)
    Code = models.CharField(max_length=10, unique=True)
    GI_No = models.IntegerField(unique=True)
    Status = models.CharField(max_length=60, default='Ok')

    Invoice = models.ForeignKey(
        'Purchase',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
    )

    def __str__(self):
        return self.Name
