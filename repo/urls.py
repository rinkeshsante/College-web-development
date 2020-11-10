from django.urls import path

from .views import *

urlpatterns = [
    path('', DashBoardView, name='dashboard'),
    path('about/', AboutView, name='about'),
    path('not_found/', notFound, name='not_found'),
    path('not_allowed/', Unauthorized, name='not_allowed'),

    # user dep
    path('new_user/<int:num>/', UserDepartmentMappingCreateView,
         name='user_dep_create'),
    path('new_user/', UserDepartmentMappingUnauthList, name='user_unauth_list'),

    # issue
    path('issue/new/', IssueCreateForm, name='issue_create'),
    path('issue/solved/<int:num>/', IssueSolvedView, name='issue_solved'),


    # lab
    path('lab/', LabListView, name='lab_table'),
    path('lab/csv', getLabCSV, name='lab_csv'),
    path('lab/<int:num>/', LabDetailView, name='lab_detail'),
    path('lab/new/', LabCreateView, name='lab_create'),
    path('lab/update/<int:num>/', LabUpdateView, name='lab_update'),
    path('lab/delete/<int:num>/', LabDeleteView, name='lab_delete'),

    # epq
    path('equipment/', EquipmentListView, name='epq_table'),
    path('equipment/csv', getEquipmentCSV, name='epq_csv'),
    path('equipment/<int:num>/', EquipmentDetailView, name='epq_detail'),
    path('equipment/new/', EquipmentCreateView, name='epq_create'),
    path('equipment/update/<int:num>/', EquipmentUpdateView, name='epq_update'),
    path('equipment/delete/<int:num>/', EquipmentDeleteView, name='epq_delete'),

    # comp
    path('computer/', ComputerListView, name='comp_table'),
    path('computer/csv', getComputerCSV, name='comp_csv'),
    path('computer/<int:num>/', ComputerDetailView, name='comp_detail'),
    path('computer/new/', ComputerCreateView, name='comp_create'),
    path('computer/update/<int:num>/', ComputerUpdateView, name='comp_update'),
    path('computer/delete/<int:num>/', ComputerDeleteView, name='comp_delete'),

    # soft
    path('software/', SoftwareListView, name='soft_table'),
    path('software/csv', getSoftwareCSV, name='soft_csv'),
    path('software/<int:num>/', SoftwareDetailView, name='soft_detail'),
    path('software/new/', SoftwareCreateView, name='soft_create'),
    path('software/update/<int:num>/', SoftwareUpdateView, name='soft_update'),
    path('software/delete/<int:num>/', SoftwareDeleteView, name='soft_delete'),

    # purch
    path('purchase/', PurchaseListView, name='purch_table'),
    path('purchase/csv', getPurchaseCSV, name='purch_csv'),
    path('purchase/<int:num>/', PurchaseDetailView, name='purch_detail'),
    path('purchase/new/', PurchaseCreateView, name='purch_create'),
    path('purchase/update/<int:num>/', PurchaseUpdateView, name='purch_update'),
    path('purchase/delete/<int:num>/', PurchaseDeleteView, name='purch_delete'),


]
