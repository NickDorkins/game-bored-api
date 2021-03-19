from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import RulesSerializer
from .models import Rules

class RulesList(ListCreateAPIView):
    queryset = Rules.objects.all()
    serializer_class = RulesSerializer


class RulesDetail(RetrieveUpdateDestroyAPIView):
    queryset = Rules.objects.all()
    serializer_class = RulesSerializer