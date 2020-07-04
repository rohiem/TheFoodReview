from django.conf import settings
from django.urls import path, include
from .views import restaurantdishes,restaurants,reviewdetail,home,videos,reviews,videodetail,vlogs,vlogdetail,blogs ,blogdetail,recipes,recipedetail,modelCreateView,models,modeldetail
# , MovieAdd
# , Profileview

app_name = 'review'
urlpatterns = [
    path('',home , name="home"),
    path('restaurants',restaurants , name="restaurants"),
    path('restaurants/<int:id>',restaurantdishes , name="restaurantdishes"),
    path('reviews',reviews , name="reviews"),
    path('reviews/<int:id>',reviewdetail , name="reviewdetail"),
    path('videos',videos , name="videos"),
    path('videos/<int:id>',videodetail , name="videodetail"),
    path('vlogs',vlogs , name="vlogs"),
    path('vlogs/<int:id>',vlogdetail , name="vlogdetail"),
    path('blogs',blogs , name="blogs"),
    path('blogs/<int:id>',blogdetail , name="blogdetail"),
    path('recipes',recipes , name="recipes"),
    path('recipes/<int:id>',recipedetail , name="recipedetail"),
    path('create',modelCreateView.as_view() , name="create"),
    path('models',models , name="models"),
    path('models/<int:id>',modeldetail , name="modeldetail"),
]
