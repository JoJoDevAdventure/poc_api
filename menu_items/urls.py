from django.urls import path
from .views import NewItemView, AddItemView, FetchItemsView

urlpatterns = [
    path('process_item/', NewItemView.as_view(), name='new-item'),
    path('add_item/', AddItemView.as_view(), name='add-item'),
    path('fetch_items/', FetchItemsView.as_view(), name='fetch-items'),
]