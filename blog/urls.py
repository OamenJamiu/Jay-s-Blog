from . import views


from django.urls import path

urlpattern = [
    path('edit_profile/', views.edit_profile, name="edit_profile"),
#     path('post_create/', views.post_create, name="post_create"),
#     path('blog/<int:id>/<slug:slug>/',  views.post_detail, name="post_detail"),
 ]
