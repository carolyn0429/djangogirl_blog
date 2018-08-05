from django.db import models
from django.utils import timezone


# Create your models here.
# it is an object. Post is model name. models.Model is telling Django this is a model and can be saved to database.
class Post(models.Model):
    # a link to another model
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # define limited number of character as text
    title = models.CharField(max_length=200)
    # define long text
    text = models.TextField()
    # define date and time
    created_date = models.DateTimeField(blank=True, null=True)

    # we need to indent for method inside the class, otherwise the method won't belong to the class.
    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title