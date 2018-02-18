# import io
# import os
# Imports the Google Cloud client library
# from google.cloud import vision
# from google.cloud.vision import types
# from google.cloud import storage 
import requests
import json 

def sendWebRequest(readType, image_url): 
    url = 'https://vision.googleapis.com/v1p1beta1/images:annotate?key=AIzaSyC5FQW1UL-jZ9xq7ibfh1ZcfCP_6G0XpUA'
    if readType == "text":
        type = 'TEXT_DETECTION'
    elif readType == "image":
        type = "WEB_DETECTION"

    data = '''{
          "requests": [
            {
              "image": {
                "source": {
                  "imageUri": "'''+ image_url + '''"
                }
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
    print (response)
    if(response.ok):
        jData = json.loads(response.content)
        if readType == 'text':
            print (jData['responses'][0]['textAnnotations'][0]['description'])
        elif readType == 'image':
            print (jData['responses'][0]['webDetection']['webEntities'][0]['description'])


if __name__ == '__main__':
    sendWebRequest("text", "http://www.lovethispic.com/uploaded_images/39800-I-Can-Put-Text-On-A-Photo-Too.jpg")