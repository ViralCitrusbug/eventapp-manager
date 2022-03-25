from asyncio.windows_events import NULL
from re import T
from this import d
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from . models import *
from . serializer import *

# Create your views here.

class EventList(APIView):
    def get(self,request):
        queryset = Event.objects.all()
        serialize = EventSerializer(queryset,many=True)
        return Response(serialize.data)

    def post(self,request):
        serialize = EventSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)

class EventDetail(APIView):
    def get_event(self,pk):
        try:
            event = Event.objects.get(pk=pk)
            return event
        except Event.DoesNotExist:
            return False
        
    # def get(self,request,pk):
    #     if self.get_event(pk):
    #         events = Event.objects.filter(pk=pk)
    #         dates = events.first().eventdate_set.all()
    #         data = []
    #         slot = []
    #         available_slot=[]
    #         dates_filter = {}
    #         for date in dates:
    #             if date not in dates_filter:
    #                 time_slot = EventSlot.objects.filter(event=events.first(),date=date)
    #                 for i in set(time_slot):
    #                     slot = Time.objects.exclude(time=str(i))
    #                     for j in set(slot):
    #                         t = (TimeSerializer(j).data).get('time')
    #                         available_slot.append(t)
    #                 data.append({"date":(EventDateSerializer(date).data).get('date'),
    #                              "available_slot":sorted(set(available_slot))
    #                              })
    #                 dates_filter[date] = True
    #         return Response(data)
    #     else:
    #         return Response("Event Not Found")
    def get(self,request,pk):
        if self.get_event(pk):
            events = Event.objects.filter(pk=pk)
            dates = events.first().eventdate_set.all()
            data = []
            slot = []
            available_slot=[]
            dates_filter = {}
            for date in dates:
                if date not in dates_filter:
                    time_slot = EventSlot.objects.filter(event=events.first(),date=date)
                    for i in set(time_slot):
                        slot = Time.objects.exclude(time=str(i))
                        for j in set(slot):
                            t = (TimeSerializer(j).data).get('time')
                            available_slot.append(t)
                    data.append({"date":(EventDateSerializer(date).data).get('date'),
                                 "available_slot":sorted(set(available_slot))
                                 })
                    dates_filter[date] = True
            return Response(data)
        else:
            return Response("Event Not Found")


    def post(self,request,pk):
        if self.get_event(pk):
            queryset = self.get_event(pk)
            for i in request.data.get('date'):
                if i not in self.get_event(pk).eventdate_set.all():
                    event_date = EventDate.objects.create(event=queryset,date=i)
                    event_date.save()
                    data = {
                        'date':event_date
                    }
                    print(data)
                    response = {
                        "SUCCESS":"Date Updated Success Fully"
                    }
                else:
                    response = {
                        'Exist':"Date Is Already Taken"
                    }
            return Response(response)
        else:
            return Response("Event Not Found")


    def put(self,request,pk):
        if self.get_event(pk):
            queryset = self.get_event(pk)
            Event.objects.filter(pk=pk).delete()
            serialize = EventSerializer(queryset,data=request.data)
            print("**************")
            if serialize.is_valid():
                serialize.save()
                return Response('Updated Success')
            else:
                return Response(serialize.errors)
        else:
            return Response("Event Not Found")


    def delete(self,request,pk):
        if self.get_event(pk):
            Event.objects.filter(pk=pk).delete()
            response = {
                "SUCCESS":"Deleted SuccessFully"
            }
            return Response(response)
        else:
            return Response("Event Not Found")

class EventSlotView(APIView):
    def get(self,request,date):
        time = EventSlot.objects.filter(Q(time__time__range=["00:00:00","05:00:00"]))
        data = {}
        date_1 = []
        time_1 = []
        serialize = EventSlotSerializer(time,many=True)
        for i in serialize.data:
            event_date = EventDateSerializer(EventDate.objects.get(pk=list(i.values())[1]))
            event_time = TimeSerializer(Time.objects.get(pk=list(i.values())[2]))
            date_1.append(event_date.data)
            time_1.append(event_time.data)
            data['date']=date_1
            data['time']=time_1
        print(data)
        return Response(data)