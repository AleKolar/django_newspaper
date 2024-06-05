from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = sum([post.rating * 3 for post in self.post_set.all()])
        comment_rating = sum([comment.rating for comment in Comment.objects.filter(author=self)])
        post_comment_rating = sum([comment.rating for comment in Comment.objects.filter(post__author=self)])

        self.rating = post_rating + comment_rating + post_comment_rating
        self.save()

    def best_user(self):
        best_author = Author.objects.all().order_by('-rating').first()
        best_user = best_author.user
        return best_user.username, best_author.rating


    def best_post(self):
        best_post = Post.objects.filter(categories__name='Category1').order_by('-rating').first()
        best_post_content = best_post.content[:50]
        return best_post.author.user.username, best_post.created_at, best_post.rating, best_post.title, best_post_content


    def best_post_comments(self):
        best_post_comments = Comment.objects.filter(post=self.best_post)
        for comment in best_post_comments:
            return comment.created_at, comment.user.username, comment.rating, comment.content

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=True)
    POST_TYPES = (
        ('article', 'Article'),
        ('news', 'News'),
    )
    post_type = models.CharField(max_length=10, choices=POST_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', through='PostCategory')
    title = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.content[:124] + '...'

class PostCategory(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)


    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
