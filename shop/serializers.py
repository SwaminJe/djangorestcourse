from rest_framework.serializers import ModelSerializer

from shop.models import Article, Category, Product

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name']
    

class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category']

class ArticleSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'product']