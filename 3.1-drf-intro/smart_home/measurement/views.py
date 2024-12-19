# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer, ListOfSensorsSerializer





class ListAllView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = ListOfSensorsSerializer

    def post(self,request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        sensor_names = Sensor.objects.filter(name=name)
        if sensor_names:
            return Response({'status':'такой датчик уже есть'})
        Sensor.objects.create(name=name, description=description).save()
        return Response({'create sensor status':'created'})


class MeasurementsView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self,request):
        sensor_id = request.POST.get('id')
        temperature = request.POST.get('temperature')
        sensor_selected = Sensor.objects.filter(pk=sensor_id)
        if sensor_selected:
            Measurement.objects.create(sensor_id=sensor_id, temperature=temperature).save()
            return Response({'status': 'temperature data updated'})
        else:
            return Response({'status': 'sensor ID not in DATABASE'})


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    def patch(self,request, pk):
        dat = Sensor.objects.all()
        for sensor in dat:
            if str(sensor.pk) == pk:
                sensor = Sensor.objects.get(pk=pk)
                sensor_amend = ListOfSensorsSerializer(sensor, data=request.data, partial=True)
                if sensor_amend.is_valid():
                    sensor_amend.save()
                return Response({'status': 'amend success'})
        return Response({'status': 'sensor ID not in DATABASE'})



