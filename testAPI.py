# import io
# import os
# Imports the Google Cloud client library
# from google.cloud import vision
# from google.cloud.vision import types
# from google.cloud import storage 
import requests
import json 
import cv2
import base64
from getImage import capture
from textToSpeech import speak

def sendWebRequest(readType, image_url): 
    url = 'https://vision.googleapis.com/v1p1beta1/images:annotate?key=AIzaSyC5FQW1UL-jZ9xq7ibfh1ZcfCP_6G0XpUA'
    if readType == "text":
        type = "TEXT_DETECTION"
    elif readType == "image":
        type = "WEB_DETECTION"
    elif readType == "label":
        type = "LABEL_DETECTION"

    data = '''{
          "requests": [
            {
              "image": {
                "content": "'''+ image_url + '''"
              },
              "features": [
                {
                  "type": "'''+ type + '''"
                }
              ]
            }
          ]
        }'''

    print (data)
    response = requests.post(url, data=data)
    if(response.ok):
        jData = json.loads(response.content)
        # print (jData)
        if readType == "text":
            return (jData['responses'][0]['textAnnotations'][0]['description'])
        elif readType == "image":
            return (jData['responses'][0]['webDetection']['webEntities'][0]['description'])
        elif readType == "label":
            return (jData['responses'][0]['labelAnnotations'][0]['description']+ " and "+jData['responses'][0]['labelAnnotations'][2]['description'])


if __name__ == '__main__':
    capture()
    with open("./snapShot.png", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read())
        encoded_image_string = str(encoded_image)
        length = len(encoded_image_string)

        clean_string = encoded_image_string[2:(length-1)]
        image_desc = sendWebRequest("label", clean_string)
        print (image_desc)
        speak("You are looking at "+ image_desc)
