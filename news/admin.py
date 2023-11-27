from django.contrib import admin
from .models import Author, Post, PostCategory, Comment, Category, CategorySubscribers


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user_author', 'user_rating')
    list_filter = ('user_author__username', 'user_rating')


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'post_author', 'post_type', 'post_time', 'post_name',
        'post_rating', 'post_text'
    )
    list_filter = (
        'post_author__user_author__username', 'post_type', 'post_time',
        'post_category__category_name', 'post_name', 'post_rating'
    )
    search_fields = ('post_author', 'post_type', 'post_text',
                     'post_category__category_name', 'post_name'
                     )


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PostCategory._meta.get_fields()]
    list_filter = ('post', 'category')
    search_fields = ('post__post_name', 'category__category_name')


class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.get_fields()]
    list_filter = (
        'comment_post', 'comment_user', 'comment_time', 'comment_rating'
    )
    search_fields = ('comment_post__post_name', 'comment_text')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    list_filter = ('category_name', 'subscribers')


class CategorySubscribersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CategorySubscribers._meta.get_fields()]
    list_filter = ('subs_category', 'subs_user')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategorySubscribers, CategorySubscribersAdmin)

