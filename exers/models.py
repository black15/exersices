from django.db import models
from django.contrib.auth.models import User
# Create your models here.
def namer(instance,filename):
    if instance.user:
        name = instance.user.username +'/'+filename
    else:
        name = 'other/'+filename
    return name
class Exer(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    ex_file = models.FileField(upload_to=namer,null=True)
    sou_file = models.FileField(upload_to=namer,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    likes = models.IntegerField(default=0)
    speciality = models.ForeignKey('Speciality',on_delete=models.CASCADE)
    solution = models.BooleanField(default=True)
    subject = models.ForeignKey('Subject',on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100,blank=True,null=True)
    def save(self, *args, **kwargs):
        self.subject_name=self.subject.name
        super(Exer,self).save(*args, **kwargs)
    class Meta:
        verbose_name = ("exer")
        verbose_name_plural = ("exers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Subject(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Speciality(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
