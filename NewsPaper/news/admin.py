
from django.contrib import admin

# импортируем наши модели
from .models import Post, Comment, Category, Author
# и зарегистрируем их
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Author)
