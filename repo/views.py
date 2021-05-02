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

    total_lab = Laboratory.objects.count()
    total_class = ClassRoom.objects.count()
    total_cabin = Cabin.objects.count()
    total_epq = Equipment.objects.count()
    total_soft = Software.objects.count()
    total_comp = Computer.objects.count()
    total_purch = Purchase.objects.count()

    issues = Issue.objects.filter(Is_Solved=False)

    context = {
        'total_lab': total_lab,
        'total_class': total_class,
        'total_cabin': total_cabin,
        'total_epq': total_epq,
        'total_soft': total_soft,
        'total_comp': total_comp,
        'total_purch': total_purch,
        'issues': issues,
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
    'id', 'Name', 'Room_no', 'Lab_Incharge', 'Seating_Capacity',

    'Intercom_No', 'Lab_Assistant_1', 'Lab_Assistant_2',
    'Practicals_conducted_Odd_SEM', 'Practicals_conducted_Even_SEM', 'Other_Data',

    'No_of_Fans', 'No_of_AC', 'No_of_Light_Sounce', 'Area_In_sq_m', 'Total_cost'
]

classroom_attr = [
    'id', 'Name', 'Room_no', 'Seating_Capacity',

    'Teaching_Tools', 'is_stepped_Room', 'No_of_benches',

    'Department', 'No_of_Fans', 'No_of_AC', 'No_of_Light_Sounce', 'Area_In_sq_m', 'Total_cost',
]

cabin_attr = [
    'id', 'Name', 'Room_no', 'Seating_Capacity',

    'Intercom_No', 'Details', 'No_of_Tables',

    'Department', 'No_of_Fans', 'No_of_AC', 'No_of_Light_Sounce', 'Area_In_sq_m', 'Total_cost',
]


epq_attr = [
    'id', 'Name', 'Equipment_No', 'Code',  'Status', 'Location','Located_since',

    'Department', 'Invoice', 'Remarks'
]


comp_attr = [
    'id', 'Name', 'Equipment_No', 'Code',  'Status', 'Location','Located_since',

    'RAM', 'Storage_in_GB', 'Processor',

    'Department', 'Invoice', 'Remarks'
]


soft_attr = [
    'id', 'Name', 'Software_No', 'Code', 'Status',

    'Invoice', 'GI_No', 'Licenced_Qty',
]

purch_attr = [
    'id', 'Invoice_No', 'Supplier_Info', 'Date_YYYYMMDD', 'GI_No', 'Rate_With_VAT', 'Total_Cost_With_VAT',
]

# -------------labs-------------------------------


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
def LabDetailView(request, num=1):
    test_lab = Laboratory.objects.get(id=num)
    eqps = Equipment.objects.filter(Location=test_lab.id)
    comps = Computer.objects.filter(Location=test_lab.id)
    context = {
        'lab': test_lab,
        'equipments': eqps,
        'computers': comps,
        'attr_names': lab_attr,
        'extra':{
            'No of Equipments':len(eqps),
            'No of Computers':len(comps)
            }
    }

    print(context)
    return render(request, 'repo/lab_detail.html', context)


def LabListView(request):
    return DataListView(request,
                        Laboratory,
                        lab_attr,
                        table_name='Lab Table',
                        create_url='lab_create',
                        detail_url='lab_detail')


def getLabReport(request, num=1):
    test_lab = Laboratory.objects.get(id=num)
    epq_in_lab = Equipment.objects.filter(Location=num)
    comp_in_lab = Computer.objects.filter(Location=num)
    extra = {
        'No of Equipments':len(epq_in_lab),
        'No of Computers':len(comp_in_lab)
    }
    return getlabRep(request, test_lab, lab_attr, epq_in_lab, epq_attr,
                     comp_in_lab, comp_attr,extra)


def LabCreateView(request):
    return DataCreateView(request, LabForm, 'lab_table')


def LabUpdateView(request, num):
    return DataUpdateView(request, num, Laboratory, LabForm, 'lab_detail')


def LabDeleteView(request, num):
    return DataDeleteView(request, num, Laboratory, 'lab_table')


# ---------------class room-----------------

@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
def ClassRoomDetailView(request, num=1):
    test_room = ClassRoom.objects.get(id=num)
    context = {'classroom': test_room, 'attr_names': classroom_attr}
    return render(request, 'repo/class_detail.html', context)


def ClassRoomListView(request):
    return DataListView(request,
                        ClassRoom,
                        classroom_attr,
                        table_name='ClassRoom Table',
                        create_url='class_create',
                        detail_url='class_detail')


def ClassRoomCreateView(request, num=0):
    return DataCreateView(request,
                          ClassRoomForm,
                          'class_table',
                          initial={'Invoice': num})


def ClassRoomUpdateView(request, num):
    return DataUpdateView(request, num, ClassRoom, ClassRoomForm, 'class_detail')


def ClassRoomDeleteView(request, num):
    return DataDeleteView(request, num, ClassRoom, 'class_table')

# ---------------cabin room-----------------


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
def CabinDetailView(request, num=1):
    test_cabin = Cabin.objects.get(id=num)
    context = {'cabin': test_cabin, 'attr_names': cabin_attr}
    return render(request, 'repo/cabin_detail.html', context)


def CabinListView(request):
    return DataListView(request,
                        Cabin,
                        cabin_attr,
                        table_name='Cabin Table',
                        create_url='cabin_create',
                        detail_url='cabin_detail')


def CabinCreateView(request, num=0):
    return DataCreateView(request,
                          CabinForm,
                          'cabin_table',
                          initial={'Invoice': num})


def CabinUpdateView(request, num):
    return DataUpdateView(request, num, Cabin, CabinForm, 'cabin_detail')


def CabinDeleteView(request, num):
    return DataDeleteView(request, num, Cabin, 'cabin_table')


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
                        create_url='epq_create',
                        detail_url='epq_detail')


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
                        create_url='comp_create',
                        detail_url='comp_detail')


def ComputerCreateView(request, num=0):
    return DataCreateView(request,
                          ComputerForm,
                          'comp_table',
                          initial={'Invoice': num})


def ComputerUpdateView(request, num):
    return DataUpdateView(request, num, Computer, ComputerForm, 'comp_detail')


def ComputerDeleteView(request, num):
    return DataDeleteView(request, num, Computer, 'comp_table')


# --------------------------Software--------------


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
def SoftwareDetailView(request, num=1):
    test_soft = Software.objects.get(id=num)
    comps = Computer.objects.filter(Installed_Softwares=num).all()
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
                        create_url='soft_create',
                        detail_url='soft_detail')


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
                        create_url='purch_create',
                        detail_url='purch_detail')


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
def PurchaseDetailView(request, num=1):
    comps = Computer.objects.filter(Invoice=num)
    epqs = Equipment.objects.filter(Invoice=num)
    softs = Software.objects.filter(Invoice=num)
    test_purch = Purchase.objects.get(id=num)
    context = {
        'purch': test_purch,
        'attr_names': purch_attr,
        'comps': comps,
        'epqs': epqs,
        'softs': softs,
    }
    return render(request, 'repo/purch_detail.html', context)


def PurchaseCreateView(request):
    return DataCreateView(request, PurchaseForm, 'purch_table')


def PurchaseUpdateView(request, num):
    return DataUpdateView(request, num, Purchase, PurchaseForm, 'purch_detail')


def PurchaseDeleteView(request, num):
    return DataDeleteView(request, num, Purchase, 'purch_table')


def getPurchaseReport(request, num=1):
    test_purch = Purchase.objects.get(id=num)
    epq_in_lab = Equipment.objects.filter(Invoice=num)
    comp_in_lab = Computer.objects.filter(Invoice=num)
    soft_in_lab = Software.objects.filter(Invoice=num)
    return getPurchaseRep(request, test_purch, purch_attr, epq_in_lab, epq_attr,
                          comp_in_lab, comp_attr, soft_in_lab, soft_attr)


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
        id__in=[x.User.id for x in UserDepartmentMapping.objects.all()])
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
            form.Creator = request.user
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'repo/create.html', context)


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
@user_passes_test(is_sub_admin, login_url='not_allowed')
def IssueSolvedView(request, num):
    obj = Issue.objects.get(id=num)
    obj.Is_Solved = True
    obj.save()
    return redirect('dashboard')
