from django.db import models
from model_utils import Choices
from django.utils.translation import ugettext_lazy as _

# Create your models here.
GRADE_CHOICES = Choices(
        ('0', '10'),
        ('1', '11'),
        ('2', '12'),
    )

TYPE_CHOICES = Choices(
        ('0',"Điểm 15'"),
        ('1',"Điểm 45'"),
        ('2',"Điểm học kỳ'"),
        ('3',"Điểm miệng'"),
    )

SEMESTER_CHOICES = Choices(
        ('0', '1'),
        ('1', '2'),
    )

DAYS_OF_WEEK_CHOICES = Choices(
    ('0', 'Thứ 2'),
    ('1', 'Thứ 3'),
    ('2', 'Thứ 4'),
    ('3', 'Thứ 5'),
    ('4', 'Thứ 6'),
    ('5', 'Thứ 7'),
)


class Teacher(models.Model):
    full_name = models.CharField(max_length=100, blank=True, null=True, verbose_name =_("Họ và tên"))

    def __str__(self):
        if self.full_name is None:
            return ""
        else:
            return self.full_name

    class Meta:
        verbose_name = verbose_name_plural = _('Danh sách giáo viên')
        ordering = ['full_name', 'id']


class Class(models.Model):
    grade = models.CharField(
        max_length = 20,
        choices = GRADE_CHOICES,
        default = '-----'
        )
    name = models.CharField(max_length=10, blank=True, null=True, verbose_name=_('Tên lớp'))

    def __str__(self):
        if self.name is None:
            return ""
        else:
            return self.name

    class Meta:
        verbose_name = verbose_name_plural = _('Danh sách lớp')
        ordering = ['name', 'id']


class Subject(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Tên môn học'))

    def __str__(self):
        if self.name is None:
            return ""
        else:
            return self.name

    class Meta:
        verbose_name = verbose_name_plural = _('Danh sách môn học')
        ordering = ['name', 'id']


class Student(models.Model):
    full_name = models.CharField(max_length=100, blank=True, null=True, verbose_name =_("Họ và tên"))
    class_id = models.ForeignKey('Class', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Lớp"))
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        if self.full_name is None:
            return ""
        else:
            return self.full_name

    class Meta:
        verbose_name = verbose_name_plural = _('Danh sách Học sinh')
        ordering = ['full_name', 'id']


class Score(models.Model):
    result = models.IntegerField(blank=True, null=True, verbose_name= ('Kết qua'))
    type = models.CharField(
        max_length = 20,
        choices = TYPE_CHOICES,
        default = '-----'
        )
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Học sinh"))
    subject_id = models.ForeignKey('Subject', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Môn học"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Ngày tạo'))
    last_modify_date = models.DateTimeField(auto_now=True, null=True, verbose_name=_('Ngày sửa'))

    def __str__(self):
        if self.result is None:
            return ""
        else:
            return self.result

    class Meta:
        verbose_name = verbose_name_plural = _('Danh sách Điểm')
        ordering = ['student_id', 'subject_id']


class Schedule(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name =_("Tên thời khóa biểu"))
    semester = models.CharField(
        max_length = 20,
        choices = SEMESTER_CHOICES,
        default = '-----',
        verbose_name=_('Học kỳ')
        )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Ngày tạo'))
    last_modify_date = models.DateTimeField(auto_now=True, null=True, verbose_name=_('Ngày sửa'))

    def __str__(self):
        if self.name is None:
            return ""
        else:
            return '{} học kỳ {}'.format(self.name, self.semester)

    class Meta:
        verbose_name = verbose_name_plural = _('Danh sách thời khóa biểu')
        ordering = ['name', 'id', ]


class Lesson(models.Model):
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE, blank=True, null=True,verbose_name=_("Giáo viên"))
    subject_id = models.ForeignKey('Subject', on_delete=models.CASCADE, blank=True, null=True,verbose_name=_("Môn học"))
    class_id = models.ForeignKey('Class', on_delete=models.CASCADE, blank=True, null=True,verbose_name=_("Lớp"))
    schedule_id = models.ForeignKey('Schedule', on_delete=models.CASCADE, blank=True, null=True,verbose_name=_("Thời khóa biểu"))
    note = models.CharField(max_length=100, blank=True, null=True,verbose_name=_('Ghi chú'))
    time = models.CharField(
        max_length=20,
        choices=DAYS_OF_WEEK_CHOICES,
        default='-----'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Ngày tạo'))
    last_modify_date = models.DateTimeField(auto_now=True, null=True, verbose_name=_('Ngày sửa'))

    def __str__(self):
        if self.created_at is None:
            return ""
        else:
            return '{}:{}'.format(self.teacher_id, self.class_id)

    class Meta:
        verbose_name = verbose_name_plural = _('Danh sách buổi học')
        ordering = ['teacher_id', 'class_id', 'subject_id']




