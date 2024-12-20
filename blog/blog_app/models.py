from tabnanny import verbose
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class HomeSlider(models.Model):
    photo = models.ImageField(
        upload_to='homeslider/%Y/%m/%d/',
        verbose_name='Фото',
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок слайда',
        help_text='Внимательнее'

    )
    text = models.TextField(
        verbose_name='Текст',

    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class Todo(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Название',
        unique=True,
    )
    short_description = models.TextField(
        verbose_name='Краткое описание',
    )
    full_description = models.TextField(
        verbose_name='Полное описание',
    )
    preview = models.ImageField(
        upload_to='todo/%Y/%m/%d/',
        null=True,
        blank=True,
        verbose_name='Фото'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    views = models.IntegerField(
        default=0,
        verbose_name='Просмотры'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


def post_gallery_image_path(instance, filename):
    return f'post-{instance.post.id}/gallery/{filename}'


class TodoGallery(models.Model):
    post = models.ForeignKey(
        Todo,
        on_delete=models.CASCADE,
        verbose_name='Пост'
    )
    image = models.ImageField(
        upload_to=post_gallery_image_path,
        verbose_name='Фото'
    )


class Comment(models.Model):
    post = models.ForeignKey(Todo, on_delete=models.CASCADE, verbose_name='Пост')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Пост-{self.post}: {self.author}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
