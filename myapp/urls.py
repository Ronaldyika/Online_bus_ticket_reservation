from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= 'index'),
    path('zilo/payticket', views.payticket, name= 'payticket'),

    path('zilo/blog', views.blog, name= 'blog'),
    path('zilo/blog/create_blog', views.create_blog, name= 'create_blog'),
    path('zilo/blog_delete<str:pk>', views.blog_delete, name= 'blog_delete'),
    path('zilo/blog_update<str:pk>', views.blog_update, name= 'blog_update'),
    path('zilo/blog_content<str:pk>', views.blog_content, name= 'blog_content'),




    path('zilo/customer_registration', views.customer_registration, name = 'customer_registration'),


    path('zilo/contact', views.contact, name= 'contact'),


    path('zilo/choose', views.choose, name = 'choose'),

    path('zilo/signin', views.signin, name= 'sigin'),
    path('zilo/signup', views.signup, name= 'signup'),
]
