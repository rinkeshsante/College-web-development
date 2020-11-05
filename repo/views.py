from django import template
from django.shortcuts import render, redirect, HttpResponse
from .models import Lab, Equipment, Software, Computer, Purchase
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import LabForm, EquipmentForm, SoftwareForm, ComputerForm, PurchaseForm

from .services import getfile, is_sub_admin, is_teacher, DataCreateView, DataUpdateView, DataDeleteView, DataListView


# ----------------dashboard ------------------------


@login_required
def DashBoardView(request):

    total_lab = Lab.objects.count()
    total_epq = Equipment.objects.count()
    total_soft = Software.objects.count()

    context = {
        'total_lab': total_lab,
        'total_epq': total_epq,
        'total_soft': total_soft,
        'unauth_user': 0
    }
    return render(request, 'repo/dashboard.html', context)

# ----------------- unauthorized----------------------


def Unauthorized(request):
    return HttpResponse('<h1>sorry not allowed for you</h1>')

# -------------labs-------------------------------


@login_required
# @user_passes_test(is_sub_admin, login_url='error')
def LabDetailView(request, num=1):
    test_lab = Lab.objects.get(id=num)
    eqps = Equipment.objects.filter(lab=test_lab.id)
    context = {'lab': test_lab, 'equipments': eqps}
    return render(request, 'repo/lab/lab_detail.html', context)


lab_attr = ['id', 'code', 'name', 'lab_number',
            'lab_area', 'lab_capacity', 'intercom_no',
            'lab_incharge', 'department']


def LabListView(request):
    return DataListView(request, Lab, lab_attr,
                        table_name='Lab Table', csv_url='lab_csv',
                        create_url='lab_create', detail_url='lab_detail')


def getLabCSV(request):
    return getfile(request, Lab.objects.all(), lab_attr, filename='labs.csv')


def LabCreateView(request):
    return DataCreateView(request, LabForm, 'lab_table')


def LabUpdateView(request, num):
    return DataUpdateView(request, num, Lab, LabForm, 'lab_detail')


def LabDeleteView(request, num):
    return DataDeleteView(request, num, Lab, 'lab_table')


# -------------epq------------------------


@login_required
def EquipmentDetailView(request, num=1):
    test_epq = Equipment.objects.get(id=num)
    # eqps = Equipment.objects.filter(lab=test_lab.id)

    context = {'epq': test_epq}
    return render(request, 'repo/epq/epq_detail.html', context)


@login_required
def EquipmentListView(request, num=1):
    epq_list = Equipment.objects.order_by('-id')
    context = {'epq_list': epq_list}
    return render(request, 'repo/epq/epq_table.html', context)


def EquipmentCreateView(request):
    return DataCreateView(request, EquipmentForm, 'epq_table')


def EquipmentUpdateView(request, num):
    return DataUpdateView(request, num, Equipment, EquipmentForm, 'epq_detail')


def EquipmentDeleteView(request, num):
    return DataDeleteView(request, num, Equipment, 'epq_table')

# --------------------------Software--------------


@login_required
def SoftListView(request, num=1):
    soft_list = Software.objects.order_by('-id')
    context = {'soft_list': soft_list}
    return render(request, 'repo/soft/soft_table.html', context)


@login_required
def SoftDetailView(request, num=1):
    test_soft = Software.objects.get(id=num)
    context = {'soft': test_soft}
    return render(request, 'repo/soft/soft_detail.html', context)


def SoftwareCreateView(request):
    return DataCreateView(request, SoftwareForm, 'soft_table')


def SoftwareUpdateView(request, num):
    return DataUpdateView(request, num, Software, SoftwareForm, 'soft_detail')


def SoftwareDeleteView(request, num):
    return DataDeleteView(request, num, Software, 'soft_table')
