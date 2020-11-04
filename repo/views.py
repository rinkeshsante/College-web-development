from django.shortcuts import render, redirect, HttpResponse
from .models import Lab, Equipment, Software, Computer, Purchase
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import LabForm, EquipmentForm, SoftwareForm, ComputerForm, PurchaseForm

from .services import getfile, is_sub_admin, is_teacher, DataCreateView, DataUpdateView, DataDeleteView


def getCSV(request):
    return getfile(request, Lab.objects.all(), ['id', 'name'])


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
    }
    return render(request, 'repo/dashboard.html', context)

# ----------------- unauthorized----------------------


def Unauthorized(request):
    return HttpResponse('<h1>sorry not allowed for you</h1>')

# -------------labs------------------------


@login_required
@user_passes_test(is_sub_admin, login_url='error')
def LabDetailView(request, num=1):
    test_lab = Lab.objects.get(id=num)
    eqps = Equipment.objects.filter(lab=test_lab.id)
    context = {'lab': test_lab, 'equipments': eqps}
    return render(request, 'repo/lab/lab_detail.html', context)


@login_required
def LabListView(request):
    lab_list = Lab.objects.order_by('-id')
    context = {'lab_list': lab_list}
    return render(request, 'repo/lab/lab_table.html', context)


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
    # eqps = Equipment.objects.filter(lab=test_lab.id)
    context = {'soft': test_soft}
    return render(request, 'repo/soft/soft_detail.html', context)


@login_required
def SoftwareCreateView(request):
    form = SoftwareForm()
    if request.method == 'POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('soft_table')

    context = {'form': form}
    return render(request, 'repo/create.html', context)


@login_required
def SoftwareUpdateView(request, num):
    epq = Software.objects.get(id=num)
    form = SoftwareForm(instance=epq)
    if request.method == 'POST':
        form = SoftwareForm(request.POST, instance=epq)
        if form.is_valid():
            form.save()
            return redirect('soft_detail', num)

    context = {'form': form}
    return render(request, 'repo/create.html', context)


@login_required
def SoftwareDeleteView(request, num):
    epq = Software.objects.get(id=num)
    if request.method == 'POST':
        epq.delete()
        return redirect('soft_table')

    context = {'item': epq}
    return render(request, 'repo/delete.html', context)
