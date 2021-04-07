from django.shortcuts import render

# Create your views here.
from django import template
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import *

from .services import *
from django.contrib.auth import get_user_model

# ----------------dashboard ------------------------


@login_required
def DashBoardView(request):

    total_lab = Lab.objects.count()
    total_epq = Equipment.objects.count()
    total_soft = Software.objects.count()
    total_comp = Computer.objects.count()
    total_purch = Purchase.objects.count()

    issues = Issue.objects.filter(is_solved=False)

    context = {
        'total_lab': total_lab,
        'total_epq': total_epq,
        'total_soft': total_soft,
        'total_comp': total_comp,
        'total_purch': total_purch,
        'issues': issues
    }
    return render(request, 'repo/dashboard.html', context)


def AboutView(request):
    return render(request, 'about.html')


# ----------------- unauthorized----------------------


def Unauthorized(request):
    return render(request, 'not_allowed.html')


def notFound(request):
    return render(request, 'not_found.html')


# ------------------ attr -----------------------

lab_attr = [
    'id', 'code', 'name', 'lab_number', 'lab_area_in_sqft', 'lab_capacity',
    'intercom_no', 'lab_incharge', 'department'
]

lab_attr_csv = [
    'name', 'lab_area_in_sqft', 'lab_capacity', 'intercom_no', 'lab_incharge',
    'department'
]

epq_attr = [
    'id', 'name', 'equipment_no', 'code', 'gi_no', 'Status', 'lab',
    'department', 'purchase'
]

epq_attr_csv = [
    'name',
    'gi_no',
    'Status',
    'lab',
    'department',
]

comp_attr = [
    'id', 'name', 'Computer_no', 'code', 'gi_no', 'Status', 'ram', 'storage',
    'processor', 'lab', 'purchase_bill_no'
]

comp_attr_csv = [
    'name', 'gi_no', 'Status', 'ram', 'storage', 'processor', 'lab'
]

soft_attr = [
    'id',
    'name',
    'Licenced_Qty',
    'software_no',
    'code',
    'gi_no',
    'Status',
    'purchase',
]

soft_attr_csv = [
    'name',
    'Licenced_Qty',
    'gi_no',
    'Status',
]

purch_attr = [
    'id',
    'bill_no',
    'supplier_info',
    'invoice_no',
    'date',
    'rate_in_Rupee',
]

# -------------labs-------------------------------


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
def LabDetailView(request, num=1):
    test_lab = Lab.objects.get(id=num)
    eqps = Equipment.objects.filter(lab=test_lab.id)
    comps = Computer.objects.filter(lab=test_lab.id)
    context = {
        'lab': test_lab,
        'equipments': eqps,
        'computers': comps,
        'attr_names': lab_attr
    }
    return render(request, 'repo/lab_detail.html', context)


def LabListView(request):
    return DataListView(request,
                        Lab,
                        lab_attr,
                        table_name='Lab Table',
                        csv_url='lab_csv',
                        create_url='lab_create',
                        detail_url='lab_detail')


def getLabCSV(request):
    return getfile(request,
                   Lab.objects.all(),
                   lab_attr_csv,
                   filename='labs.csv')


def getLabReport(request, num=1):
    test_lab = Lab.objects.get(id=num)
    epq_in_lab = Equipment.objects.filter(lab=num)
    comp_in_lab = Computer.objects.filter(lab=num)
    return getlabRep(request, test_lab, lab_attr, epq_in_lab, epq_attr_csv,
                     comp_in_lab, comp_attr_csv)


def LabCreateView(request):
    return DataCreateView(request, LabForm, 'lab_table')


def LabUpdateView(request, num):
    return DataUpdateView(request, num, Lab, LabForm, 'lab_detail')


def LabDeleteView(request, num):
    return DataDeleteView(request, num, Lab, 'lab_table')


# -------------epq------------------------


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
def EquipmentDetailView(request, num=1):
    test_epq = Equipment.objects.get(id=num)
    context = {'epq': test_epq, 'attr_names': epq_attr}
    return render(request, 'repo/epq_detail.html', context)


def EquipmentListView(request):
    return DataListView(request,
                        Equipment,
                        epq_attr,
                        table_name='Equipment Table',
                        csv_url='epq_csv',
                        create_url='epq_create',
                        detail_url='epq_detail')


def getEquipmentCSV(request):
    return getfile(request,
                   Equipment.objects.all(),
                   epq_attr_csv,
                   filename='Equipment.csv')


def EquipmentCreateView(request):
    return DataCreateView(request, EquipmentForm, 'epq_table')


def EquipmentUpdateView(request, num):
    return DataUpdateView(request, num, Equipment, EquipmentForm, 'epq_detail')


def EquipmentDeleteView(request, num):
    return DataDeleteView(request, num, Equipment, 'epq_table')


# ---------------Computer--------------------


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
def ComputerDetailView(request, num=1):
    test_comp = Computer.objects.get(id=num)
    context = {'comp': test_comp, 'attr_names': comp_attr}
    return render(request, 'repo/comp_detail.html', context)


def ComputerListView(request):
    return DataListView(request,
                        Computer,
                        comp_attr,
                        table_name='Computer Table',
                        csv_url='comp_csv',
                        create_url='comp_create',
                        detail_url='comp_detail')


def getComputerCSV(request):
    return getfile(request,
                   Computer.objects.all(),
                   comp_attr_csv,
                   filename='Computer.csv')


def ComputerCreateView(request, num=0):
    return DataCreateView(request,
                          ComputerForm,
                          'comp_table',
                          initial={'purchase_bill_no': num})


def ComputerUpdateView(request, num):
    return DataUpdateView(request, num, Computer, ComputerForm, 'comp_detail')


def ComputerDeleteView(request, num):
    return DataDeleteView(request, num, Computer, 'comp_table')


# --------------------------Software--------------


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
def SoftwareDetailView(request, num=1):
    test_soft = Software.objects.get(id=num)
    comps = Computer.objects.filter(installed_software=num).all()
    context = {
        'soft': test_soft,
        'attr_names': soft_attr,
        'installed_on': comps
    }
    return render(request, 'repo/soft_detail.html', context)


def SoftwareListView(request):
    return DataListView(request,
                        Software,
                        soft_attr,
                        table_name='Software Table',
                        csv_url='soft_csv',
                        create_url='soft_create',
                        detail_url='soft_detail')


def getSoftwareCSV(request):
    return getfile(request,
                   Software.objects.all(),
                   soft_attr_csv,
                   filename='Software.csv')


def SoftwareCreateView(request):
    return DataCreateView(request, SoftwareForm, 'soft_table')


def SoftwareUpdateView(request, num):
    return DataUpdateView(request, num, Software, SoftwareForm, 'soft_detail')


def SoftwareDeleteView(request, num):
    return DataDeleteView(request, num, Software, 'soft_table')


# --------------------------purchase--------------


def PurchaseListView(request):
    return DataListView(request,
                        Purchase,
                        purch_attr,
                        table_name='Purchase Table',
                        csv_url='purch_csv',
                        create_url='purch_create',
                        detail_url='purch_detail')


def getPurchaseCSV(request):
    return getfile(request,
                   Purchase.objects.all(),
                   purch_attr,
                   filename='Purchase.csv')


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
def PurchaseDetailView(request, num=1):
    comps = Computer.objects.filter(purchase_bill_no=num)
    # epqs = Equipment.objects.filter(purchase=num)
    # softs = Software.objects.filter(purchase=num)
    test_purch = Purchase.objects.get(id=num)
    context = {
        'purch': test_purch,
        'attr_names': purch_attr,
        'comps': comps,
        #    'epqs': epqs,
        #    'softs': softs,
    }
    return render(request, 'repo/purch_detail.html', context)


def PurchaseCreateView(request):
    return DataCreateView(request, PurchaseForm, 'purch_table')


def PurchaseUpdateView(request, num):
    return DataUpdateView(request, num, Purchase, PurchaseForm, 'purch_detail')


def PurchaseDeleteView(request, num):
    return DataDeleteView(request, num, Purchase, 'purch_table')


# ----------------user dep mapping---------------


def UserDepartmentMappingCreateView(request, num):
    return DataCreateView(request,
                          UserDepartmentMappingForm,
                          'dashboard',
                          initial={'user': num})


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
@user_passes_test(is_sub_admin, login_url='not_allowed')
def UserDepartmentMappingUnauthList(request):
    User = get_user_model()
    users = User.objects.exclude(
        id__in=[x.user.id for x in UserDepartmentMapping.objects.all()])
    context = {'users': users}
    return render(request, 'repo/new_user.html', context)


# ---------------issue-------------------------


@login_required
def IssueCreateForm(request):
    form = IssueForm
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.creator = request.user
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'repo/create.html', context)


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
@user_passes_test(is_sub_admin, login_url='not_allowed')
def IssueSolvedView(request, num):
    obj = Issue.objects.get(id=num)
    obj.is_solved = True
    obj.save()
    return redirect('dashboard')
