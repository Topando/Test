from django.urls import path, re_path, include
from django.views.decorators.cache import cache_page

from Test import settings
from .views import *

urlpatterns = [
    path('', ManHome.as_view(), name='home'),
    path("about/", about, name="about"),
    path("contact/", ContactFormView.as_view(), name="contact"),
    path("addpage/", AddPage.as_view(), name="add_page"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("post/<slug:post_slug>/", ShowPost.as_view(), name="post"),
    path("cat/<slug:cat_slug>/", ManCategory.as_view(), name="category"),
    path('captcha/', include('captcha.urls')),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        # ...
        path("__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns