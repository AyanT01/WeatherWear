"""import requests
request = requests.get("https://official-joke-api.appspot.com/random_joke")
json = request.json()
print(json["setup"])
print(json["punchline"])
parameters = {
    "lat": 44.978718,
    "lng": -84.515887,
}

request = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
def utc_to_est(utc_time):
    temp = utc_time[:2]
    temp = int(temp) - 4
    utc_time = str(temp) + utc_time[2:]
    print(utc_time)
    return utc_time

sunrise = request.json()["results"]["sunrise"]
utc_to_est(sunrise)"""
import time

import requests
#request = requests.get("https://api.sunrise-sunset.org/json")
"""
def get_latitude_and_longitude(location = input("Enter your current location: ")):
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    path = "/usr/local/bin/chromedriver"
    service = ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=service)

    driver.get("https://www.latlong.net/")
    search = driver.find_element(by=By.CLASS_NAME,value='width70')
    search.send_keys(location)
    button = driver.find_element(by=By.ID,value="btnfind")
    button.click()
"""
#get_latitude_and_longitude()


def get_sunrise_and_sunset(latitude,longitude):
    import requests
    parameters = {
        "lat":latitude,
        "lng":longitude
    }
    request = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
def convert_to_fahrenheit(kelvin):
    result = (kelvin - 273.15) * 9 / 5 + 32
    return result
import os

def dress_type(min_temp,max_temp):
    """Get the dress type appropriate for the day based on the minimum and maximum temperature of the day."""
    if min_temp <= 25:
        result = "The temperature is quite cold. It's recommended to dress heavily and wear a Winter Jacket to stay warm."
    elif min_temp >= 45 and max_temp <= 63:
        result = "The temperature is cool. Dress in layers and consider wearing a light to medium coat to stay comfortable."
    elif min_temp <= 64 and max_temp <= 78:
        result = "The temperature is mild. A fleece jacket or a sweater would be suitable to keep you warm."
    elif min_temp <= 79 and max_temp <= 80:
        result = "The temperature is warm. You can go for short sleeves and light layers to stay comfortable."
    elif min_temp <= 80 and max_temp <= 90:
        result = "The temperature is quite warm. Light clothing like shorts and t-shirts would be very appropriate."
    else:
        result = "The temperature is hot! Consider wearing light and breathable clothing to beat the heat."
    return result

#def outdoor_activities()
def post_api():
    import requests
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = {

        "title" : 'Abdul haq',

    }
    response = requests.delete(url)
    print(response.json())

#post_api()
def est_time(time):
    """
    The openweathermap api returns a unix UTC time, so this function helps to convert it from that to readable time.
    """
    import datetime
    import pytz
    # Get the sunrise time in unix UTC
    unix_time = time
    # Convert the sunrise time to a datetime object
    unix_datetime = datetime.datetime.fromtimestamp(unix_time)
    # Get the current time zone
    timezone = pytz.timezone('America/New_York')
    # Convert the sunrise datetime object to EST
    est_time_datetime = unix_datetime.astimezone(timezone)
    # Print the EST sunrise time
    print(est_time_datetime)


def get_weather(location):
    """Using requests and an API key, I am able to access data from the *openweathermapapi* about a city or country"""
    #sunrise and sunset-> https://api.sunrise-sunset.org/json
    #location = input("Enter your current location: ")
    api_key = os.environ.get("owm_api")
    print(api_key)
    parameters = {
        "q": location,
        "appid": api_key
    }
    #print(parameters["appid"])
    #request = requests.get(f"https://api.openweathermap.org/data/2.5/weather",params=parameters)
    request = requests.get(f"https://api.openweathermap.org/data/2.5/weather",params=parameters)
    #sunrise_time = request.json()["sys"]["sunrise"]
    #sunset_time = request.json()["sys"]["sunset"]
    temp_min = request.json()["main"]["temp_min"]
    temp_max = request.json()["main"]["temp_max"]
    temp_min = round(convert_to_fahrenheit(temp_min))
    temp_max = round(convert_to_fahrenheit(temp_max))
    print(temp_min)
    print(temp_max)
    #est_time(sunrise_time)
    #est_time(sunset_time)
    current_temp = request.json()["main"]["temp"]
    current_temp = round(convert_to_fahrenheit(current_temp))
    print(f"The current temperature in {location} is {current_temp} degrees Fahrenheit.")
    print(dress_type(temp_min,temp_max))
    return dress_type(temp_min,temp_max)



import smtplib
from email.message import EmailMessage
def email_content(subject,body,to):
    """new_email = EmailMessage()
    new_email.set_content(body)
    new_email["subject"] = subject
    new_email["to"] = to
    user = "ayantayoabdulhaq7@gmail.com"
    new_email["from"] = user
    pass_word = os.environ.get("email_password")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user,pass_word)
    server.send_message(new_email)
    server.quit()"""
    password = os.environ.get("email_password")
    new_message = EmailMessage()
    new_message.set_content(body)
    new_message["subject"] = subject
    new_message["to"] = to
    user = "ayantayoabdulhaq7@gmail.com"
    new_message["from"] = user
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    password = os.environ.get("email_password")
    print(password)
    server.login(user,password=password)
    server.send_message(new_message)
    server.quit()
location = input("Enter your location: ")
def get_phone_service_and_number():
    print("""
        Available phone services:
         1. Verizon
         2. TMobile
         3. Mint Mobile
         4. AT&T
         """
        )
    while True:
        try:
            phone_service = int(input("Select the number for your phone service: "))
            break
        except:
            print("Invalid argument, enter a number between (1-4). ")
    if phone_service == 1:
        end_text = "@vtext.com"
    elif phone_service == 2:
        end_text = "@tmomail.net"
    elif phone_service == 3:
        end_text = "@tmomail.net"
    elif phone_service == 4:
        end_text = "@txt.att.net"
    phone_number = input("Enter your phone number: ")
    result = phone_number+end_text
    print(result)
    return result

number = get_phone_service_and_number()
while True:
    email_content("Dress code today",get_weather(location),number)
    time.sleep(30)
#email_content("Weather","It's cold today","abdulhaqayantayo@gmail.com")



