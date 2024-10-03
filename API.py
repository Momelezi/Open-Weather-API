import requests

def get_weather_data(city, api_key):
    # OpenWeather API endpoint for current weather
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Sending a request to OpenWeather API
    response = requests.get(url)
    
    # Checking if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Parsing weather data
        city_name = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Displaying the summary
        print(f"Weather in {city_name}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather_description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"Failed to get weather data for {city}. Error code: {response.status_code}")

# Main function
if __name__ == "__main__":
    api_key = "bd83c4dc33e82200b4493232e1c555a9"
    city = input("Enter the city name: ")
    get_weather_data(city, api_key)
