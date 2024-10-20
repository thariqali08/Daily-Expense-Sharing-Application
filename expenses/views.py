from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from .models import User, Expense
from .serializers import UserSerializer, ExpenseSerializer
import pandas as pd
import csv

class UserView(APIView):
    def post(self, request):
        serialized_user=UserSerializer(data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(serialized_user.data, status=status.HTTP_201_CREATED)
        return Response(serialized_user.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,user_id):
        user = get_object_or_404(User, id=user_id)
        serialized_user=UserSerializer(user)
        return Response(serialized_user.data)

    def patch(self, request,user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,user_id):
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return Response(f"User {user_id} Deleted",status=status.HTTP_204_NO_CONTENT)

class ExpenseView(APIView):
    def post(self, request):
        data = request.data
        participants = data.get('participants', [])
        split_method = data.get('split_method')
        total_amount = data.get('amount')

        # Handle Equal Split
        if split_method == 'equal':
            split_amount = total_amount / len(participants)
            split_details = {str(p): split_amount for p in participants}
        
        # Handle Exact Amount Split
        elif split_method == 'exact':
            split_details = data.get('split_details', {})
            if sum(split_details.values()) != total_amount:
                return Response({"error": "Exact split amounts do not match total amount."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Handle Percentage Split
        elif split_method == 'percentage':
            split_details = data.get('split_details', {})
            if sum(split_details.values()) != 100:
                return Response({"error": "Percentage split must add up to 100."}, status=status.HTTP_400_BAD_REQUEST)
            split_details = {p: total_amount * (split / 100) for p, split in split_details.items()}

        else:
            return Response({"error": "Invalid split method."}, status=status.HTTP_400_BAD_REQUEST)

        # Saving the Expense
        serializer = ExpenseSerializer(data={"description": data['description'], "amount": total_amount,
            "payer": data['payer'],"participants": participants,"split_method": split_method,"split_details": split_details})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ExpenseDetail(APIView):
    def get(self, request, user_id):
        expense = get_object_or_404(Expense, id=user_id)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)

    def patch(self, request, user_id):
        expense = get_object_or_404(Expense, id=user_id)
        serializer = ExpenseSerializer(expense, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        expense = get_object_or_404(Expense, id=user_id)
        expense.delete()
        return Response(f"Expense Id {user_id} Deleted",status=status.HTTP_204_NO_CONTENT)


class BalanceSheetCSV(APIView):
    def get(self, request):
        expenses = Expense.objects.all()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="balance_sheet.csv"'

        writer = csv.writer(response)
        writer.writerow(['ID', 'Description', 'Amount', 'Payer', 'Participants', 'Split Method', 'Split Details'])

        for expense in expenses:
            writer.writerow([expense.id, expense.description, expense.amount, 
                expense.payer.id, expense.participants.all(), expense.split_method, expense.split_details])
        return response
