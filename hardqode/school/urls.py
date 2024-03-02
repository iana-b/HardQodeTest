from django.urls import path
from .views import ProductList

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),  # URL для списка продуктов
    # path('products/<int:product_id>/lessons/', LessonListView.as_view(), name='lesson-list'),  # URL для списка уроков по конкретному продукту
]

