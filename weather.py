import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY') # get API key from weatherapp

# dedine a data class to structure weather information
@dataclass
class WeatherData:
    main:str # primary weather cahracterstic
    name: str # City
    description: str # detailed weather description
    icon: str
    temperature: float 

# get gepgraphic coordinates
def get_lat_lon(city_name, state_code, country_code, api_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit=10&appid={api_key}').json()
    data= resp[0]
    # print("Given JSon is", data)
    #2 variabels extractinng(get) response data from response above
    name, lat,lon = data.get('name'),data.get('lat'),data.get('lon')
    return name,lat,lon

def get_current_weather(name, lat, lon, api_key):
    resp = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
    ).json()
    # print(resp)
    data = WeatherData(
        main=resp.get('weather')[0].get('main'),
        name=name,
        description=resp.get('weather')[0].get('description'),
        icon=resp.get('weather')[0].get('icon'),
        temperature=resp.get('main').get('temp')
    )
    return data

def main(city_name, state_name, country_name):
    name, lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)
    weather_data = get_current_weather(name,lat,lon,api_key)
    return weather_data

    
if __name__ =="__main__" : 
    name, lat,lon = get_lat_lon("Daly City",'CA','US',api_key)
    print(get_current_weather(name,lat,lon,api_key))
    print("Responsed")
    

    
    
 
   


    
    
    
    