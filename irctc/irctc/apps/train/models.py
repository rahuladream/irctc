from django.db import models
# Create your models here.

NATURAL_NUMBER = (
    (1, ('1')),
    (2, ('2'))
)

class TrainStation(models.Model):
    code = models.CharField(max_length=5, null=False)
    name = models.CharField(max_length=100)
    geolocation = models.JSONField()

    class Meta:
        verbose_name = 'Station'

    def __str__(self):
        return self.code


class TrainWeek(models.Model):
    short_name = models.CharField(max_length=2)
    long_name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Running Week'

    def __str__(self):
        return self.short_name


class TrainSeater(models.Model):
    short_name = models.CharField(max_length=10)
    reservation_charge = models.FloatField()

    class Meta:
        verbose_name = 'Seater'

    def __str__(self):
        return self.short_name


class Train(models.Model):
    number = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=100)
    source = models.ForeignKey(TrainStation, related_name='train_destination', null=True, on_delete=models.SET_NULL)
    destination = models.ForeignKey(TrainStation, related_name='train_source', null=True, on_delete=models.SET_NULL)
    run_days = models.ManyToManyField(TrainWeek)
    source_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(default=True)
    max_carry_passenger = models.SmallIntegerField()
    reserved_vip_seat = models.SmallIntegerField()
    is_superfast = models.BooleanField(default=False)
    available_seater = models.ManyToManyField(TrainSeater)

    class Meta:
        verbose_name = 'Train'

    def __str__(self):
        return self.number


class TrainRoute(models.Model):
    train = models.ForeignKey(Train, related_name='train_route_history', null=True, on_delete=models.SET_NULL)
    source = models.ForeignKey(TrainStation, related_name='train_route_source', null=True, on_delete=models.SET_NULL)
    destination = models.ForeignKey(TrainStation, related_name='train_route_destination', null=True, on_delete=models.SET_NULL)
    source_start_time = models.TimeField()
    destination_end_time = models.TimeField()
    halt = models.IntegerField(help_text="Halt in second")
    distance_between = models.FloatField(max_length=5, help_text="Distance between source & Destination")
    ranking = models.SmallIntegerField(choices=NATURAL_NUMBER)

    class Meta:
        verbose_name = 'Running Route'

    def __str__(self):
        try:
            return '{} - {}'.format(self.source.code, self.destination.code)
        except:
            return self.distance_between

