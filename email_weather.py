import time
import datetime 
import requests, json
import smtplib
import getpass


base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = "9fb446f95425c3d706ba6cf52fec1969"
#city_name = input("Enter city name: ")
city_name = 'Bengaluru'

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":
  y = x["main"]
  current_temperature = y["temp"]
  current_pressure = y["pressure"]
  current_humidity = y["humidity"]
  z = x["weather"]
  
  weather_description = z[0]["description"]
  

  smtpObj = smtplib.SMTP('smtp.gmail.com',587)
  smtpObj.starttls()
  pwd = getpass.getpass(prompt='Password: ', stream=None)
  my_email = input("\nEnter your email")
  smtpObj.login(my_email, pwd)
  recipient = my_email

  email_body = 'Subject: Weather\n.' + "Temperature = " + str(current_temperature-273) + "\n atmospheric pressure (in hPa unit) = " + str(current_pressure) + \
     "\n humidity (in percentage) = " + str(current_humidity) + \
     "\n description = " + str(weather_description) 
  smtpObj.sendmail(my_email, recipient, email_body)
  smtpObj.quit()
else:
	print("City not found")



