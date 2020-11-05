
from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test

import csv

# -------------- user functions---------------------


def is_sub_admin(user):
    return user.groups.filter(name='sub_admin').exists()


def is_teacher(user):
    return user.groups.filter(name='teacher').exists()


def get_user_dep(user):
    return user.department()

# --------------csv---------------------


@login_required
def getfile(request, data, attr_names, filename='datafile.csv'):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename='+filename

    writer = csv.writer(response)

    writer.writerow(attr_names)
    for data_item in data:
        ls = []
        for attr_name in attr_names:
            ls.append(getattr(data_item, attr_name))
        writer.writerow(ls)
    return response

# -------------------common function --------------


@login_required
def DataListView(request, Obj, attr_names, table_name, detail_url, create_url, csv_url):
    data_list = Obj.objects.order_by('-id')
    context = {'data_list': data_list,
               'attr_names': attr_names,
               'detail_url': detail_url,
               'create_url': create_url,
               'table_name': table_name,
               'csv_url': csv_url}
    print(data_list, attr_names)
    return render(request, 'repo/common_table.html', context)


@login_required
def DataCreateView(request, dataForm, redirect_url):
    form = dataForm()
    if request.method == 'POST':
        form = dataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)

    context = {'form': form}
    return render(request, 'repo/create.html', context)


@login_required
# @user_passes_test(is_sub_admin, login_url='error')
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
# @user_passes_test(is_sub_admin, login_url='error')
def DataDeleteView(request, num, Obj, redirect_url):
    obj = Obj.objects.get(id=num)
    if request.method == 'POST':
        obj.delete()
        return redirect(redirect_url)

    context = {'item': obj}
    return render(request, 'repo/delete.html', context)
