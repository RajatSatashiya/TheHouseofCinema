
from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title("API Weather")
root.geometry("400x400")

def ziplookup():
    #zip.get()
    #ziplabel = Label(root,text=zip.get())
    #ziplabel.grid(row=1,column=0,columnspan=2)

    try:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zip.get()+"&distance=5&API_KEY=0D2099A6-E8F4-4A68-9EC8-85881C4B746F")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#00e400"
        elif category == "Moderate":
            weather_color = "#ffff00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff7e00"
        elif category == "Unhealthy":
            weather_color = "#ff0000"
        elif category == "Very Unhealthy":
            weather_color = "#99004c"
        elif category == "Hazardous":
            weather_color = "#7e0023"

        root.configure(background=weather_color)
        
        mylabel = Label(root,text=city + " " + "Air Quality: " +  str(quality), font=("georgia",20),background=weather_color)
        mylabel.grid(row=1,column=0,columnspan=2)
    
    except Exception as e:
        api = "Error...."

zip = Entry(root)
zip.grid(row=0,column=0,sticky=W+E+N+S)

zipbutton = Button(root,text="Lookup Zipcode",command=ziplookup)
zipbutton.grid(row=0,column=1)



#air now api password : ygZc9KLJEEJ29@!
#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=0D2099A6-E8F4-4A68-9EC8-85881C4B746F
root.mainloop()
