from django.urls import path

from LibraryApp import views

urlpatterns = [
    path('',views.login_fun,name='login'),
    path('logread',views.logread_fun,name='logr'),
    path('a_reg',views.adminreg_fun,name='a'),
    path('a_read',views.adminread_fun),
    path('s_reg',views.studentreg_fun,name='s'),
    path('s_read',views.studentread_fun),
    path('add_book',views.addbook_fun,name='add'),
    path('addread',views.addbook_read),
    path('display',views.diplay_fun,name='dis'),
    path('ahome',views.adminhome_fun,name='ahome'),
    path('log_out',views.logout_fun,name='log_out'),
    path('update/<int:id>',views.updatebook_fun,name='up'),
    path('delete/<int:id>',views.delete_fun,name='del'),
    path('assign',views.assignbook_fun,name='as'),
    path('assignread',views.assignread_fun),
    path('readassign',views.issued_read),
    path('issuedbook',views.issued_book,name='ib'),
    path('updateissue/<int:id>',views.update_issue,name='ui'),
    path('deleteissue/<int:id>',views.delete_issue,name='di'),
    path('stuissuedbook',views.stu_issued_book,name='sib'),
    path('studenthome',views.student_home_fun,name='stuh')

    ]

