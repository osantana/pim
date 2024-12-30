from django.contrib import admin
from django.urls import path

from calendar import views  # <.>


urlpatterns = [
    path("hello-world/", views.hello, name="hello-world"),  # <.>
    path("admin/", admin.site.urls),
]
