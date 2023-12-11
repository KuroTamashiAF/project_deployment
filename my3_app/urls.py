from django.urls import path
from .views import view_function, HelloView, year_posts, Monthposts, post_detail, my_view, TempleIf, TempleFor
from .views import index, about, author_posts, post_full

urlpatterns = [
    path("fuction/", view_function, name="fuction"),
    path("class/", HelloView.as_view(), name="class"),
    path("posts/<int:year>/", year_posts, name="year_posts"),
    path("posts/<int:year>/<int:month>/", Monthposts.as_view(), name="year_posts"),
    path("posts/<int:year>/<int:month>/<slug:slug>/", post_detail, name="post_detail"),
    path("temp/<str:name>/", my_view, name="my_view"),
    path("tempif/", TempleIf.as_view(), name="view_if"),
    path("tempfor/", TempleFor.as_view(), name="view_for"),
    path("index/", index, name="index"),
    path("about/", about, name="about"),
    path("author/<int:author_id>/", author_posts, name="author_posts"),
    path("post/<int:post_id>/", post_full, name="post_full"),

]
