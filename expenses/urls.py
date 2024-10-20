from django.urls import path
from .views import UserView, ExpenseDetail, ExpenseView, BalanceSheetCSV

urlpatterns = [
    # User routes
    path('users/', UserView.as_view() ),
    path('users/<int:user_id>/', UserView.as_view() ),

    # Expense routes
    path('expense/', ExpenseView.as_view() ),
    path('expenselistall/', ExpenseView.as_view() ),
    path('expense/user/<int:user_id>/', ExpenseDetail.as_view() ),
    path('balancesheet/', BalanceSheetCSV.as_view() ),
    
]
