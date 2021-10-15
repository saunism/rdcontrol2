from django.urls import path
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns=[
    path('',views.main_page,name="main_page"),
    path('write_article',views.write_article,name="write_article"),
    path('registration',views.registration,name="registration"),
    path('sign_in',views.auth,name="auth"),
    path('accounts/' ,include('django.contrib.auth.urls')),
    path('article/<int:option>',views.show_article),
    path('posts/article/<int:option>',views.show_article),
    path('posts/<str:category>',views.article_list),
    path('other',views.other)
]
