from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    user_rating = models.FloatField(verbose_name='Рейтинг автора', default=0)


class Category(models.Model):
    name = models.CharField(max_length=35, db_index=True, unique=True, verbose_name='Название категории')


class Post(models.Model):
    category_list = [
        (1, 'статья'),
        (2, 'новость')
    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    choice = models.PositiveSmallIntegerField(choices=category_list, verbose_name='Выбор')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    category = models.ManyToManyField(Category, through="PostCategory")
    header = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Текст поста')
    post_rating = models.FloatField(verbose_name='Рейтинг поста', default=0)

    def like(self):
        self.post_rating += 1
        pass

    def dislike(self):
        self.post_rating -= 1
        pass


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    comment_rating = models.FloatField(verbose_name='Рейтинг комментария')
