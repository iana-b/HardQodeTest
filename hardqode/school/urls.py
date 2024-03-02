from django.urls import path
from .views import ProductList, LessonList

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:product_id>/', LessonList.as_view(), name='lesson-list'),
]
