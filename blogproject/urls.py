
from django.contrib import admin
from django.urls import path, include
from blog.feeds import AllPostsRssFeed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('comments.urls')),

    # 记得在顶部引入 AllPostsRssFeed
    path('all/rss/', AllPostsRssFeed(), name='rss'),
]
