from django.db import models


class Soft(models.Model):

    soft_skills = models.CharField(max_length=50, verbose_name='Софтскилл')

    def __str__(self):
        return self.soft_skills

    class Meta:
        verbose_name = 'СофтСкилл'
        verbose_name_plural = 'СофтСкиллы'


class Hard(models.Model):

    hard_skills = models.CharField(max_length=50, verbose_name='Хардскилл')

    def __str__(self):
        return self.hard_skills

    class Meta:
        verbose_name = 'ХардСкилл'
        verbose_name_plural = 'ХардСкиллы'


class Work(models.Model):

    place = models.CharField(max_length=50, verbose_name='Место работы')
    position = models.CharField(max_length=50, verbose_name='Должность')
    data_start = models.DateField(verbose_name='Начало работы')
    data_finish = models.DateField(verbose_name='Окончание работы', null=True, blank=True)
    tasks = models.TextField(verbose_name='Задачи')

    def __str__(self):
        return self.place

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
        ordering = ['data_start']


class Aducation(models.Model):
    intitute = models.CharField(max_length=50, verbose_name='Место учебы')
    position = models.CharField(max_length=50, verbose_name='Специальность')
    data_start = models.DateField(verbose_name='Начало учебы')
    data_finish = models.DateField(verbose_name='Окончание учебы', null=True, blank=True)
    progress = models.TextField(verbose_name='Успехи')

    def __str__(self):
        return self.intitute

    class Meta:
        verbose_name = 'Университет'
        verbose_name_plural = 'Университеты'
        ordering = ['data_start']