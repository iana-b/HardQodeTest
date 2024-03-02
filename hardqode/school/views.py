from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Product, Lesson
from .serializers import ProductSerializer, LessonSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


# class LessonListView(generics.ListAPIView):
#     serializer_class = LessonSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#         product_id = self.kwargs['product_id']
#         return Lesson.objects.filter(product_id=product_id)

