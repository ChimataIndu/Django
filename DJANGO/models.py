from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class MyModel(models.Model):
    name = models.CharField(max_length=100)


@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal received for: {instance.name}")
    time.sleep(5)  
    print("Signal handler finished executing")


if __name__ == "__main__":
    obj = MyModel.objects.create(name="Test")
    print("Object created")
