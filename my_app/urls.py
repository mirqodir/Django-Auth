from django.urls import path
from .views import IndexPageView,NwewPageView


urlpatterns = [

				path('',IndexPageView.as_view(),name='index'),
				path('new/',NwewPageView.as_view(),name='new'),
			

]