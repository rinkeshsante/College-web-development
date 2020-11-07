from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from safedelete.models import SafeDeleteModel


class Department(SafeDeleteModel):
    name = models.CharField(max_length=40, unique=True)
    Dep_admin = models.ForeignKey(
        get_user_model(),
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
    )

    def __str__(self):
        return self.name


class UserDepartmentMapping(SafeDeleteModel):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        unique=True
    )
    is_sub_admin = models.BooleanField(default=False)
    department = models.ForeignKey(
        'Department',
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return str(self.user) + str(self.department)


class Issue(SafeDeleteModel):
    header = models.CharField(max_length=40)
    info = models.TextField()
    date = models.DateField(auto_now_add=True)
    is_solved = models.BooleanField(default=False)
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.header


class Lab(SafeDeleteModel):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=20, unique=True)
    lab_number = models.IntegerField(default=0, unique=True)
    lab_area_in_sqft = models.IntegerField(default=0)  # in sq ft
    lab_capacity = models.IntegerField(default=0)
    intercom_no = models.IntegerField(
        default=0, unique=True, null=True, blank=True)
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


class Purchase(SafeDeleteModel):
    bill_no = models.CharField(max_length=10, unique=True)
    supplier_info = models.TextField()
    invoice_no = models.CharField(max_length=20, unique=True)
    date = models.DateField(auto_now_add=True)
    rate_in_Rupee = models.FloatField()

    def __str__(self):
        return self.bill_no


class Equipment(SafeDeleteModel):
    name = models.CharField(max_length=100)
    equipment_no = models.CharField(max_length=10, unique=True)
    code = models.CharField(max_length=10, unique=True)
    gi_no = models.IntegerField(unique=True)
    Status = models.CharField(max_length=60)

    department = models.ForeignKey(
        'Department',
        null=True,
        on_delete=models.SET_NULL,
    )
    lab = models.ForeignKey(
        'Lab',
        null=True,
        on_delete=models.SET_NULL,
    )
    purchase = models.ForeignKey(
        'Purchase',
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name


class Computer(SafeDeleteModel):
    name = models.CharField(max_length=100)
    Computer_no = models.CharField(max_length=10, unique=True)
    code = models.CharField(max_length=100, unique=True)
    gi_no = models.IntegerField(unique=True)
    Status = models.CharField(max_length=60)
    ram = models.IntegerField()
    storage = models.IntegerField()
    processor = models.CharField(max_length=50)

    installed_software = models.ManyToManyField(
        "Software",
        blank=True,
        null=True,
    )
    lab = models.ForeignKey(
        'Lab',
        null=True,
        on_delete=models.SET_NULL,
    )
    purchase_bill_no = models.ForeignKey(
        'Purchase',
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name


class Software(SafeDeleteModel):
    name = models.CharField(max_length=100)
    Licenced_Qty = models.IntegerField(null=True, blank=True)
    software_no = models.IntegerField(unique=True)
    code = models.CharField(max_length=10, unique=True)
    gi_no = models.IntegerField(unique=True)
    Status = models.CharField(max_length=60, default='Ok')

    purchase = models.ForeignKey(
        'Purchase',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
    )

    def __str__(self):
        return self.name
