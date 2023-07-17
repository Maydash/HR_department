from django.contrib import admin
from .models import *

class PersonEducationInline(admin.StackedInline):
    model = PersonEducation
    fields = ('place_of_university', 'name_of_university', 'date_of_finishing_university', 'diploma_id', 'name_of_academy', 'date_of_finishing_academy', 'academy_diploma_id', 'remote', 'full_time', 'confirmation_of_education', 'date_of_confirmation', 'education_degree', 'major', 'scientific_degree')
    extra = 1

class WasHeAboardInline(admin.StackedInline):
    model = WasHeAbroad
    fields = ('person', 'name_of_country', 'date')
    extra = 1

class StateAwardsInline(admin.StackedInline):
    model = StateAwards
    fields = ('name_of_award', 'order_id', 'order_date')
    extra = 1

class WorkExperienceInline(admin.StackedInline):
    model = WorkExperience
    fields = ('total_experience', 'experience_in_court', 'experience_in_army', 'experience_in_education', 'experience_in_last_position')
    extra = 1

class ParticipateInElectionsInline(admin.StackedInline):
    model = ParticipateInElections
    fields = ('note', )
    extra = 1

class PunishmentInline(admin.StackedInline):
    model = Punishment
    fields = ('name', 'order_id', 'order_date')
    extra = 1

class AppreciationLetterInline(admin.StackedInline):
    model = AppreciationLetter
    fields = ('name', 'order_id', 'order_date')
    extra = 1

class RewardsInline(admin.StackedInline):
    model = Rewards
    fields = ('name', 'order_id', 'order_date')
    extra = 1

class VacationInline(admin.StackedInline):
    model = Vacation
    fields = ('name', 'order_id', 'order_date')
    extra = 1

class AdditionalVacationInline(admin.StackedInline):
    model = AdditionalVacation
    fields = ('name', 'order_id', 'order_date')
    extra = 1

class HealthVacationInline(admin.StackedInline):
    model = HealthVacation
    fields = ('name', 'order_id', 'order_date')
    extra = 1

class UnpaidLeaveInline(admin.StackedInline):
    model = UnpaidLeave
    fields = ('name', 'order_id', 'order_date')
    extra = 1

class BusinessTripInline(admin.StackedInline):
    model = BusinessTrip
    fields = ('name_of_country', 'order_id', 'order_date', 'start_date', 'end_date')
    extra = 1

class CarInfoInline(admin.StackedInline):
    model = CarInfo
    fields = ('name', 'date_manufacture', 'is_own')
    extra = 1

class CriminalLiabilityInline(admin.StackedInline):
    model = CriminalLiability
    fields = ('name', 'date', 'court_info')
    extra = 1

class RelativesLivingAbroadInline(admin.StackedInline):
    model = RelativesLivingAbroad
    fields = ('name', 'country_name', 'start_date', 'end_date')
    extra = 1

@admin.register(PersonInformation)
class PersonInformationAdmin(admin.ModelAdmin):

    search_fields = (
        'first_name',
        'last_name',
        'person_CarInfo__name',
    )
    list_filter = ('id', 'height', 'weight',)
    readonly_fields = ('author', 'members')
    list_display_links = ('last_name', 'first_name',)
    list_display = ('id',
                    'last_name',
                    'first_name',
                    'date_of_birthday',
                    'nationality',
                    'address',
                    'foreign_languages',
                    'washeaboard_titles',
                    'person_education_titles',
                    'stateawards_titles',
                    )
    inlines = [WasHeAboardInline,
               PersonEducationInline,
               StateAwardsInline,
               WorkExperienceInline,
               ParticipateInElectionsInline,
               PunishmentInline,
               AppreciationLetterInline,
               RewardsInline,
               VacationInline,
               AdditionalVacationInline,
               HealthVacationInline,
               UnpaidLeaveInline,
               BusinessTripInline,
               CarInfoInline,
               CriminalLiabilityInline,
               RelativesLivingAbroadInline
               ]

    def washeaboard_titles(self, obj):
        return  ', '.join([b.name_of_country for b in obj.person_WasHeAbroad.all()])

    washeaboard_titles.short_description = 'Daşary ýurtda bolanmy'

    def person_education_titles(self, obj):
        return ', '.join([b.name_of_university for b in obj.person.all()])

    person_education_titles.short_description = 'Bilimi barada maglumat'

    def stateawards_titles(self, obj):
        return ', '.join([b.name_of_award for b in obj.person_StateAwards.all()])

    stateawards_titles.short_description = 'Döwlet sylaglary barada maglumat'


# admin.site.register(Logos)
# # admin.site.register(PersonInformation)
# admin.site.register(PersonEducation)
# admin.site.register(WasHeAbroad)
# admin.site.register(StateAwards)
# admin.site.register(ParticipateInElections)
# admin.site.register(WorkExperience)
# admin.site.register(Punishment)
# admin.site.register(AppreciationLetter)
# admin.site.register(Rewards)
# admin.site.register(Vacation)
# admin.site.register(AdditionalVacation)
# admin.site.register(HealthVacation)
# admin.site.register(UnpaidLeave)
# admin.site.register(BusinessTrip)
# admin.site.register(CarInfo)
# admin.site.register(CriminalLiability)
# admin.site.register(RelativesLivingAbroad)
