from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *



class CreatePersonInformation(APIView):

    def post(self, request, format=None):
        car_info_data = request.data.get('car_info_data')
        participate_in_elections_data = request.data.get('participate_in_elections_data')

        car_info_serializer = CarInfoSerializer(data=car_info_data)
        if car_info_serializer.is_valid():
            car_info_serializer.save()

        participate_in_elections_serializer = ParticipateInElectionsSerializer(data=participate_in_elections_data)
        if participate_in_elections_serializer.is_valid():
            participate_in_elections_serializer.save()

        return Response('Data added successfully')

