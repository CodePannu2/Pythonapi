import base64                  
import requests
from PIL import Image


emotions = ['happy','sad','angry','adorable']
for emotion in emotions:
	with open(f'{emotion}.png','rb') as f:
		response = requests.post(f'https://api.codepannu.com/emoji/{emotion}',params={'apiKey':'codepannustudent'},data={'img':base64.b64encode(f.read()).decode("utf8")})
		print(response.json())	

response = requests.get('https://api.codepannu.com/emoji/sad',params={'apiKey':'codepannustudent'})
print(response.json())

with open('emotions21.png','wb') as f:
	f.write(base64.b64decode(response.json()['img']))


im = Image.open('./emotions21.png')
im.show()