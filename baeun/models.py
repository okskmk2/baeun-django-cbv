from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Cashbook(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event_dt = models.DateField()
    money_amount = models.IntegerField()
    money_usage = models.CharField(max_length=40)
    money_usage_group = models.CharField(max_length=10)
    counting_type = models.CharField(max_length=8)
    reg_dt = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('cashbook')

    class Meta:
        verbose_name_plural = "회계장부"
        ordering = ['-event_dt', 'money_usage_group']


class Diary(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    event_dt = models.DateField()
    reg_dt = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('diary')

    class Meta:
        verbose_name_plural = "다이어리"
        ordering = ['-event_dt', '-id']


class Activity(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event_dt = models.DateField()
    content = models.CharField(max_length=100)
    activity_group = models.CharField(max_length=10)
    reg_dt = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "활동들"


class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    condition = models.CharField(max_length=70)
    content = models.TextField()
    check_yn = models.BooleanField()
    reg_dt = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "할일"


class Habit(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    condition = models.CharField(max_length=70)
    content = models.TextField()
    reg_dt = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "습관"


# 2019-02-22 added
class Relation(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    friend_id = models.CharField(max_length=150)
    total_trust_point = models.IntegerField()
    first_friend_dt = models.DateField()
    reg_dt = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('relation')

    def __str__(self):
        return '%s-%s' % (self.owner, self.friend_id)

    class Meta:
        verbose_name_plural = "사람들"
        ordering = ['-first_friend_dt', '-id']


# 2019-02-22 added
class FriendHistory(models.Model):
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE)
    trust_point = models.IntegerField()
    content = models.TextField()
    reg_dt = models.DateField(auto_now_add=True)
    event_dt = models.DateField(null=True)

    def save(self, *args, **kwargs):
        pre_r = FriendHistory.objects.filter(id=self.id).first()
        r = Relation.objects.get(id=self.relation.id)
        if pre_r is None:
            new_trust_point = self.trust_point
        else:
            new_trust_point = self.trust_point - pre_r.trust_point
        r.total_trust_point += new_trust_point
        r.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        r = Relation.objects.get(id=self.relation.id)
        r.total_trust_point -= self.trust_point
        r.save()
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('friend_history')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "지인기록"
        ordering = ['-event_dt']


class MoodLog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.IntegerField()
    event_dttm = models.DateTimeField()
    reason = models.TextField()
    reg_dt = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "기분기록"


class Chronicle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    primary_tag = models.CharField(max_length=20, null=True, blank=True)
    year = models.IntegerField()
    residence = models.CharField(max_length=90)
    content = models.TextField()
    new_people = models.TextField(null=True, blank=True)
    reg_dt = models.DateField(auto_now_add=True)
    upd_dt = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "연대기"
