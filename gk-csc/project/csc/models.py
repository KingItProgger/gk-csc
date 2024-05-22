from django.db import models

from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse


class House(models.Model):
    house=models.IntegerField(verbose_name='номер дома',validators=[MinValueValidator(0)],unique=True)
    floors=models.IntegerField(verbose_name='количество этажей',validators=[MinValueValidator(0)],)
    padics=models.IntegerField(verbose_name='количество подьездов',validators=[MinValueValidator(0)],)
    flatss=models.IntegerField(verbose_name='количество квартир',validators=[MinValueValidator(0)],)
    img=models.ImageField(null=True,verbose_name='фото дома',upload_to='images/')
    year=models.IntegerField(verbose_name='год сдачи',validators=[MinValueValidator(2015)],)

    class Meta:
        verbose_name='дом'
        verbose_name_plural = 'дома'
        ordering=['year']
    def __str__(self):
        return f"{self.house}"



class News(models.Model):

    title=models.CharField(max_length=64,verbose_name='название',unique=True)
    text=models.TextField(verbose_name='текст')
    img=models.ImageField(null=True,verbose_name='картинка',upload_to='images/')
    datetime=models.DateTimeField(verbose_name='дата публикации', auto_now_add=True)
    class Meta:
        verbose_name='новость'
        verbose_name_plural = 'новости'
        ordering=['datetime']
    def __str__(self):
        return f"{self.title} \n {self.text[:140]} \n {self.datetime}"

class Flat(models.Model):
    house=models.ForeignKey(to='House',verbose_name='литер', on_delete=models.CASCADE, related_name='flats')
    square=models.FloatField(verbose_name='площадь',validators=[MinValueValidator(20)])
    rooms=models.ForeignKey(to='Room', on_delete=models.PROTECT, verbose_name='количество комнат')
    amount=models.IntegerField(verbose_name='квартир в продаже',validators=[MinValueValidator(0)])
    plan=models.ImageField(null=True,verbose_name='план-схема',upload_to='images/')
    price=models.FloatField(verbose_name='цена',default=0, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name='квартира'
        verbose_name_plural = 'квартиры'
        ordering=['square']


    def price_for_metr_calc(self):
        self.price_for_metr=self.price/self.square
        self.save()
        return self.price_for_metr


class Recall(models.Model):
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=20)
    message=models.TextField()

class Review(models.Model):
    username=models.CharField(max_length=32, default='Гость', verbose_name='имя пользователя',blank=True)
    message=models.TextField(verbose_name='отзыв')
    mark=models.IntegerField(verbose_name='оценка', validators=[MinValueValidator(1),MaxValueValidator(5)])
    img=models.ImageField(verbose_name='картинка звезд',upload_to='images/')
    datetime=models.DateTimeField(blank=True,auto_now_add=True,null=True)

    class Meta:
        verbose_name='отзыв'
        verbose_name_plural = 'отзывы'

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

class Room(models.Model):
    room=models.IntegerField(verbose_name='количество комнат',unique=True,validators=[MinValueValidator(1)])
    class Meta:
        verbose_name='комната'
        verbose_name_plural = 'комнаты'
    def __str__(self):
        return f"{self.room}"


