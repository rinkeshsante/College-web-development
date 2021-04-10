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
def getfile(request, data, attr_names, filename='datafile.csv'):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + filename

    writer = csv.writer(response)

    writer.writerow(attr_names)
    for data_item in data:
        ls = []
        for attr_name in attr_names:
            ls.append(getattr(data_item, attr_name))
        writer.writerow(ls)
    return response


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
def getlabRep(request, lab, lab_attrs, epq_l, epq_attrs, comp_l, comp_attrs):
    filename = lab.name + ' detail.csv'

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + filename

    writer = csv.writer(response)

    writer.writerow(['lab :', lab.name])

    writer.writerow('')
    writer.writerow(['Lab Detail'])
    writer.writerow('')

    for lab_attr in lab_attrs:
        ls = [lab_attr]
        ls.append(getattr(lab, lab_attr))
        writer.writerow(ls)

    writer.writerow('')
    writer.writerow(['epuipmets in lab'])
    writer.writerow('')

    writer.writerow(epq_attrs)
    for epq in epq_l:
        ls = []
        for epq_attr in epq_attrs:
            ls.append(getattr(epq, epq_attr))
        writer.writerow(ls)

    writer.writerow('')
    writer.writerow(['computers in lab'])
    writer.writerow('')

    writer.writerow(comp_attrs + ['software installed'])
    for comp in comp_l:
        ls = []

        for comp_attr in comp_attrs:
            ls.append(getattr(comp, comp_attr))

        writer.writerow(ls)
        ls2 = []
        for j in ls:
            ls2 = ls2 + ['']
        for i in getattr(comp, 'installed_software').all():
            writer.writerow(ls2 + [i.code, i.name])

    return response


# -------------------common function --------------


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
def DataListView(request, Obj, attr_names, table_name, detail_url, create_url,
                 csv_url):
    data_list = Obj.objects.order_by('-id')
    context = {
        'data_list': data_list,
        'attr_names': attr_names,
        'detail_url': detail_url,
        'create_url': create_url,
        'table_name': table_name,
        'csv_url': csv_url
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
