from django.db import models

# Create your models here.
 
# Create your models here.
PRIORITY = (('danger', 'high'), ('info', 'normal'), ('success', 'low'))
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True, null=True,)
    priority = models.CharField(
      max_length = 50,
      choices = PRIORITY
    )
    duedate = models.DateField()
    
    category = models.CharField(max_length=50)

    color = models.CharField(max_length=20)

    def __str__(self):
      return self.title