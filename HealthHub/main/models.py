from django.db import models

class EatingList(models.Model):
    username = models.CharField('Пользователь', max_length=50)
    date = models.DateField('Дата')
    breakfast = models.CharField('Завтрак', max_length=100)
    lunch = models.CharField('Обед', max_length=100)
    dinner = models.CharField('Ужин', max_length=100)
    snack = models.CharField('Перекусы', max_length=100)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Список приемов пищи'
        verbose_name_plural = 'Списки приемов пищи'
            
class UserData(models.Model):
    name = models.CharField('Имя пользователя', max_length=50)
    gender = models.CharField('Пол', max_length=50 )
    birth_date = models.DateField('Дата рождения', max_length=50)
    email = models.CharField('Адрес почты', max_length=50)
    height = models.IntegerField('Рост', max_length=50)
    weight = models.FloatField('Вес', max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
