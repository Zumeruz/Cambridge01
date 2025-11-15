from django.urls import path

from blog.views import BoshListView, TextListView, KonsultatsiyaCreateView, YutuqlarListView, NegakambrijListView, \
    KurslarimizListView, KonsultatsiyaCreateView2, TextListView2, TeacherListView, NatijaListView, ArtifaktlarListView
urlpatterns=[


    path('boshlist/<int:id>/', BoshListView.as_view(), name="bosh_list"),

    path('textlist/', TextListView.as_view(), name="text_list"),
    path('konsultatsiyalistcreate/', KonsultatsiyaCreateView.as_view(), name="konsultatsiya_create"),


    path('yutuqlarlistcreate/', YutuqlarListView.as_view(), name="yutuqlar_create"),


    path('negakambrijlistcreate/', NegakambrijListView.as_view(), name="negakambrij_create"),


    path('kurslarimizlistcreate/', KurslarimizListView.as_view(), name="kurslarimiz_create"),


    path('text2list/', TextListView2.as_view(), name="text2_list"),
    path('konsultatsiya2listcreate/', KonsultatsiyaCreateView2.as_view(), name="konsultatsiya2_create"),

    path('teachers/', TeacherListView.as_view(), name='teacherlist'),


    path('natijalist/', NatijaListView.as_view(), name="natija_list"),


    path('artifaktlarlist/', ArtifaktlarListView.as_view(), name="artifaktlar_list"),

    ]