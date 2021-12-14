from rest_framework import  serializers

from .models import Exer
class ExerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exer
        fields = ['name','likes','user','speciality','solution','subject_name','ex_file','sou_file','date']
