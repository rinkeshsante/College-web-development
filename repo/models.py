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


class Lab(SafeDeleteModel):
    code = models.CharField(max_length=10, unique=True)
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


class Purchase(SafeDeleteModel):
    bill_no = models.CharField(max_length=10)
    supplier = models.TextField()
    invoice = models.CharField(max_length=20, unique=True)
    date = models.DateField(auto_now_add=True)
    rate = models.FloatField()

    def __str__(self):
        return self.bill_no


class Equipment(SafeDeleteModel):
    name = models.CharField(max_length=100)
    equipment_no = models.CharField(max_length=10, unique=True)
    code = models.CharField(max_length=100)
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
    code = models.CharField(max_length=100)
    gi_no = models.IntegerField(unique=True)
    Status = models.CharField(max_length=60)
    ram = models.IntegerField()
    storage = models.IntegerField()
    processor = models.CharField(max_length=50)

    installed_software = models.ManyToManyField(
        "Software")

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


class Software(SafeDeleteModel):
    name = models.CharField(max_length=100)
    Licenced_Qty = models.IntegerField(null=True)
    software_no = models.CharField(max_length=10, unique=True)
    code = models.CharField(max_length=30)
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
