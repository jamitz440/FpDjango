from django.db import models
from django.core.validators import FileExtensionValidator
from PIL import Image
import os
import colorsys

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    etsy_link = models.CharField(max_length=1000, default="https://www.etsy.com/shop/FitzPrintsgb")
    description = models.TextField()
    print_time = models.FloatField()
    weight = models.FloatField()
    cost_to_print = models.FloatField()
    filament_used = models.ManyToManyField('Filament', blank=True)
    profit = models.FloatField(blank=True)
    colour_h = models.CharField(max_length=100, blank=True)
    colour_s = models.CharField(max_length=100, blank=True)
    colour_l = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to='files/', validators=[FileExtensionValidator(allowed_extensions=['zip'])], blank=True, null=True)

    def __str__(self):
        return self.name
    
    def average_color(self, image_path, border_percent=12):
        image = Image.open(image_path).convert('RGB')
        width, height = image.size

        # Calculate the border size to exclude
        border_width = int(width * border_percent / 100)
        border_height = int(height * border_percent / 100)

        # Crop the image to exclude the border
        cropped_image = image.crop((border_width, border_height, width - border_width, height - border_height))

        # Get pixel data
        pixels = cropped_image.getdata()

        # Calculate the average color
        r_total, g_total, b_total = 0, 0, 0
        num_pixels = cropped_image.width * cropped_image.height
        for r, g, b in pixels:
            r_total += r
            g_total += g
            b_total += b

        avg_r = r_total / num_pixels / 225
        avg_g = g_total / num_pixels / 225
        avg_b = b_total / num_pixels / 225
        h, l, s = colorsys.rgb_to_hls(avg_r, avg_g, avg_b)

        self.colour_h = h * 360
        self.colour_s = s * 100
        self.colour_l = l * 100
        
    
    def save(self, *args, **kwargs):
        self.profit = self.price - self.cost_to_print
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        image.thumbnail((1000, 1000))
        image.save(self.image.path)
        self.average_color(self.image.path)
        super().save(update_fields=['colour_h', 'colour_s', 'colour_l'])



class Filament(models.Model):

    manufacturer = models.CharField(max_length=100)
    price = models.FloatField()
    CHOICES = (
        ('PLA', 'PLA'),
        ('ABS', 'ABS'),
        ('PETG', 'PETG'),
        ('TPU', 'TPU'),
        ('Nylon', 'Nylon'),
        ('ASA', 'ASA'),
        ('PC', 'PC'),
        ('Carbon Fibre', 'Carbon Fibre'),
    )
    material = models.CharField(max_length=100, choices=CHOICES)
    type = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    hex = models.CharField(max_length=100 , blank=True)

    def __str__(self):
        return self.manufacturer + " " + self.material + " " + self.type + " " + self.colour + " " + self.hex