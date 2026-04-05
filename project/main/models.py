from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    is_landmark = models.BooleanField(default=False, verbose_name="Famous Landmark (Show on load)")

    def __str__(self):
        return self.name

class PathEdge(models.Model):
    node_a = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='paths_from')
    node_b = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='paths_to')
    weight_distance = models.FloatField(help_text="Distance in meters")

    def __str__(self):
        return f"{self.node_a.name} <-> {self.node_b.name}"