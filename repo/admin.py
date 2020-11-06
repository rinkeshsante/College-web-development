from django.contrib import admin

from.models import *


class ComputerInline(admin.TabularInline):
    model = Computer


class EquipnmentInline(admin.TabularInline):
    model = Equipment


class LabAdmin(admin.ModelAdmin):
    inlines = [
        ComputerInline,
        EquipnmentInline
    ]

    list_display = ('code', 'name', 'lab_number',)


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'gi_no', 'code', 'lab')


class UserDepartmentMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'department')


class ComputerAdmin(admin.ModelAdmin):
    # inlines = [
    #     ComputerSoftwareInline,
    # ]
    list_display = ('name', 'gi_no', 'code', 'lab')


class SoftwareAdmin(admin.ModelAdmin):
    # inlines = [
    #     ComputerSoftwareInline,
    # ]
    list_display = ('name', 'gi_no', 'code')


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('bill_no', 'date', 'rate')

# class LabFacultyMappingAdmin(admin.ModelAdmin):
#     list_display=('lab','faculty')


admin.site.register(Department)
admin.site.register(Lab, LabAdmin)
admin.site.register(UserDepartmentMapping, UserDepartmentMappingAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Purchase, PurchaseAdmin)

# admin.site.register(LabEquipmentMapping)
# admin.site.register(LabFacultyMapping, LabFacultyMappingAdmin)
