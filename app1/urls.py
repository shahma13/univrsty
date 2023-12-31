from django.urls import path
from.import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('thome',views.thome,name='thome'),
    path('',views.login1,name='login1'),
    path('signup1',views.signup1,name='signup1'),
    path('add_course',views.add_course,name='add_course'),
    path('add_stud',views.add_stud,name='add_stud'),
    path('table1',views.table1,name='table1'),
    path('table2',views.table2,name='table2'),
    path('edit',views.edit,name='edit'),
    path('add',views.add,name='add'),
    path('th_add',views.th_add,name='th_add'),
    path('std_add',views.std_add,name='std_add'),
    path('edit_page/<int:pk>',views.edit_page,name='edit_page'),
    path('edit_pages/<int:pk>',views.edit_pages,name='edit_pages'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('card',views.card,name='card'),
    path('logout',views.logout,name='logout'),
    path('adminlog',views.adminlog,name='adminlog'),
    path('edit_st/<int:pk>',views.edit_st,name='edit_st'),
    path('deletes/<int:pk>',views.deletes,name='deletes'),
    path('sign',views.sign,name='sign'),
    path('profile',views.profile,name='profile'),
    # path('scard',views.scard,name='scard'),
    path('goback',views.goback,name='goback'),
    path('sedit',views.sedit,name='sedit'),
]