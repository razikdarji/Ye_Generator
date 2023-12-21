from openai import AzureOpenAI
import os
import json
# from kanye import get_kanye_quote

client = AzureOpenAI(
	api_key	= os.getenv("AZURE_OPENAI_KEY"),
	api_version = "2023-12-01-preview",
	azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
)

#from somewhere import dalle_client  # Import your DALL-E client setup

def generate_dalle_image(prompt):
	# Code to generate an image using DALL-E with the given prompt
	# This will depend on how your DALL-E API client is set up
	image = client.images.generate(
		model = "dalle3", 
		prompt = prompt
	)
	json_response = json.loads(image.model_dump_json())
	#print(json_response)
	image_dir = os.path.join(os.curdir, 'images')
	#print("end function")
	return json_response['data'][0]['url']
