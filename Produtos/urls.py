from django.urls import path
from .views import index, detail, admin, delete, create, update

urlpatterns = [
    path("", index, name='index'),
    path("produtos/detail/<int:id>", detail, name='detail'),
    path("produtos/admin/", admin, name='admin'),
    path("produtos/delete/<int:id>", delete, name='delete'),
    path("produtos/create/", create, name='create'),
    path("produtos/update/<int:id>", update, name='update'),
]
