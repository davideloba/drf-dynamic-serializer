from drf_eager_fields.views import EagerFieldsAPIView
from rest_framework import generics

from .models import Article, Country, Customer
from .serializers.article_serializer import ArticleSerializer, LazyArticleSerializer
from .serializers.customer_serializer import CustomerSerializer
from .serializers.data_serializers import DataArticleSerializer
from .serializers.country_serializer import MixedCountrySerializer


class ArticleList(generics.ListCreateAPIView, EagerFieldsAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    serializer_extra = "orders.customer, customer.country"
    # serializer_fields =
    # serializer_exclude =


class ArticleDetail(generics.RetrieveAPIView, EagerFieldsAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    serializer_extra = "orders.customer, customer.country"
    # serializer_fields =
    # serializer_exclude_fields =


class LazyArticleList(generics.ListCreateAPIView, EagerFieldsAPIView):
    queryset = Article.objects.all()
    serializer_class = LazyArticleSerializer


class CustomerList(generics.ListCreateAPIView, EagerFieldsAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveAPIView, EagerFieldsAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class LazyCustomerDetail(generics.RetrieveAPIView, EagerFieldsAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class DataArticlesList(generics.ListAPIView, EagerFieldsAPIView):
    queryset = Article.objects.all()
    serializer_class = DataArticleSerializer
    serializer_extra = "customer.countries.region, last_10_orders"


class MixedCountryList(generics.ListAPIView, EagerFieldsAPIView):
    queryset = Country.objects.all()
    serializer_class = MixedCountrySerializer
