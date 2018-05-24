from django.shortcuts import render, Http404, HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from . serializers import *
import json
import datetime
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt

def update_information(request):
    if request.method == "POST":
        post = json.loads(request.body.decode("utf-8"))
        print(post)
        response_data = {}
        if post.get("key") == "70b66a89929e93416d2ef535893ea14da331da8991cc7c74010b4f3d7fabfd62":
            android_id = post['android_id']
            advertiser_name = post['advertiser_name']
            video_count = post['video_count']
            latitude = post['latitude']
            longitude = post['longitude']
            
            try:
                a = Information()
                a.android_id= android_id
                a.advertiser_name= advertiser_name
                a.video_count= video_count
                a.latitude= latitude
                a.longitude= longitude
                
                a.save()
                response_data['status'] = 'true'
            except Exception as e:
                    response_data['status'] = str(e)
                    print(e)

        else:
            response_data['status'] = 'Request Invalid'

        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
            )
    else:
        raise Http404("NOT ALLOWED")

@csrf_exempt
def update_information1(request):
    if request.method == "POST":
        post = json.loads(request.body.decode("utf-8"))
        print(post)
        response_data = {}
        if post.get("key") == "70b66a89929e93416d2ef535893ea14da331da8991cc7c74010b4f3d7fabfd62":
            user_id = post['user_id']
            latitude = post['latitude']
            longitude = post['longitude']
            
            try:
                a = Information1()
                a.user_id= user_id
                a.latitude= latitude
                a.longitude= longitude
                
                a.save()
                response_data['status'] = 'true'
            except Exception as e:
                    response_data['status'] = str(e)
                    print(e)

        else:
            response_data['status'] = 'Request Invalid'

        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
            )
    else:
        raise Http404("NOT ALLOWED")

@csrf_exempt
def update_information2(request):
    if request.method == "POST":
        post = json.loads(request.body.decode("utf-8"))
        print(post)
        response_data = {}
        if post.get("key") == "70b66a89929e93416d2ef535893ea14da331da8991cc7c74010b4f3d7fabfd62":
            user_id = post['user_id']
            video_id = post['video_id']
            video_count = post['video_count']
    
            try:
                a = Information2()
                a.user_id= user_id
                a.video_count= video_count
                a.video_id= video_id
                
                a.save()
                response_data['status'] = 'true'
            except Exception as e:
                    response_data['status'] = str(e)
                    print(e)

        else:
            response_data['status'] = 'Request Invalid'

        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
            )
    else:
        raise Http404("NOT ALLOWED")


@csrf_exempt
def update_information3(request):
    if request.method == "POST":
        post = json.loads(request.body.decode("utf-8"))
        print(post)
        response_data = {}
        if post.get("key") == "70b66a89929e93416d2ef535893ea14da331da8991cc7c74010b4f3d7fabfd62":
            user_id = post['user_id']
            speed = post['speed']
            video_frquency = post['video_frquency']
            
            try:
                a = Information3()
                a.user_id= user_id
                a.speed= speed
                a.video_frquency= video_frquency
                
                a.save()
                response_data['status'] = 'true'
            except Exception as e:
                    response_data['status'] = str(e)
                    print(e)

        else:
            response_data['status'] = 'Request Invalid'

        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
            )
    else:
        raise Http404("NOT ALLOWED")


class postList(APIView):

   def get(self, request):
    
      allpost = Information.objects.order_by('android_id', '-time')
      serializer = postSerializer(allpost, many=True)
      return Response(serializer.data)

   def post(self):
      pass




class postList2(APIView):

   def get(self, request):
    
      allpost = Sendtotab.objects.all()
      serializer = postSerializer2(allpost, many=True)
      return Response(serializer.data)

   def post(self):
      pass

