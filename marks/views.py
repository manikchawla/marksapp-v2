from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from .models import Batch, Subject, Student, Teacher, Marks, BatchSubject, Coordinator
from .forms import TeacherForm, MarksFormSet, UploadFileForm
import django_excel as excel
import pyexcel.ext.xlsx
import openpyxl
import math

def home(request):
    return render(request, "marks/home.html")

def teacher_login(request):
    form = TeacherForm
    context = {
        'form': form
    }
    if request.POST:
        email= request.POST['email']
        if Teacher.objects.filter(email=email).exists():
            teacher = Teacher.objects.get(email=email)
            if teacher.password == request.POST['password']:
                is_coordinator = False
                coordinator_batch = None
                request.session['teacher_id'] = teacher.id
                batch_subject = BatchSubject.objects.filter(teacher=teacher)
                if Coordinator.objects.filter(teacher=teacher).exists():
                    is_coordinator = True
                    coordinator = Coordinator.objects.get(teacher=teacher)
                    coordinator_batch = coordinator.batch
                context = {
                    "teacher": teacher,
                    'batch_subject': batch_subject,
                    "is_coordinator": is_coordinator,
                    "coordinator_batch": coordinator_batch,
                }
                return render(request, "marks/dashboard.html", context)
            else:
                return redirect(reverse('marks:teacher_login')) 
        else: 
            return redirect(reverse('marks:teacher_login'))
    elif request.session.get('teacher_id'):
        teacher_id = request.session['teacher_id']
        teacher = Teacher.objects.get(pk=teacher_id)
        is_coordinator = False
        coordinator_batch = None
        batch_subject = BatchSubject.objects.filter(teacher=teacher)
        if Coordinator.objects.filter(teacher=teacher).exists():
            is_coordinator = True
            coordinator = Coordinator.objects.get(teacher=teacher)
            coordinator_batch = coordinator.batch
        context = {
            "teacher": teacher,
            'batch_subject': batch_subject,
            "is_coordinator": is_coordinator,
            "coordinator_batch": coordinator_batch,
        }
        return render(request, "marks/dashboard.html", context)
    else: 
        return render(request, "marks/teacher_login.html", context)

def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv", file_name="download")
    else:
        form = UploadFileForm()
    context = {
        "form": form,
    }
    return render(request, "marks/upload_form.html", context)

def edit_marks(request):
    batch_subject_id = request.POST['batch_subject_id']
    exam_type = request.POST['exam_type']
    batch_subject = BatchSubject.objects.get(pk=batch_subject_id)
    batch = batch_subject.batch
    subject = batch_subject.subject
    student_list = Student.objects.filter(batch=batch)
    student_marks_list = []
    for student in student_list:
        student_details = {}
        Marks.objects.get_or_create(subject=subject, student=student)
        marks = Marks.objects.get(subject=subject, student=student)
        student_details['marks'] = marks
        student_details['student'] = Student.objects.get(pk=student.roll_no)
        student_marks_list.append(student_details)
    context = {
        "student_list": student_list,
        "batch_subject_id": batch_subject_id,
        "exam_type": exam_type,
        "student_marks_list": student_marks_list,
    }
    return render(request, "marks/edit_marks.html", context)

def submit_marks(request):
    print(request.POST)
    dict_post_data = request.POST
    exam_type = dict_post_data['exam_type']
    print(exam_type)
    batch_subject_id = dict_post_data['batch_subject_id']
    batch_subject = BatchSubject.objects.get(pk=batch_subject_id)
    batch = batch_subject.batch
    subject = batch_subject.subject
    student_list = Student.objects.filter(batch=batch)
    for student in student_list:
        if student.roll_no in dict_post_data:
            marks = dict_post_data[student.roll_no]
            Marks.objects.get(subject=subject, student=student)
            marks_field = Marks.objects.get(subject=subject, student=student)
            if exam_type == 'first_sessional' and marks != '':
                marks_field.first_sessional = float(marks)
            elif exam_type == 'second_sessional' and marks != '':
                marks_field.second_sessional = float(marks)
            elif exam_type == "internal_assessment" and marks != '':
                marks_field.internal_assessment = int(marks)
            if marks_field.first_sessional is not None and marks_field.second_sessional is not None \
            and marks_field.internal_assessment is not None:
                first = marks_field.first_sessional
                second = marks_field.second_sessional
                internal = marks_field.internal_assessment
                total = math.ceil(first / 3) + math.ceil(second / 3) + internal
                marks_field.total_internal_marks = total
            marks_field.save() 
    return redirect(reverse('marks:teacher_login'))

def view_marks(request):
    exam_type = request.POST['exam_type']
    batch_name = request.POST['batch']
    batch = Batch.objects.get(name=batch_name)
    subjects = batch.subjects.all()
    marks_list = []
    subject_teachers = ['', '']
    headers = ['Roll No', 'Name']
    for subject in subjects: 
        headers.append(subject.name)
        sub_teacher = BatchSubject.objects.get(batch=batch, subject=subject).teacher.name
        subject_teachers.append(sub_teacher)
    print(headers)
    marks_list.append(headers)
    marks_list.append(subject_teachers)
    student_list = Student.objects.filter(batch=batch)
    for student in student_list:
        print(student)
        marks_student = []
        marks_student.append(student.roll_no)
        marks_student.append(student.name)
        for subject in subjects:
            print(subject)
            marks = Marks.objects.get(student=student, subject=subject)
            if exam_type == 'first_sessional':
                print(marks.first_sessional)
                marks_student.append(marks.first_sessional)
            elif exam_type == 'second_sessional':
                print(marks.second_sessional)
                marks_student.append(marks.second_sessional)
            if exam_type == 'total_internal_marks':
                print(marks.total_internal_marks)
                marks_student.append(marks.total_internal_marks)
        marks_list.append(marks_student)
    print(marks_list)
    wb = openpyxl.Workbook()
    sheet = wb.get_sheet_by_name('Sheet')
    i = 1
    for line in marks_list:
        sheet.append(line)
    # for marks in marks_list:
    #     print(marks)
    #     j = 1
    #     for item in marks:
    #         sheet.cell(row=i, column=j, value=item)
    #         j += 1
    #     i += 1
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetm.sheet')
    response['Content-Disposition'] = 'attachment; filename=mydata.xlsx'
    wb.save(response)
    return response

def logout(request):
    try:
        del request.session['teacher_id']
        return redirect(reverse("marks:teacher_login"))
    except KeyError:
        pass
    return redirect(reverse("marks:teacher_login"))