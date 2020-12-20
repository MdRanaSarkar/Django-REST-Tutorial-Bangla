from django.urls import path, include
from DjangoRESTApp.views import (Articlelist,
                                 ArticleDetails,
                                 Actileformview, GenericArticleView)

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('article', GenericArticleView, basename='article')

# articlelist, articledetails
urlpatterns = [
    # path('articlelistapi/', articlelist, name='articlelist'),
    # path('articledetails/<int:pk>/', articledetails, name='articledetails'),
    path('articlelist/', Articlelist.as_view(), name='Articlelist'),
    path('articlelist/<int:id>/', ArticleDetails.as_view(), name='ArticleDetails'),
    path('articleadd/', Actileformview, name='articleform'),
    #  path('generic/article/', GenericArticleView.as_view(), name='genericarticle'),
    # path('generic/article/<int:id>/', GenericArticleView.as_view(), name='genericarticle'),
    path('viewsets/', include(router.urls)),
    path('viewsets/<int:pk>/', include(router.urls))
]
