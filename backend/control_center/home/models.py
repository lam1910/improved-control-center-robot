from django.db import models

# Create your models here.
robot_loc = [
    ('vn', 'Vietnam'),
    ('swe', 'Sweden'),
]

order_status = [
    ('incomplete', 'Incomplete'),
    ('completed', 'Completed'),
]

lvl = [
    (1, 'Level 1'),
    (2, 'Level 2')
]
class Order(models.Model):
    robot = models.CharField(max_length=3, choices=robot_loc)
    level = models.IntegerField(choices=lvl)
    status = models.CharField(max_length=12, choices=order_status)