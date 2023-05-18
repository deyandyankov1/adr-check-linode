from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import HomeView, AdrCreateView, AdrListView, AdrDetailView, AdrUpdateView, LoginPageView, AdrDeleteView


urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('list/', AdrListView.as_view(), name='adr_list'),
    path('add/', AdrCreateView.as_view(), name='adr_check'),
    # path('add/signature', SignatureView.as_view(), name = 'adr_signature'),
    path('list/<int:pk>/', AdrDetailView.as_view(), name='adr_detail'),
    path('list/<int:pk>/update', AdrUpdateView.as_view(), name='adr_update'),
    path('list/<int:pk>/delete', AdrDeleteView.as_view(), name='adr_delete'),

]
