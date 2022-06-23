from django.db import models


class VegetableType(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Vegetable(models.Model):
    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=35, verbose_name="Food")
    description = models.TextField(null=True, blank=True)

    environment = models.TextChoices("Environment", "INDOOR OUTDOOR")
    season = models.TextChoices("Season", "SUMMER FALL WINTER SPRING")

    veg_type = models.ForeignKey(
        VegetableType, null=False, blank=False, on_delete=models.CASCADE
    )

    compost = models.CharField(max_length=100)
    harvest = models.CharField(max_length=100)
    watering = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
