Здравствуйте! Сделано согласно задания D5.9
Для Вашего и моего удобства, прямо здесь напишу консольную часть:
1.	Создание пользователей:

from news.models import Author, Post, Category, Comment

from django.contrib.auth.models import User 

user1 = User.objects.create_user('user1') 

user2 = User.objects.create_user('user2') 

2.	Создание объектов модели Author, связанных с пользователями:

author1 = Author.objects.create(user=user1)

author2 = Author.objects.create(user=user2) 

3.	Добавление категорий в модель Category:

Category.objects.create(name='Category1') 

Category.objects.create(name='Category2') 

Category.objects.create(name='Category3') 

Category.objects.create(name='Category4') 

4.	Добавление статей и новости с категориями:

categories = Category.objects.all()

post1 = Post.objects.create(author=author1, title='Post 1', content='Content 1')

post1.categories.add(categories[0], categories[1]) 

post2 = Post.objects.create(author=author2, title='Post 2', content='Content 2')

post2.categories.add(categories[2], categories[3]) 

news1 = Post.objects.create(author=author1, title='News 1', content='News content') 

news1.categories.add(categories[0], categories[2]) 

5.	Создание комментариев к объектам модели Post:

comment1 = Comment.objects.create(post=post1, user=user1, author_id=1, text='Comment 1') 

comment2 = Comment.objects.create(post=post2, user=user2, author_id=2, text ='Comment 2') 

comment3 = Comment.objects.create(post=news1, user=user1, author_id=1, text ='Comment 3')

comment4 = Comment.objects.create(post=news1, user=user2, author_id=2, text ='Comment 4') 

6.	Применение функций like() и dislike() к объектам и обновление рейтингов:

post1.like()

post1.like() 

post2.dislike() 

comment1.like() 

comment2.like() 

comment3.dislike() 

author1.update_rating() 

author2.update_rating() 

7.	Вывод username и рейтинга лучшего пользователя:

best_user = Author.objects.all().order_by('-rating').first() 

print(best_user.user, best_user.rating) 

8.	Вывод информации о лучшей статье:

best_post = Post.objects.filter(categories__name='Category1').order_by('-rating').first() 

print(best_post.author.user.username, best_post.created_at, best_post.rating, best_post.title, best_post.content[:50]) 

Просто доп.функция, потому-что я запутался(просто с ней, уже, «закоммитино» было:

 best_post_func = Post.display_best_post(Post)

9.	Вывод всех комментариев к лучшей статье:

best_post_comments = Comment.objects.filter(post=best_post) 

for comment in best_post_comments:

       print('Date:',comment.created_at, ';', 'Comment_usename:', comment.user.username, ';',   'Commentrating:',comment.rating, ';', 'Commentcontent:',comment.text)
