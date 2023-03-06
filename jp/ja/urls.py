from django.urls import path

from . import views





urlpatterns = [
    path('', views.HomeView.as_view(),name="home"),
    path("about/", views.aboutview.as_view(), name="about"),
    path("contact/", views.Contactus.as_view(),name="contact"),
    path("property/" ,views.Property.as_view(),name="properties"),
    path("pricing/",views.PriceView.as_view(),name="pricing"),
    path("userpage/",views.UserPage.as_view(),name="user"),
    path("recomonded/",views.Recommond.as_view(),name="recomonded"),

]