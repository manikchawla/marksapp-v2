from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Batch(models.Model):
    SEMESTER_CHOICES = [(i, i) for i in range(1, 9)]
    STREAM_CHOICES = (
        ("cse", "Computer Science"),
        ("ece", "Electronics and Communication"),
        ("mae", "Mechanical and Automation"),
        ("it", "Information Technology"),
        ("eee", "Electrical and Electronics")
    )
    name = models.CharField(max_length=5)
    subjects = models.ManyToManyField(Subject)
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    stream = models.CharField(max_length=3, choices=STREAM_CHOICES)

    def __str__(self):
        return self.name


class Student(models.Model):
    batch = models.ForeignKey(Batch)
    # subjects = models.ManyToManyField(Subject)
    name = models.CharField(max_length=250)
    roll_no = models.CharField(max_length=15, primary_key=True)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name
    

class Teacher(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class BatchSubject(models.Model):
    teacher = models.ForeignKey(Teacher)
    subject = models.ForeignKey(Subject)
    batch = models.ForeignKey(Batch)

    def __str__(self):
        return self.teacher.name


class Marks(models.Model):
    student = models.ForeignKey(Student)
    subject = models.ForeignKey(Subject)
    first_sessional = models.FloatField(null=True)
    second_sessional = models.FloatField(null=True)
    internal_assessment = models.IntegerField(null=True)
    total_internal_marks = models.IntegerField(null=True)


class Coordinator(models.Model):
    teacher = models.ForeignKey(Teacher)
    batch = models.ForeignKey(Batch)

    def __str__(self):
        return self.batch.name





