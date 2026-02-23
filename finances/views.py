from django.shortcuts import render
from .models import Transaction

def transaction_list(request):
    transaction = Transaction.objects.all()
    return render(request, 'finances/transaction_list.html', {
        'transaction': transaction
    })
