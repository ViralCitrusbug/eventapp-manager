from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200)
    organizeer = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    post_code = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class EventDate(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self) -> str:
        return str(self.date)



class Time(models.Model):
    time = models.TimeField(blank=True,null=True,db_column='t')
    mod = models.IntegerField(blank=True,null=True)

    def __str__(self) -> str:
        return str(self.time)
    
    class Meta:
        db_table = 'cv_alloc_times'
        ordering =  ('time',)


class EventSlot(models.Model):
    date = models.ForeignKey(EventDate,on_delete=models.CASCADE)
    time = models.ForeignKey(Time,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.time.time)
# event_data:[
# {"date":10-11-2021, "start_slot":"01:00", "end_slot":"06:00"},
# {"date":11-11-2021, "start_slot":"05:00", "end_slot":"12:00"}, 
# {"date":10-11-2021, "start_slot":"13:00", "end_slot":"18:00"}
# ]