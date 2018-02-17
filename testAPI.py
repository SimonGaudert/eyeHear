import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.cloud import storage

def getCredentials():
	storage_client = storage.Client.from_service_account_json(
	        'eyeHear-cad56858f9be.json')
	return storage_client
	# buckets = list(storage_client.list_buckets())
	# print(buckets)

def instantiateClient():
	# Instantiates a client
	client = vision.ImageAnnotatorClient(
		credentials=getCredentials())

	# The name of the image file to annotate
	file_name = os.path.join(
	    os.path.dirname(__file__),
	    'images/demo-image.jpg')

	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
	    content = image_file.read()

	image = types.Image(content=content)

	# Performs label detection on the image file
	response = client.label_detection(image=image)
	# labels = response.label_annotations

	# print('Labels:')
	# for label in labels:
	#     print(label.description)

instantiateClient()
