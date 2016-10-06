from django.contrib import admin

# Register your models here.

from .models import Games,Player_Reg_Details

admin.site.register(Games)

#populate other models

admin.site.register(Player_Reg_Details)
# admin.site.register(Games)
# admin.site.register(Games)
# admin.site.register(Games)
# admin.site.register(Games)




