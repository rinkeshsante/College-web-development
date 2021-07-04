from django.contrib import admin

from .models import *


class ComputerInline(admin.TabularInline):
    model = Computer


class EquipnmentInline(admin.TabularInline):
    model = Equipment


class SoftwareInline(admin.TabularInline):
    model = Software


class LaboratoryAdmin(admin.ModelAdmin):
    inlines = [ComputerInline, EquipnmentInline]

    list_display = (
        'Name',
        'Room_no',
        'Lab_Incharge',
        'Seating_Capacity'
    )


class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'Name',
        'Dep_admin',
    )


class ClassRoomAdmin(admin.ModelAdmin):
    list_display = (
        'Name',
        'Room_no',
        'No_of_benches',
        'Seating_Capacity'
    )


class CabinAdmin(admin.ModelAdmin):
    list_display = (
        'Name',
        'Room_no',
        'Details',
        'Seating_Capacity'
    )


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Code', 'Location')


class UserDepartmentMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'User', 'Department')


class ComputerAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Code', 'Location')


class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('Name', 'GI_No', 'Code')


class PurchaseAdmin(admin.ModelAdmin):
    inlines = [ComputerInline, SoftwareInline, EquipnmentInline]
    list_display = ('Invoice', 'Date_YYYYMMDD', 'Rate_With_VAT',
                    'Total_Cost_With_VAT')


class IssueAdmin(admin.ModelAdmin):
    list_display = ('Header', 'Is_Solved', 'Creator', 'Date_YYYYMMDD')


admin.site.register(Department)
admin.site.register(UserDepartmentMapping, UserDepartmentMappingAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)
admin.site.register(Cabin, CabinAdmin)
admin.site.register(Laboratory, LaboratoryAdmin)
