from django.urls import path
from . import views


urlpatterns = [
    path('', views.DestinationsList.as_view(), name='home'),
    # {% comment %} ChatGPT as supplement for slug:slug in lesson as my model does not have slug (pk primary key, int integer only) {% endcomment %}
    path('<int:pk>/', views.destination_detail, name='destination_detail'),
    path('<int:destination_id>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<int:destination_id>/edit_tip/<int:tip_id>', views.tip_edit, name='tip_edit'),
    path('<int:destination_id>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('<int:destination_id>/delete_tip/<int:tip_id>/', views.tip_delete, name="tip_delete"),
]
