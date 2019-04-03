from baeun.models import Diary, Cashbook, Relation, FriendHistory
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


class UserCreate(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class DiaryList(LoginRequiredMixin, ListView):
    model = Diary
    context_object_name = 'diary_list'
    paginate_by = 15

    def get_queryset(self):
        queryset = super(DiaryList, self).get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class DiaryCreate(CreateView):
    model = Diary
    fields = ['owner', 'content', 'event_dt']

    def get_initial(self):
        initial = super(DiaryCreate, self).get_initial()
        initial.update({'owner': self.request.user})
        return initial

    # def __init__(self, *args, **kwargs):
    #     super(DiaryCreate, self).__init__(*args, **kwargs)
    #     self.fields['owner'].disabled = True


class DiaryDetail(DetailView):
    model = Diary


class DiaryUpdate(UpdateView):
    model = Diary
    fields = ['content', 'event_dt']


class DiaryDelete(DeleteView):
    model = Diary
    success_url = reverse_lazy('diary')


# Cashbook
class CashbookList(LoginRequiredMixin, ListView):
    model = Cashbook
    context_object_name = 'cashbook_list'
    paginate_by = 20

    def get_queryset(self):
        queryset = super(CashbookList, self).get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class CashbookCreate(CreateView):
    model = Cashbook
    fields = ['owner', 'event_dt', 'money_usage', 'money_amount', 'money_usage_group', 'counting_type']

    def get_initial(self):
        initial = super(CashbookCreate, self).get_initial()
        initial.update({'owner': self.request.user})
        return initial


class CashbookDetail(DetailView):
    model = Cashbook


class CashbookUpdate(UpdateView):
    model = Cashbook
    fields = ['event_dt', 'money_usage', 'money_amount', 'money_usage_group', 'counting_type']


class CashbookDelete(DeleteView):
    model = Cashbook
    success_url = reverse_lazy('cashbook')


# Relation
class RelationList(LoginRequiredMixin, ListView):
    model = Relation
    context_object_name = 'relation_list'
    paginate_by = 20

    def get_queryset(self):
        queryset = super(RelationList, self).get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class RelationCreate(CreateView):
    model = Relation
    fields = ['owner', 'friend_id', 'total_trust_point', 'first_friend_dt']

    def get_initial(self):
        initial = super(RelationCreate, self).get_initial()
        initial.update({'owner': self.request.user})
        return initial


class RelationDetail(DetailView):
    model = Relation


class RelationUpdate(UpdateView):
    model = Relation
    fields = ['friend_id', 'total_trust_point', 'first_friend_dt']


class RelationDelete(DeleteView):
    model = Relation
    success_url = reverse_lazy('relation')


class RelationMeList(LoginRequiredMixin, ListView):
    template_name = 'baeun/relation_me_list.html'
    model = Relation
    context_object_name = 'relation_me_list'
    paginate_by = 20

    def get_queryset(self):
        queryset = super(RelationMeList, self).get_queryset()
        queryset = queryset.filter(friend_id=self.request.user)
        return queryset


# friendHistory
# Relation
class FriendHistoryList(LoginRequiredMixin, ListView):
    model = FriendHistory
    context_object_name = 'friend_history_list'
    paginate_by = 20

    # def get_queryset(self):
    #     queryset = super(FriendHistoryList, self).get_queryset()
    #     queryset = queryset.filter(owner=self.request.user)
    #     return queryset


class FriendHistoryCreate(CreateView):
    model = FriendHistory
    fields = ['relation', 'trust_point', 'content']

    # def get_initial(self):
    #     initial = super(FriendHistoryCreate, self).get_initial()
    #     initial.update({'owner': self.request.user})
    #     return initial


class FriendHistoryDetail(DetailView):
    model = FriendHistory


class FriendHistoryUpdate(UpdateView):
    model = FriendHistory
    fields = ['trust_point', 'content']


class FriendHistoryDelete(DeleteView):
    model = FriendHistory
    success_url = reverse_lazy('friend_history')
