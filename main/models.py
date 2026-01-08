from django.db import models
from django.dispatch import receiver

# Driver model linked to Django's built-in User model
class Driver(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

@receiver(models.signals.post_save, sender='auth.User')
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Driver.objects.create(user=instance)
    else:
        instance.driver.save()


class Trip(models.Model):
    current_location = models.CharField(max_length=255)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    estimated_cycle_used = models.IntegerField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trip from {self.pickup_location} to {self.dropoff_location}"

class Actvity(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100, choices=[('ONDUTY', 'On Duty'), ('OFFDUTY', 'Off Duty'), ('DRIVING', 'Driving'), ('SLEEPER', 'Sleeper')])
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Activity {self.activity_type} for Driver ID {self.driver.id}"