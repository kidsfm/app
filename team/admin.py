from django.contrib import admin
from .forms 		import MemberAdminForm
from .models		import Member, Interest, Role



# Config inline admin form for Interest model
class InterestInline(admin.TabularInline):
    model   = Member.interests.through
    extra   = 1
    max_num = 5



# Config admin form for Member model
class MemberAdmin(admin.ModelAdmin):
    form = MemberAdminForm
    list_display = [
		# ToDo:
		# - enable image preview in Member admin list
		# see: http://stackoverflow.com/questions/16307307/django-admin-show-image-from-imagefield
    	#'profile_img',
    	'first_name',
    	'last_name',
    	'role',
    ]
    inlines = [
        InterestInline,
    ]
    exclude = ('interests',)

# Register Member model and admin form
admin.site.register(Member, MemberAdmin)



# Config admin form for Member model
class RoleAdmin(admin.ModelAdmin):
    list_display = [
    	'label',
    	'description',
    ]

# Register Role model and admin form
admin.site.register(Role, RoleAdmin)



# Config admin form for Member model
class InterestAdmin(admin.ModelAdmin):
    list_display = [
    	'label',
    	'description',
    ]

# Register Interest model and admin form
admin.site.register(Interest, InterestAdmin)






