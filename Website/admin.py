from django.contrib import admin
from .models import TalentCategories,Talent,Advertisement

# Register your models here.


class CustomTalentFilter(admin.SimpleListFilter):
    title = ("Category")
    parameter_name = "category"

    def lookups(self, request, model_admin):
        # Example:
        # def lookups(self, request, model_admin):
        # countries = set([c.country for c in model_admin.model.objects.all()])
        # return [(c.id, c.name) for c in countries] + [
        #   ('AFRICA', 'AFRICA - ALL')]

        categories = set([talents.category for talents in model_admin.model.objects.all()])
        return [(category.id, category.category_title) for category in categories]
    

    def queryset(self, request, queryset):
        # to decide how to filter the queryset.
        # if self.value() == 'AFRICA':
        #     return queryset.filter(country__continent='Africa')
        #               OR
        if self.value():
            return queryset.filter(
                category=self.value(),
                # paid=False,
            )




class CustomTalent(admin.ModelAdmin):
    list_display=(Talent.name,"category","stage_name","gender")
    list_filter=("gender",CustomTalentFilter)
    list_per_page=10


admin.site.register(TalentCategories)
admin.site.register(Talent,CustomTalent)
admin.site.register(Advertisement)


