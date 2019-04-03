"""sampleproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from baeun.views import (
    DiaryList, DiaryCreate, DiaryDetail, DiaryUpdate, DiaryDelete,
    CashbookList, CashbookCreate, CashbookDetail, CashbookUpdate, CashbookDelete,
    FriendHistoryList, FriendHistoryCreate, FriendHistoryDetail, FriendHistoryUpdate, FriendHistoryDelete,
    RelationList, RelationCreate, RelationDetail, RelationUpdate, RelationDelete, RelationMeList,
    UserCreate
)

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),

    path('diary/<int:pk>/', DiaryDetail.as_view(), name='diary_detail'),
    path('diary/update/<int:pk>/', DiaryUpdate.as_view(), name='diary_update'),
    path('diary/delete/<int:pk>/', DiaryDelete.as_view(), name='diary_delete'),
    path('diary/', DiaryList.as_view(), name='diary'),
    path('diary/form/', DiaryCreate.as_view(), name='diary_form'),

    path('cashbook/<int:pk>/', CashbookDetail.as_view(), name='cashbook_detail'),
    path('cashbook/update/<int:pk>/', CashbookUpdate.as_view(), name='cashbook_update'),
    path('cashbook/delete/<int:pk>/', CashbookDelete.as_view(), name='cashbook_delete'),
    path('cashbook/', CashbookList.as_view(), name='cashbook'),
    path('cashbook/form/', CashbookCreate.as_view(), name='cashbook_form'),

    path('relation/<int:pk>/', RelationDetail.as_view(), name='relation_detail'),
    path('relation/update/<int:pk>/', RelationUpdate.as_view(), name='relation_update'),
    path('relation/delete/<int:pk>/', RelationDelete.as_view(), name='relation_delete'),
    path('relation/', RelationList.as_view(), name='relation'),
    path('relation/me/', RelationMeList.as_view(), name='relation_me'),
    path('relation/form/', RelationCreate.as_view(), name='relation_form'),

    path('friend_history/<int:pk>/', FriendHistoryDetail.as_view(), name='friend_history_detail'),
    path('friend_history/update/<int:pk>/', FriendHistoryUpdate.as_view(), name='friend_history_update'),
    path('friend_history/delete/<int:pk>/', FriendHistoryDelete.as_view(), name='friend_history_delete'),
    path('friend_history/', FriendHistoryList.as_view(), name='friend_history'),
    path('friend_history/form/', FriendHistoryCreate.as_view(), name='friend_history_form'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreate.as_view(), name='register'),
    path('accounts/register/done/', TemplateView.as_view(template_name='registration/register_done.html'),
         name='register_done'),
    path('admin/', admin.site.urls),
]
