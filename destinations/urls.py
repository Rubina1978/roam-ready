from django.urls import path
from . import views


urlpatterns = [
    path('', views.DestinationsList.as_view(), name='home'),
    # {% comment %} ChatGPT as supplement for slug:slug in lesson as my model does not have slug (pk primary key, int integer only) {% endcomment %}
    path('<int:pk>/', views.destination_detail, name='destination_detail'),
    path('<int:destination_id>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
]
