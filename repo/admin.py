from django.contrib import admin

from.models import Lab,Department,Equipment,Software,LabFacultyMapping,ComputerSoftwareMapping

# #
class EquipmentInline(admin.TabularInline):
    model =Equipment
    list_display=('code','name',)

class LabAdmin(admin.ModelAdmin):
    # inlines=[
    #     EquipmentInline
    # ]
    list_display=('code','name','lab_number',)

class EquipmentAdmin(admin.ModelAdmin):
    list_display=('name','gi_no','rate','code','lab')

class SoftwareAdmin(admin.ModelAdmin):
    list_display=('name','gi_no','rate','code')

class LabFacultyMappingAdmin(admin.ModelAdmin):
    list_display=('lab','faculty')


admin.site.register(Department)
admin.site.register(Lab,LabAdmin)
admin.site.register(Equipment,EquipmentAdmin)
admin.site.register(Software,SoftwareAdmin)
admin.site.register(LabFacultyMapping,LabFacultyMappingAdmin)
admin.site.register(ComputerSoftwareMapping)
# admin.site.register(LabEquipmentMapping)