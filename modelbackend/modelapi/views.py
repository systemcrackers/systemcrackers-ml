from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
import tensorflow as tf
from modelbackend.settings import BASE_DIR
from keras.models import load_model
import numpy as np
from keras.utils import load_img, img_to_array
import os 
from .models import Predictor
from modelbackend import settings

# Create your views here.

class ModelApi(APIView):
    def post(self, request):
        model = load_model(os.path.join(BASE_DIR, 'model_1.h5'))
        obj = Predictor.objects.create(image = request.data["files"])
        obj.save()
        path = os.path.join(settings.BASE_DIR, r'media/predict/modelimg.png')
        test_image = load_img(path, target_size = (32,32))
        test_image = img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)
        if result[0][0] == 1:
            pred = 'Corrected'

        elif result[0][1] == 1:
            pred = 'Normal'

        elif result[0][2] == 1:
            pred = 'Reversal'

        else:
            pred = "Nothing"

        os.remove(path)
        return Response({'status': "200", 'pred' :pred})

        

