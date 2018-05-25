from django.urls import path, include

from . import views

# namespace for urls
app_name = 'website'

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('', views.IndexView.as_view(), name='index'),
    path('book/add', views.add, name='add'),
    path('book/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('edit/<int:book_id>', views.edit, name='edit'),
    path('book/<int:book_id>/delete', views.delete, name='delete'),
    # path('auth/', include('django.contrib.auth.urls'))
]
