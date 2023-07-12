from django.contrib import admin
from .models import *


@admin.register(PersonInformation)
class PersonInformationAdmin(admin.ModelAdmin):
    search_fields = (
        'first_name',
        'last_name',
    )
    list_filter = ('id', 'height', 'weight',)
    list_display_links = ('last_name', 'first_name',)
    list_display = ('id',
                    'last_name',
                    'first_name',
                    'date_of_birthday',
                    'nationality',
                    'address',
                    'foreign_languages',
                    'nationality',
                    'height',
                    'weight',
                    'phone_number',
                    'person_education',
                    'work_experience',
                    'car_info',
                    )


admin.site.register(Logos)
# admin.site.register(PersonInformation)
admin.site.register(PersonEducation)
admin.site.register(WasHeAbroad)
admin.site.register(StateAwards)
admin.site.register(ParticipateInElections)
admin.site.register(WorkExperience)
admin.site.register(Punishment)
admin.site.register(AppreciationLetter)
admin.site.register(Rewards)
admin.site.register(Vacation)
admin.site.register(AdditionalVacation)
admin.site.register(HealthVacation)
admin.site.register(UnpaidLeave)
admin.site.register(BusinessTrip)
admin.site.register(CarInfo)
admin.site.register(CriminalLiability)
admin.site.register(RelativesLivingAbroad)
