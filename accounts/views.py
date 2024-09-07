from rest_framework import generics,status
from .models import Walet
from .serializers import WaletSerializer,UpateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class WaletListCreateView(generics.ListCreateAPIView):
    queryset = Walet.objects.all()
    serializer_class = WaletSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Walet.objects.filter(user = self.request.user)


class WaletUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Walet.objects.all()
    serializer_class = UpateSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Walet.objects.filter(user = self.request.user)

class WaletListCreateView(generics.ListCreateAPIView):
    queryset = Walet.objects.all()
    serializer_class = WaletSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Walet.objects.filter(user=self.request.user)

class WaletRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Walet.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Walet.objects.filter(user=self.request.user)

    def add_amount(self, request, *args, **kwargs):
        walet = self.get_object()
        amount = request.data.get('amount', 0)

        try:
            walet.add_amount(amount)
            return Response({"message": "Amount added successfully.", "new_balance": walet.wallet}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



