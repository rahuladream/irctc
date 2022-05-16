from django.contrib import admin
from .models import *
from django.contrib.admin.options import TabularInline


@admin.register(TrainStation)
class TrainStationModelAdmin(admin.ModelAdmin):
    fields = ('code', 'name', 'geolocation')


@admin.register(TrainWeek)
class TrainWeekModelAdmin(admin.ModelAdmin):
    fields = ('short_name', 'long_name')


class TrainRouteAdminInline(TabularInline):
    extra = 5
    model = TrainRoute


@admin.register(Train)
class TrainModelAdmin(admin.ModelAdmin):
    inlines = (TrainRouteAdminInline, )
    fields = ('number', 'name', 'source', 'destination', 'run_days', 'source_time', 'end_time', 'is_active', 'max_carry_passenger', 'reserved_vip_seat', 'is_superfast', 'available_seater')


@admin.register(TrainSeater)
class TrainWeekModelAdmin(admin.ModelAdmin):
    fields = ('short_name', 'reservation_charge')
