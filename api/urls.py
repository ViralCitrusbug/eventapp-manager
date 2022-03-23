from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.EventList.as_view(),name="home"),
    path('event/<pk>',views.EventDetail.as_view(),name="event-detail"),
    path('slot/<str:date>',views.EventSlotView.as_view(),name='event-slot')
]