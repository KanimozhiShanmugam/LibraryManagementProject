from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from LibraryApp.models import Student, Course, Book, Issue_Book


# Create your views here.
def login_fun(request):
    return render(request,'login.html',{'data':''})

def logread_fun(request):
    username=request.POST['texttname']
    passw=request.POST['txtpwd']
    user = authenticate(username=username, password=passw)
    if user is not None:
        if user.is_superuser:
            return render(request,'admin_home.html')
        else:
            return render(request,'login.html',{'data':'User is not SuperUser'})
    elif Student.objects.filter(Q(Student_Name=username) & Q(Student_password=passw)).exists():

            request.session['name']=username
            return render(request,'student_home.html',{'student':username})
    else:
        return render(request, 'login.html', {'data': '!!Enter proper UserName and Password!!'})


def adminreg_fun(request):
    return render(request,'admin_register.html')


def adminread_fun(request):
    if User.objects.filter(Q(username=request.POST['txtname']) | Q(email=request.POST['txtemail'])).exists():
        return render(request, 'admin_register.html', {'data': '!!UserName or Email is already exists!!'})
    else:
        u1 = User.objects.create_superuser(username=request.POST['txtname'], email=request.POST['txtemail'], password=request.POST['txtpwd'])
        u1.save()
        return redirect('login')


def studentreg_fun(request):
    c1 = Course.objects.all()
    return render(request,'stu_register.html',{'data':'','course_data':c1})


def studentread_fun(request):
    c1 = Course.objects.all()
    user= Student.objects.filter(Q(Student_Phno= request.POST['txtphno']) & Q(Student_Name=request.POST['txtname'])).exists()
    if user:
        return render(request,'stu_register.html',{'data': '!!Name or PhoneNumber is already exists!!', 'course_data': c1})
    else:
        s1 = Student()
        s1.Student_Name = request.POST['txtname']
        s1.Student_Phno = request.POST['txtphno']
        s1.Student_Semester = request.POST['txtsem']
        s1.Student_password = request.POST['txtpwd']
        s1.Student_Course = Course.objects.get(Course_Name=request.POST['ddlcourse'])
        s1.save()
        return redirect('login')


def addbook_fun(request):
    c1=Course.objects.all()
    return render(request,'addbook.html',{'data':'','course':c1})


def addbook_read(request):

    b1=Book()
    b1.Book_Name=request.POST['txtbname']
    b1.Author_Name = request.POST['txtauthname']
    b1.Course_Id =Course.objects.get(Course_Name=request.POST['ddlcourse'])
    b1.save()
    return redirect('add')


def diplay_fun(request):
    book=Book.objects.all()
    return render(request,'displaybook.html',{'data':book})


def adminhome_fun(request):
    return render(request,'admin_home.html')


def logout_fun(request):
    return render(request,'login.html')


def updatebook_fun(request,id):
    b1 = Book.objects.get(id=id)
    c1=Course.objects.all()
    if request.method=='POST':
        b1.Book_Name = request.POST['txtbname']
        b1.Author_Name = request.POST['txtauthname']
        b1.Course_Id = Course.objects.get(Course_Name=request.POST['ddlcourse'])
        b1.save()
        return redirect('dis')
    else:
        return render(request,'updatebooks.html',{'data':b1,'course':c1})


def delete_fun(request,id):
    book= Book.objects.get(id=id)
    book.delete()
    return redirect('dis')

def assignbook_fun(request):
    c1=Course.objects.all()
    return render(request,'assignbook.html',{'course':c1})

def assignread_fun(request):
    stu=Student.objects.filter(Q(Student_Semester=request.POST['txtsem']) & Q(Student_Course=Course.objects.get(Course_Name=request.POST['ddlcourse'])))
    book = Book.objects.filter(Course_Id=Course.objects.get(Course_Name=request.POST['ddlcourse']))
    return render(request, 'assignbook.html', {'student': stu, 'book': book})


def issued_read(request):
    i1=Issue_Book()
    i1.Stu_Name=Student.objects.get(Student_Name=request.POST['ddlstuname'])
    i1.Bname=Book.objects.get(Book_Name=request.POST['ddlbname'])
    i1.Start_Date=request.POST['sdate']
    i1.End_Date=request.POST['edate']
    i1.save()
    return redirect('as')

def issued_book(request):
    i1=Issue_Book.objects.all()
    return render(request,'issuedbook.html',{'data':i1})


def update_issue(request,id):
    i1 = Issue_Book.objects.get(id=id)
    student=Student.objects.get(Student_Name=i1.Stu_Name)
    book=Book.objects.filter(Course_Id=student.Student_Course)
    if request.method=='POST':
        i1.Stu_Name = Student.objects.get(Student_Name=request.POST['txtname'])
        i1.Bname = Book.objects.get(Book_Name=request.POST['ddlbname'])
        i1.Start_Date = request.POST['sdate']
        i1.End_Date = request.POST['edate']
        i1.save()
        return redirect('ib')
    else:
        return render(request,'issueupdate.html',{'data':i1,'student':student,'book':book})



def stu_issued_book(request):
    i1=Issue_Book.objects.filter(Stu_Name=Student.objects.get(Student_Name=request.session['name']))
    print(i1)
    return render(request,'studentissuedbook.html',{'issue':i1})


def delete_issue(request,id):
    i1=Issue_Book.objects.get(id=id)
    i1.delete()
    return redirect('ib')


def student_home_fun(request):
    return render(request,'student_home.html',{'student':request.session['name']})