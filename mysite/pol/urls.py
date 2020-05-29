from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'pol'

urlpatterns = [
    # ex: /polls/
    path('', views.index_view, name='mhome'),
    path('upload/', views.upload, name='upload'),
    path('books/', views.book_list, name='book_list'),
    path('books/upload/', views.Upload_book, name='upload_book'),
    path('main/', views.home_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('register/', views.register_view, name='register_url'),
    path('login/', LoginView.as_view(), name="login_urls" ),
    path('logout/', LogoutView.as_view(next_page='pol:mhome'),name="logout_url"),
    path('resources/', views.Resource_View, name='resource'),
    path('profile/', views.Profile_View, name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)