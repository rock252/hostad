from django.shortcuts import render, Http404, HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from . serializers import *
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
from math import sin, cos, sqrt, atan2, radians


def distance(la1, lo1, la2, lo2):

    R = 6373.0
    lat1 = radians(float(la1))
    lon1 = radians(float(lo1))
    lat2 = radians(float(la2))
    lon2 = radians(float(lo2))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = R * c
    return d


def algo(tab_id, latitude, longitude):


    obj = advertiser_data.objects.all()

    if Sendtotab.objects.filter(user_id = tab_id).exists():

        a = Sendtotab.objects.get(user_id = tab_id) 
        s = 0
        for i in obj:

            d= distance(latitude, longitude, i.latitude, i.longitude)

            if d < float(i.radius):                   #convert this into an array instead of 5 links
                s = s+1
                if s ==1 :
                    a.video_id1 = i.video_id
                if s ==2 :
                    a.video_id2 = i.video_id
                if s ==3 :
                    a.video_id3 = i.video_id
                if s ==4 :
                    a.video_id4 = i.video_id
                if s ==5 :
                    a.video_id5 = i.video_id                         #need to find the ways to update data instead of creating new dataset
        a.save() 
    else:
        a = Sendtotab() 
        s = 0
        a.user_id = tab_id
        for i in obj:

            d= distance(latitude, longitude, i.latitude, i.longitude)

            if d < float(i.radius):                   #convert this into an array instead of 5 links
                s = s+1
                if s ==1 :
                    a.video_id1 = i.video_id
                if s ==2 :
                    a.video_id2 = i.video_id
                if s ==3 :
                    a.video_id3 = i.video_id
                if s ==4 :
                    a.video_id4 = i.video_id
                if s ==5 :
                    a.video_id5 = i.video_id                         #need to find the ways to update data instead of creating new dataset
        a.save()         



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

            algo(user_id, latitude, longitude)



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


class downloadvideo(APIView):

   def get(self, request):
    
      allpost = download.objects.all()
      serializer = downloadvideoserializer(allpost, many=True)
      return Response(serializer.data)

   def post(self):
      pass
