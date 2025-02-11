from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Placeholder homepage
    path('add_expense/', views.add_expense, name='add_expense'),  # Add expense view
    path('expenses/', views.expense_list, name='expense_list'),  # List of expenses
]
