from django.db import models
# this thing above is the base class all models are built upon

# import something else
from django.contrib.auth import get_user_model


class Snack(models.Model):
	# these are like the columns of our table
	name = models.CharField(max_length=256)
	# each thing will have a name and a reviewer
	description = models.TextField(blank=True)
	# on delete will decide what happens if reviewer is deleted
	purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

	def __str__(self):
		return self.name
