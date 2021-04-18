from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserDepartmentMapping

import csv

# -------------- user functions---------------------


def is_sub_admin(user):
    try:
        return UserDepartmentMapping.objects.get(User=user).Is_Sub_Admin
    except:
        return False


def get_user_dep(user):
    try:
        return UserDepartmentMapping.objects.get(User=user).Department
    except:
        return -1


def is_authorized(user):
    dep = get_user_dep(user)

    # print(dep)

    if dep == -1:
        return False
    else:
        return True


# --------------csv---------------------


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
def getlabRep(request, lab, lab_attrs, epq_l, epq_attrs, comp_l, comp_attrs):
    filename = lab.Name + ' detail.csv'

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + filename

    writer = csv.writer(response)

    writer.writerow(['lab :', lab.Name])

    writer.writerow('')
    writer.writerow(['Lab Detail'])
    writer.writerow('')

    for lab_attr in lab_attrs:
        ls = [lab_attr]
        ls.append(getattr(lab, lab_attr))
        writer.writerow(ls)

    writer.writerow('')
    writer.writerow(['Epuipmets in Lab'])
    writer.writerow('')

    writer.writerow(epq_attrs)
    for epq in epq_l:
        ls = []
        for epq_attr in epq_attrs:
            ls.append(getattr(epq, epq_attr))
        writer.writerow(ls)

    writer.writerow('')
    writer.writerow(['Computers in Lab'])
    writer.writerow('')

    writer.writerow(comp_attrs + ['Software installed'])
    for comp in comp_l:
        ls = []

        for comp_attr in comp_attrs:
            ls.append(getattr(comp, comp_attr))

        writer.writerow(ls)
        ls2 = []
        for j in ls:
            ls2 = ls2 + ['']
        for i in getattr(comp, 'Installed_Softwares').all():
            writer.writerow(ls2 + [i.Code, i.Name])

    return response


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
def getPurchaseRep(request, purch, purch_attrs, epq_l, epq_attrs, comp_l, comp_attrs, soft_l, soft_attrs):
    filename = purch.Invoice_No + ' detail.csv'

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + filename

    writer = csv.writer(response)

    writer.writerow(['Invoice_No :', purch.Invoice_No])

    writer.writerow('')
    writer.writerow(['Invoice Detail'])
    writer.writerow('')

    for purch_attr in purch_attrs:
        ls = [purch_attr]
        ls.append(getattr(purch, purch_attr))
        writer.writerow(ls)

    writer.writerow('')
    writer.writerow(['Epuipmets in Invoice'])
    writer.writerow('')

    writer.writerow(epq_attrs)
    for epq in epq_l:
        ls = []
        for epq_attr in epq_attrs:
            ls.append(getattr(epq, epq_attr))
        writer.writerow(ls)

    writer.writerow('')
    writer.writerow(['Computers in Invoice'])
    writer.writerow('')

    writer.writerow(comp_attrs)
    for comp in comp_l:
        ls = []
        for comp_attr in comp_attrs:
            ls.append(getattr(comp, comp_attr))
        writer.writerow(ls)

    writer.writerow('')
    writer.writerow(['Software in Invoice'])
    writer.writerow('')

    writer.writerow(soft_attrs)
    for soft in soft_l:
        ls = []
        for soft_attr in soft_attrs:
            ls.append(getattr(soft, soft_attr))
        writer.writerow(ls)

    return response

# -------------------common function --------------


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
def DataListView(request, Obj, attr_names, table_name, detail_url, create_url,
                 ):

    dep = get_user_dep(request.user)
    try:
        data_list = Obj.objects.filter(Department=dep).order_by('-id')
    except:
        data_list = Obj.objects.order_by('-id')

    for i in data_list:
        print(i)

    context = {
        'data_list': data_list,
        'attr_names': attr_names,
        'detail_url': detail_url,
        'create_url': create_url,
        'table_name': table_name,
    }
    return render(request, 'repo/common_table.html', context)


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
@user_passes_test(is_sub_admin, login_url='not_allowed')
def DataCreateView(request, dataForm, redirect_url, initial={}):
    form = dataForm(initial=initial)
    if request.method == 'POST':
        form = dataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)

    context = {'form': form}
    return render(request, 'repo/create.html', context)


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
@user_passes_test(is_sub_admin, login_url='not_allowed')
def DataUpdateView(request, num, Obj, dataForm, redirect_url):
    obj = Obj.objects.get(id=num)
    form = dataForm(instance=obj)
    if request.method == 'POST':
        form = dataForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(redirect_url, num)

    context = {'form': form}
    return render(request, 'repo/create.html', context)


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
@user_passes_test(is_sub_admin, login_url='not_allowed')
def DataDeleteView(request, num, Obj, redirect_url):
    obj = Obj.objects.get(id=num)
    if request.method == 'POST':
        obj.delete()
        return redirect(redirect_url)

    context = {'item': obj}
    return render(request, 'repo/delete.html', context)
