from django.shortcuts import render
import datetime
import requests

# Create your views here.
def home(request):

   if 'city' in request.POST:
        city = request.POST['city']
   else:
        city = 'Karachi'  # Default city if none provided

   url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={b187aa6eeb3b8ab732e256343aba5733}'
   PARAMS = {'units': 'metric'}

   data =request.get(url,PARAMS).json()

   description = data['weather'][0]['description']
   icon = data['weather'][0]['icon']
   temp = data['main']['temp']

   day = datetime.date.today()

   return render(request, 'weatherapp/index.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day})