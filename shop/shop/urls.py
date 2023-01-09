from django.urls import path
from .import views
from django.contrib.auth import views as auth_views 
urlpatterns = [
    path('',views.home,name="home"),
    path('about',views.about.as_view(),name="about"),
    path('register',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('cart',views.cart_page,name="cart"),
    path('fav',views.fav_page,name="fav"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('remove_fav/<str:cid>',views.remove_fav,name="remove_fav"),
    path('collections',views.collections,name="collections"),
    path('contacts',views.contact,name="contacts"),
    path('collections/<str:name>',views.collectionsview,name="collections"),
    path('collections/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('addtocart',views.add_to_cart,name="addtocart"),
    path('favourite',views.favourite_page,name="favourite"),

    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]