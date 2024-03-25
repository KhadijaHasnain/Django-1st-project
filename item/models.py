from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_item_id_generator

class Item(models.Model):
    DEVICE_TYPE_CHOICES = [
        ('Mobile Device', 'Mobile Device'),
        ('Non-Portable PC', 'Non-Portable PC'),
        ('Laptop', 'Laptop'),
        ('Standalone Headset', 'Standalone Headset'),
    ]

    CPU_CHOICES = [
        ('I7-7700HQ', 'I7-7700HQ'),
        ('I7-8750H', 'I7-8750H'),
        ('M2 10C', 'M2 10C'),
        ('BCM2711C0', 'BCM2711C0'),
        ('6-Core Intel Core I5', '6-Core Intel Core I5'),
    ]

    GPU_CHOICES = [
        ('GTX 1070', 'GTX 1070'),
        ('RTX 2070', 'RTX 2070'),
    ]

    RAM_CHOICES = [
        ('32', '32'),
        ('16', '16'),
    ]

    name = models.CharField(max_length=100, null=True, verbose_name="Device name")
    type = models.CharField(max_length=100, null=True, choices=DEVICE_TYPE_CHOICES, verbose_name="Device type")
    serial = models.CharField(max_length=100, null=True, verbose_name="Device Serial")
    cpu = models.CharField(max_length=100, null=True, choices=CPU_CHOICES, verbose_name="CPU")
    gpu = models.CharField(max_length=100, null=True, choices=GPU_CHOICES, verbose_name="GPU")
    ram = models.CharField(max_length=100, null=True, choices=RAM_CHOICES, verbose_name="RAM")
    item_id = models.CharField(max_length=10, verbose_name="Item ID",
                               primary_key=True, null=False)

    def __str__(self):
        return self.item_id

def pre_save_create_item_id(sender, instance, *args, **kwargs):
    if not instance.item_id:
        instance.item_id = unique_item_id_generator(instance)

pre_save.connect(pre_save_create_item_id, sender=Item)
