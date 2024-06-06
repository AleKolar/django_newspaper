from NewsPaper.news.models import Post, Comment


def display_best_post_and_comments():
    best_post = Post.objects.filter(categories__name='Category1').order_by('-rating').first()
    best_post_preview = best_post.preview()

    print("Best Post:")
    print("Created at:", best_post.created_at)
    print("Author:", best_post.author.user.username)
    print("Rating:", best_post.rating)
    print("Title:", best_post.title)
    print("Preview:", best_post_preview)

    print("\nComments:")
    comments = Comment.objects.filter(post=best_post)
    for comment in comments:
        print("Created at:", comment.created_at)
        print("User:", comment.user.username)
        print("Rating:", comment.rating)
        print("Text:", comment.text)
        print("--------------")

display_best_post_and_comments = display_best_post_and_comments()