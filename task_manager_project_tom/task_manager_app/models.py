from django.db import models
class Category(models.Model):
    name = models.CharField(max=1000)

    def __str__(self):
        return self.name
    

class Task(models.Model):
        PRIORITY_CHOICES = [
             ("high", "High")
             ("medium", "Medium")
             ("low", "Low")

        ]
        title = models.CharField(max_length=200)
        description = models.TextField()
        due_date = models.DateField()
        priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
        catergory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
        completed = models.BooleanField(default=False)

        def __str__(self):
             return self.title
