from django.contrib import admin
from home.models import Student, HighSchoolList

#register ModelAdmin objects for custom admin page if needed. This is optional
class StudentAdmin(admin.ModelAdmin):
	list_display = ('user', 'firstname', 'lastname', 'race','act_composite','get_email')
	def get_email(self,obj):
		return obj.user.email
	get_email.short_description = 'Email'
	get_email.admin_order_field = 'user__email'

class HighSchoolListAdmin(admin.ModelAdmin):
	list_display = ('name', 'borough', 'school_type','institution_type')

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(HighSchoolList, HighSchoolListAdmin)