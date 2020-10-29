from django.urls import path

from .views import (
    DashBoardView,Unauthorized,
    
    LabCreateView,LabUpdateView,LabDetailView, LabDeleteView,LabListView,
    
    EquipmentCreateView,EquipmentUpdateView,EquipmentDeleteView,EquipmentListView,EquipmentDetailView,

    SoftwareCreateView,SoftwareDeleteView,SoftListView,SoftDetailView,SoftwareUpdateView,

    ComputerSoftwareMappingCreateView,ComputerSoftwareMappingUpdateView,ComputerSoftwareMappingDeleteView
)

urlpatterns =[
    path('',DashBoardView,name ='dashboard'),
    path('error/',Unauthorized,name ='error'),
    
    #lab
    path('lab/',LabListView,name ='lab_table'),
    path('lab/<int:num>/',LabDetailView,name ='lab_detail'),
    path('lab/new/',LabCreateView,name ='lab_create'),
    path('lab/update/<int:num>/',LabUpdateView,name ='lab_update'),
    path('lab/delete/<int:num>/', LabDeleteView, name='lab_delete'),

    #epq
    path('epq/',EquipmentListView,name ='epq_table'),
    path('epq/<int:num>/',EquipmentDetailView,name ='epq_detail'),
    path('equipment/new/',EquipmentCreateView,name ='epq_create'),
    path('equipment/update/<int:num>/',EquipmentUpdateView,name ='epq_update'),
    path('equipment/delete/<int:num>/', EquipmentDeleteView, name='epq_delete'),

    #soft
    path('soft/',SoftListView,name ='soft_table'),
    path('soft/<int:num>/',SoftDetailView,name ='soft_detail'),
    path('software/new/',SoftwareCreateView,name ='soft_create'),
    path('software/update/<int:num>/',SoftwareUpdateView,name ='soft_update'),
    path('software/delete/<int:num>/', SoftwareDeleteView, name='soft_delete'),

    #CSMapping
    
]