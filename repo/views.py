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
    return render(request, 'not_allowed.html')


def notFound(request):
    return render(request, 'not_found.html')


# -------------labs-------------------------------
lab_attr = ['id', 'code', 'name', 'lab_number',
            'lab_area', 'lab_capacity', 'intercom_no',
            'lab_incharge', 'department']


@login_required
# @user_passes_test(is_sub_admin, login_url='error')
def LabDetailView(request, num=1):
    test_lab = Lab.objects.get(id=num)
    eqps = Equipment.objects.filter(lab=test_lab.id)
    context = {'lab': test_lab, 'equipments': eqps, 'attr_names': lab_attr}
    return render(request, 'repo/lab_detail.html', context)


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

epq_attr = ['id',  'name', 'equipment_no',
            'code', 'gi_no', 'Status',
            'lab', 'department', 'purchase']


@login_required
def EquipmentDetailView(request, num=1):
    test_epq = Equipment.objects.get(id=num)
    # eqps = Equipment.objects.filter(lab=test_lab.id)

    context = {'epq': test_epq, 'attr_names': epq_attr}
    return render(request, 'repo/epq_detail.html', context)


def EquipmentListView(request):
    return DataListView(request, Equipment, epq_attr,
                        table_name='Equipment Table', csv_url='epq_csv',
                        create_url='epq_create', detail_url='epq_detail')


def getEquipmentCSV(request):
    return getfile(request, Equipment.objects.all(), epq_attr, filename='Equipment.csv')


def EquipmentCreateView(request):
    return DataCreateView(request, EquipmentForm, 'epq_table')


def EquipmentUpdateView(request, num):
    return DataUpdateView(request, num, Equipment, EquipmentForm, 'epq_detail')


def EquipmentDeleteView(request, num):
    return DataDeleteView(request, num, Equipment, 'epq_table')

# ---------------Computer--------------------


comp_attr = ['id',  'name', 'Computer_no',
             'code', 'gi_no', 'Status', 'ram', 'storage',
             'processor', 'lab', 'purchase']


@login_required
def ComputerDetailView(request, num=1):
    test_comp = Computer.objects.get(id=num)
    # eqps = Equipment.objects.filter(lab=test_lab.id)

    context = {'comp': test_comp, 'attr_names': comp_attr}
    return render(request, 'repo/comp_detail.html', context)


def ComputerListView(request):
    return DataListView(request, Computer, comp_attr,
                        table_name='Computer Table', csv_url='comp_csv',
                        create_url='comp_create', detail_url='comp_detail')


def getComputerCSV(request):
    return getfile(request, Computer.objects.all(), comp_attr, filename='Computer.csv')


def ComputerCreateView(request):
    return DataCreateView(request, ComputerForm, 'comp_table')


def ComputerUpdateView(request, num):
    return DataUpdateView(request, num, Computer, ComputerForm, 'comp_detail')


def ComputerDeleteView(request, num):
    return DataDeleteView(request, num, Computer, 'comp_table')

# --------------------------Software--------------


soft_attr = ['id', 'name', 'software_no', 'code',
             'gi_no', 'Status', 'purchase', ]


def SoftwareListView(request):
    return DataListView(request, Software, soft_attr,
                        table_name='Software Table', csv_url='soft_csv',
                        create_url='soft_create', detail_url='soft_detail')


def getSoftwareCSV(request):
    return getfile(request, Software.objects.all(), soft_attr, filename='Software.csv')


@login_required
def SoftwareDetailView(request, num=1):
    test_soft = Software.objects.get(id=num)
    context = {'soft': test_soft, 'attr_names': soft_attr}
    return render(request, 'repo/soft_detail.html', context)


def SoftwareCreateView(request):
    return DataCreateView(request, SoftwareForm, 'soft_table')


def SoftwareUpdateView(request, num):
    return DataUpdateView(request, num, Software, SoftwareForm, 'soft_detail')


def SoftwareDeleteView(request, num):
    return DataDeleteView(request, num, Software, 'soft_table')


# --------------------------purchase--------------


purch_attr = ['id', 'bill_no', 'supplier', 'invoice',
              'date', 'rate', ]


def PurchaseListView(request):
    return DataListView(request, Purchase, purch_attr,
                        table_name='Purchase Table', csv_url='purch_csv',
                        create_url='purch_create', detail_url='purch_detail')


def getPurchaseCSV(request):
    return getfile(request, Purchase.objects.all(), purch_attr, filename='Purchase.csv')


@login_required
def PurchaseDetailView(request, num=1):
    test_purch = Purchase.objects.get(id=num)
    context = {'purch': test_purch, 'attr_names': purch_attr}
    return render(request, 'repo/purch_detail.html', context)


def PurchaseCreateView(request):
    return DataCreateView(request, PurchaseForm, 'purch_table')


def PurchaseUpdateView(request, num):
    return DataUpdateView(request, num, Purchase, PurchaseForm, 'purch_detail')


def PurchaseDeleteView(request, num):
    return DataDeleteView(request, num, Purchase, 'soft_table')
