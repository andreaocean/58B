from django.db import models


# lesson3
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
    
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"



class Post(models.Model):
    # lesson3
    image = models.ImageField(null=True, blank=True)
    
    # lesson2
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=1000, null=True, blank=True)
    rate = models.IntegerField(default=0)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,blank=True)
  
    # HW2
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return f"{self.title}"
