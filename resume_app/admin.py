from django.contrib import admin
from .models import Personal,Education,Employment,Skill,Project,Certificate


admin.site.register(Personal)
admin.site.register(Education)
admin.site.register(Employment)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Certificate)