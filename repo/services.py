from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from xlsxwriter.workbook import Workbook
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


def get_lab_cost(lab):
    cost = 0

    lab = Laboratory.objects.get(id=lab)
    comps = Computer.objects.filter(Location=lab.id)
    epq = Equipment.objects.filter(Location=lab.id)

    for ls in [comps, epq]:

        for item in ls:
            purch = item.Invoice

            total = purch.Total_Cost_With_VAT

            total_comp = len(Computer.objects.filter(Invoice=purch.id))
            total_epq = len(Equipment.objects.filter(Invoice=purch.id))
            total_soft = len(Software.objects.filter(Invoice=purch.id))

            cost += total / (total_comp+total_epq+total_soft)

    return cost


# --------------csv---------------------

def writeRow(obj,  last_row, row):
    for i in range(len(row)):
        obj.write(last_row, i, row[i])


@login_required
@user_passes_test(is_authorized, login_url='not_allowed')
def getlabRep(request, lab, lab_attrs, epq_l, epq_attrs, comp_l, comp_attrs, extra):
    extra_attrs = ['Invoice', 'Supplier_Info', 'Date_YYYYMMDD',
                   'GI_No', 'Rate_With_VAT', 'Total_Cost_With_VAT']
    epq_attrs = epq_attrs[:-1]

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=lab Details.xlsx"

    book = Workbook(response, {'in_memory': True})
    sheet = book.add_worksheet('test')

    # sheet.write(0, 0, 'Hello, world!')

    cell_format = book.add_format({'bold': True})
    cell_format.set_align('center')
    cell_format.set_valign('center')

    c = 0

    sheet.merge_range(
        'A1:O1', 'K. J. SOMAIYA INSTITUTE OF ENGINEERING AND INFORMATION TECHNOLOGY Sion, Mumbai - 400022.', cell_format)
    sheet.merge_range(
        'A2:O2', str(lab.Department), cell_format)
    sheet.merge_range(
        'A3:O3', 'lab :' + lab.Name, cell_format)
    sheet.merge_range(
        'A4:O4', 'Epuipmets in Lab', cell_format)

    writeRow(sheet, 4, epq_attrs + extra_attrs)
    c = 5

    # looping for both comp and epq
    for one_ls in [comp_l, epq_l]:
        last = None
        for epq in one_ls:
            # create the data row
            ls = []
            for epq_attr in epq_attrs:
                ls.append(getattr(epq, epq_attr))

            # print data row
            if last == epq.Invoice:
                writeRow(sheet, c, [str(i) for i in ls])
                col = 9
                for e in [getattr(epq.Invoice, attr) for attr in extra_attrs]:
                    sheet.merge_range(last_empty, col, c, col, e)
                    col += 1
            else:
                last_empty = c
                writeRow(sheet, c, [
                         str(i) for i in ls + [getattr(epq.Invoice, attr) for attr in extra_attrs]])
            c += 1
            last = epq.Invoice

    c += 1

    # printing infoat bottom

    for row in [
        ['Total Rs:', get_lab_cost(lab.id)],
        ['Lab Incharge :', lab.Lab_Incharge],
        ['Lab Assistant 1 :', lab.Lab_Assistant_1],
        ['Lab Assistant 2 :', lab.Lab_Assistant_2]
    ]:
        writeRow(sheet, c, row)
        c += 1

    book.close()

    return response


@ login_required
@ user_passes_test(is_authorized, login_url='not_allowed')
def getPurchaseRep(request, purch, purch_attrs, epq_l, epq_attrs, comp_l, comp_attrs, soft_l, soft_attrs):
    filename = purch.Invoice + ' detail.csv'

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + filename

    writer = csv.writer(response)

    writer.writerow(['Invoice :', purch.Invoice])

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


@ login_required
@ user_passes_test(is_authorized, login_url='not_allowed')
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


@ login_required
@ user_passes_test(is_authorized, login_url='not_allowed')
@ user_passes_test(is_sub_admin, login_url='not_allowed')
def DataCreateView(request, dataForm, redirect_url, initial={}):
    form = dataForm(initial=initial)
    if request.method == 'POST':
        form = dataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)

    context = {'form': form}
    return render(request, 'repo/create.html', context)


@ login_required
@ user_passes_test(is_authorized, login_url='not_allowed')
@ user_passes_test(is_sub_admin, login_url='not_allowed')
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


@ login_required
@ user_passes_test(is_authorized, login_url='not_allowed')
@ user_passes_test(is_sub_admin, login_url='not_allowed')
def DataDeleteView(request, num, Obj, redirect_url):
    obj = Obj.objects.get(id=num)
    if request.method == 'POST':
        obj.delete()
        return redirect(redirect_url)

    context = {'item': obj}
    return render(request, 'repo/delete.html', context)
