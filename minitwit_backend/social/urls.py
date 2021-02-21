from django.urls import path
from social.views import FollowView


urlpatterns = [
	path('follow/', FollowView.as_view(), name='follow')
]
