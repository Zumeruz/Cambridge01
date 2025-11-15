from rest_framework import generics
from rest_framework.generics import  ListAPIView
from blog.models import Bosh, Text, Konsultatsiya, Yutuqlar, Negakambrij, Kurslarimiz, Text2, Konsultatsiya2, Teacher, \
    Natija, Artifaktlar

from blog.serializers import BoshSerializer, TextSerializer, KonsultatsiyaSerializer, YutuqlarSerializer, \
    NegakambrijSerializer, KurslarimizSerializer, Text2Serializer, Konsultatsiya2Serializer, TeacherSerializer, \
    NatijaSerializer, ArtifaktlarSerializer



# Malumot1 Viewsi
class BoshListView(ListAPIView):
    queryset = Bosh.objects.all()
    serializer_class = BoshSerializer


# # Malumot2 Viewsi
class TextListView(ListAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer


# Konsultatsiya
class KonsultatsiyaCreateView(generics.CreateAPIView):
    queryset = Konsultatsiya.objects.all()
    serializer_class = KonsultatsiyaSerializer



# yutuwlarimiz

class YutuqlarListView(ListAPIView):
    queryset = Yutuqlar.objects.all()
    serializer_class = YutuqlarSerializer

# Nega kabrijni tanlashimiz kerak

class NegakambrijListView(ListAPIView):
    queryset = Negakambrij.objects.all()
    serializer_class = NegakambrijSerializer


# Bizning Kurslarimiz

class KurslarimizListView(ListAPIView):
    queryset = Kurslarimiz.objects.all()
    serializer_class = KurslarimizSerializer



# reklama 00002 start

class TextListView2(ListAPIView):
    queryset = Text2.objects.all()
    serializer_class = Text2Serializer


# Konsultatsiya
class KonsultatsiyaCreateView2(generics.CreateAPIView):
    queryset = Konsultatsiya2.objects.all()
    serializer_class = Konsultatsiya2Serializer


# reklama 00002 end

# oqtuvchilarimiz
class TeacherListView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


# bizning natijalarimiz

class NatijaListView(ListAPIView):
    queryset = Natija.objects.all()
    serializer_class = NatijaSerializer


# kop beriladoiogan savollar

class ArtifaktlarListView(ListAPIView):
    queryset = Artifaktlar.objects.all()
    serializer_class = ArtifaktlarSerializer