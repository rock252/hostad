from rest_framework import serializers
from api.models import Information , Sendtotab

class postSerializer(serializers.ModelSerializer):
   class Meta:
      model = Information
      fields= ('android_id','latitude','longitude', )




class postSerializer2(serializers.ModelSerializer):
   class Meta:
      model = Sendtotab
      fields= ('user_id','video_id1','video_id2', 'video_id3','video_id4', 'video_id5',)


