from django.contrib import admin
from .models import (
    Cashbook, Diary, Todo, Activity, Habit, Relation, FriendHistory, MoodLog,
    Chronicle
)


class CashbookAdmin(admin.ModelAdmin):
    ordering = ['-event_dt', 'money_usage_group']
    list_display = ('id', 'owner', 'event_dt', 'money_usage',
                    'money_amount', 'money_usage_group', 'counting_type')
    list_filter = ('money_usage_group', 'counting_type')
    list_per_page = 15


class DiaryAdmin(admin.ModelAdmin):
    ordering = ['-event_dt']
    list_display = ('id', 'owner', 'content', 'event_dt')
    list_per_page = 15


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'condition', 'content', 'check_yn')
    list_per_page = 15


class ActivityAdmin(admin.ModelAdmin):
    ordering = ['-event_dt', 'activity_group']
    list_display = ('id', 'owner', 'event_dt', 'content', 'activity_group')
    list_filter = ('activity_group',)
    list_per_page = 15


class HabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'condition', 'content')
    list_per_page = 15


class RelationAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'friend_id',
                    'total_trust_point', 'first_friend_dt')
    list_filter = ('owner', 'friend_id')
    list_per_page = 15


class FriendHistoryAdmin(admin.ModelAdmin):
    list_display = ('relation', 'trust_point', 'content', 'event_dt')
    list_filter = ('relation',)
    list_per_page = 15


class MoodLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'mood', 'event_dttm', 'reason')
    list_per_page = 15


class ChronicleAdmin(admin.ModelAdmin):
    ordering = ['-year']
    list_display = ('id', 'owner', 'residence', 'primary_tag', 'year', 'content', 'new_people')


admin.site.register(Cashbook, CashbookAdmin)
admin.site.register(Diary, DiaryAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Habit, HabitAdmin)
admin.site.register(Relation, RelationAdmin)
admin.site.register(FriendHistory, FriendHistoryAdmin)
admin.site.register(MoodLog, MoodLogAdmin)
admin.site.register(Chronicle, ChronicleAdmin)
