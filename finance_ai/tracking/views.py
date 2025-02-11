from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Financial Tracking AI!")

def add_expense(request):
    return HttpResponse("This is where you will add an expense.")

def expense_list(request):
    return HttpResponse("This is where you will view all expenses.")
