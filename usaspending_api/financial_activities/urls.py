from django.conf.urls import url
from usaspending_api.financial_activities import views

# bind ViewSets to URLs
financial_accounts_by_program_object = views.FinancialAccountsByProgramActivityObjectClassListViewSet.as_view(
    {'get': 'list', 'post': 'list'})

financial_accounts_by_award = views.FinancialAccountsByAwardListViewSet.as_view(
    {'get': 'list', 'post': 'list'})

urlpatterns = [
    url(r'^$', financial_accounts_by_program_object),
    url(r'^award/', financial_accounts_by_award),
]
