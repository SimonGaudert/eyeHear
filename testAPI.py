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
from naturalSpeech import readText

def sendWebRequest(image_url): 
    url = 'https://vision.googleapis.com/v1p1beta1/images:annotate?key=AIzaSyC5FQW1UL-jZ9xq7ibfh1ZcfCP_6G0XpUA'
    types = ["WEB_DETECTION", "LABEL_DETECTION"]
    v_aReadings=[]

    # send request to google vision api to get WEB_DETECTION and LABEL_DETECTION
    for type in types:
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
        response = requests.post(url, data=data)
        
        if(response.ok):
            jData = json.loads(response.content)
            if type == "WEB_DETECTION":
                v_aReadings+=(jData['responses'][0]['webDetection']['webEntities'])
            elif type == "LABEL_DETECTION":
                v_aReadings+=(jData['responses'][0]['labelAnnotations'])
    return v_aReadings

if __name__ == '__main__':
    capture()
    with open("./snapShot.png", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read())
        encoded_image_string = str(encoded_image)
        length = len(encoded_image_string)

        clean_string = encoded_image_string[2:(length-1)]
        v_aReadings = sendWebRequest(clean_string)

        number_of_labels = 0
        for i in v_aReadings:
            if i['description'][0].islower():
                number_of_labels += 1

        if v_aReadings[0]['description'].lower() == "light":
            text = "Hmmmm, I think I blinked. Please try again."
        elif v_aReadings[0]['score']>1 or v_aReadings[0]['description'].lower() == v_aReadings[len(v_aReadings)-number_of_labels]['description']:
            text = "This looks to me like you're looking at a "+ v_aReadings[0]['description']
        else:
            text = "I could be wrong, but my best guess is that you're looking at a "+ v_aReadings[0]['description'] + " or perhaps maybe " + v_aReadings[len(v_aReadings)-number_of_labels]['description']

        readText(text)
