from django.urls import path 
from . import views

urlpatterns = [
	path('signin/', views.signin_view, name="signin" ),
	path('signup/', views.signup_view, name="signup" ),
	path('logout/', views.logout_view, name="logout" ),
	path('profile/', views.profile,    name="profile"),
	path('perkembangan/', views.insert_perkembangan, name="perkembangan"),
]