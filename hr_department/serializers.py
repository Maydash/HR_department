from rest_framework import serializers
from .models import *


class PersonEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonEducation
        fields = '__all__'


class WasHeAbroadSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasHeAbroad
        fields = '__all__'


class StateAwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateAwards
        fields = '__all__'


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'


class ParticipateInElectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipateInElections
        fields = '__all__'


class PunishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Punishment
        fields = '__all__'


class AppreciationLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppreciationLetter
        fields = '__all__'


class RewardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rewards
        fields = '__all__'


class VacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = '__all__'


class AdditionalVacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalVacation
        fields = '__all__'


class HealthVacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthVacation
        fields = '__all__'


class UnpaidLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnpaidLeave
        fields = '__all__'


class BusinessTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessTrip
        fields = '__all__'


class CarInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInfo
        fields = '__all__'


class CriminalLiabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CriminalLiability
        fields = '__all__'


class RelativesLivingAbroadSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelativesLivingAbroad
        fields = '__all__'


class PersonInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonInformation
        fields = '__all__'

