from tkinter import *
import requests
import json

root = Tk()
root.title("Air Index Checker")
root.geometry("600x150")

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=89129&distance=25&API_KEY=E3ECB789-C861-4D14-8346-96999AEFBBFC


# Create a lookup function to search for specified zip codes
def zipLookup():
    global myFrame
    # zipShow = Label(root, text=zipBox.get())
    # zipShow.grid(row=1, columnspan= 2, column=0)

    myFrame.destroy()
    try:
        api_req = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + str(zipBox.get()) + "&distance=25&API_KEY=E3ECB789-C861-4D14-8346-96999AEFBBFC")
        api = json.loads(api_req.content)

        city = api[0]['ReportingArea']
        quality = str(api[0]['AQI'])
        category = api[0]['Category']['Name']

        if category == 'Good':
            myColor = "#0C0"
        elif category == 'Moderate':
            myColor = "#FFFF00"
        elif category == 'Unhealthy for Sensitive Groups':
            myColor = "#ff9900"
        elif category == 'Unhealthy':
            myColor = "#FF0000"
        elif category == 'Very Unhealthy':
            myColor = "#990066"
        elif category == 'Hazardous':
            myColor = "#660000"

        root.configure(background=myColor)

        myFrame = LabelFrame(root, bg=myColor,
                             )  # INTERNAL PADDING

        myFrame.grid(row=1, column=0, columnspan=2)  # EXTERNAL PADDING

        myLabel = Label(myFrame, text=city + " Air Quality " + quality +
                        " " + category, font=("Helvetica", 20), bg=myColor)
        myLabel.grid(row=0, columnspan=2, column=0)

    except Exception as e:
        api = "Error"


zipBox = Entry(root)
zipBox.grid(row=0, column=0, sticky=W+E+N+S)

zipBtn = Button(root, text="Lookup Air Quality", command=zipLookup)
zipBtn.grid(row=0, column=1, sticky=W+E+N+S)

myFrame = LabelFrame(root, text="First Frame", padx=40,
                     pady=50)  # INTERNAL PADDING

myFrame.grid(row=1, column=0, columnspan=2)  # EXTERNAL PADDING


root.mainloop()
