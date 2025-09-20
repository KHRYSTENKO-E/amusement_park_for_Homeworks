from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_administrator_main_page, name = "my_administrator_main_page"),
    path('attractions', views.show_attractions, name="administrator_attractions"),
    path('attractions/<int:pk>', views.AttractionDetailView.as_view(), name="detail_view"),
    path('attractions/add', views.add_attraction, name="add_attraction"),
    path('attractions/<int:pk>/update', views.AttractionUpdateView.as_view(), name="update_attraction")
]