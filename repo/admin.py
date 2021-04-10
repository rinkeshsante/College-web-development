from django.contrib import admin

from .models import *


class ComputerInline(admin.TabularInline):
    model = Computer


class EquipnmentInline(admin.TabularInline):
    model = Equipment


class LabAdmin(admin.ModelAdmin):
    inlines = [ComputerInline, EquipnmentInline]

    list_display = (
        # 'Code',
        'Name',
        'Lab_Number',
    )


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Code', 'Location')


class UserDepartmentMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'Department')


class ComputerAdmin(admin.ModelAdmin):
    # inlines = [
    #     ComputerSoftwareInline,
    # ]
    list_display = ('Name', 'Code', 'Location')


class SoftwareAdmin(admin.ModelAdmin):
    # inlines = [
    #     ComputerSoftwareInline,
    # ]
    list_display = ('name', 'gi_no', 'code')


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('Invoice_No', 'Date', 'Rate_With_VAT',
                    'Total_Cost_With_VAT')


class IssueAdmin(admin.ModelAdmin):
    list_display = ('Header', 'Is_Solved', 'Creator', 'Date')


admin.site.register(Department)
admin.site.register(Lab, LabAdmin)
admin.site.register(UserDepartmentMapping, UserDepartmentMappingAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Issue, IssueAdmin)
# admin.site.register(LabFacultyMapping, LabFacultyMappingAdmin)
