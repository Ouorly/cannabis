from django.urls import path
from cannabis import views

urlpatterns = [
    path('search-form/', views.CannabisView.as_view()),
    path('', views.CannabisView.as_view(), name='cannabis'),
    path('post/<int:pk>/', views.PostViews.as_view(), name="post_single")

]
