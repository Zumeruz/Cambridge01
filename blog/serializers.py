from rest_framework import serializers
from blog.models import Bosh, Text, Konsultatsiya, Yutuqlar, Negakambrij, Kurslarimiz, Konsultatsiya2, Text2, Teacher, \
    Natija, Artifaktlar


class BoshSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bosh
        fields='__all__'


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model=Text
        fields='__all__'

class KonsultatsiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Konsultatsiya
        fields = '__all__'

class YutuqlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yutuqlar
        fields = '__all__'

class NegakambrijSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negakambrij
        fields = '__all__'

class KurslarimizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurslarimiz
        fields = '__all__'

class Text2Serializer(serializers.ModelSerializer):
    class Meta:
        model=Text2
        fields='__all__'

class Konsultatsiya2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Konsultatsiya2
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class NatijaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Natija

class ArtifaktlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifaktlar
        fields = '__all__'