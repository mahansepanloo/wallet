from rest_framework import generics, serializers
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        wallet = getattr(user, 'walet', None)

        transaction_amount = serializer.validated_data['amount']

        if wallet and wallet.wallet >= transaction_amount:
            wallet.wallet -= transaction_amount
            wallet.save()
            return serializer.save(user=user)
        else:
            raise serializers.ValidationError("Insufficient funds in wallet or wallet does not exist.")

class TransactionDetailView(generics.UpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user__user=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)