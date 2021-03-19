from django.urls import path
from .views import RulesList, RulesDetail

urlpatterns = [
    path('', RulesList.as_view(), name='rules_list'),
    path('<int:pk>/', RulesDetail.as_view(), name='rules_detail'),
]

#     path('new/', RulesCreateView.as_view(), name='rules_create'),
#     path('<int:pk>/edit', RulesUpdateView.as_view(), name='rules_update'),
#     path('<int:pk>/delete', RulesDeleteView.as_view(), name='rules_delete'),