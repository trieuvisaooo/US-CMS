from django.db import models

# Create your models here.
class Department(models.Model):
    dep_id = models.AutoField(primary_key=True)
    dep_name = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = 'DEPARTMENT'

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'ROLE'

class Member(models.Model):
    member_id = models.CharField(max_length=20, primary_key=True)
    member_avaUrl = models.CharField(max_length=255, blank=True, null=True)
    member_name = models.CharField(max_length=50)
    member_dob = models.DateField()
    member_phoneNum = models.CharField(max_length=11)
    member_addr = models.CharField(max_length=100, blank=True, null=True)
    member_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    member_class = models.CharField(max_length=10)
    member_joinedDate = models.DateField()
    member_role = models.ForeignKey(Role, on_delete=models.CASCADE)
    member_accPassword = models.CharField(max_length=255)
    member_accStatus = models.IntegerField()

    class Meta:
        db_table = 'MEMBER'

class TaskStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'TASK_STATUS'

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_owner = models.ForeignKey(Member, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=30)
    task_subtitle = models.CharField(max_length=50, blank=True, null=True)
    task_description = models.TextField(max_length=1000, blank=True, null=True)
    task_startDate = models.DateField()
    task_dueDate = models.DateField()
    task_note = models.CharField(max_length=50, blank=True, null=True)
    task_status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)

    class Meta:
        db_table = 'TASK'

class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    activity_title = models.CharField(max_length=30)
    activity_subtitle = models.CharField(max_length=50, blank=True, null=True)
    activity_content = models.TextField(max_length=1000, blank=True, null=True)
    activity_postedDate = models.DateField()
    activity_author = models.ForeignKey(Member, on_delete=models.CASCADE)
    activity_thumbnailUrl = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'ACTIVITY'

class ClubInfo(models.Model):
    club_id = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=50)
    club_establishedDate = models.DateField(blank=True, null=True)
    club_slogan = models.CharField(max_length=255, blank=True, null=True)
    club_description = models.TextField(max_length=5000, blank=True, null=True)
    club_imgUrl = models.CharField(max_length=255, blank=True, null=True)
    club_logoUrl = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'CLUB_INFOR'

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=30)
    post_subtitle = models.CharField(max_length=50, blank=True, null=True)
    post_content = models.TextField(max_length=1000, blank=True, null=True)
    post_postedDate = models.DateField()
    post_author = models.ForeignKey(Member, on_delete=models.CASCADE)
    post_numOfLike = models.IntegerField(default=0)
    post_numOfComment = models.IntegerField(default=0)

    class Meta:
        db_table = 'POST'

class LikeOfPost(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, primary_key=True)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)

    class Meta:
        db_table = 'LIKE_OF_POST'
        unique_together = (('post_id', 'member_id'),)

class CommentOfPost(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=200)
    comment_createdDate = models.DateField()

    class Meta:
        db_table = 'COMMENT_OF_POST'
