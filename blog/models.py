from django.db import models


class Bosh(models.Model):
    nomi=models.CharField(max_length=50)
    text=models.TextField()
    rasm=models.ImageField()
    def __str__(self):
        return self.text

class Text(models.Model):
    name=models.CharField(max_length=50)
    haqida=models.TextField(blank=False)
    def __str__(self):
        return self.name

class Konsultatsiya(models.Model):
    ism=models.CharField(max_length=100)
    telefon=models.CharField(max_length=20)
    savol=models.TextField()
    vaqt=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.ism

class Yutuqlar(models.Model):
    soni=models.IntegerField()
    malumot=models.CharField(max_length=40)
    def __str__(self):
        return self.malumot

class Negakambrij(models.Model):
    name=models.CharField(max_length=50)
    Text=models.TextField()
    def __str__(self):
        return self.name

class Kurslarimiz(models.Model):
    name=models.CharField(max_length=20)
    haqida=models.TextField(blank=False)
    def __str__(self):
        return self.name

class Text2(models.Model):
    name=models.CharField(max_length=50)
    haqida=models.TextField(blank=False)
    def __str__(self):
        return self.name

class Konsultatsiya2(models.Model):
    ism=models.CharField(max_length=100)
    telefon=models.CharField(max_length=20)
    savol=models.TextField()
    vaqt=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.ism

class Teacher(models.Model):
    ielts_ball = models.DecimalField(max_digits=3, decimal_places=1)
    tajriba_yil = models.PositiveIntegerField()
    oquvchilar_soni = models.PositiveIntegerField()
    tavsif = models.TextField()
    rasm = models.ImageField()
    def __str__(self):
        return str(self.ielts_ball)

class Natija(models.Model):
    name=models.CharField(max_length=50)
    text=models.TextField(blank=True)
    rasmi=models.ImageField()
    def __str__(self):
        return self.name

class Artifaktlar(models.Model):
    savol=models.CharField(max_length=500)
    javob=models.TextField()
    def __str__(self):
        return self.savol
