import requests
import DateHandler

def HandleChoice1():
    print("Enter A Date(DD-MM-YYYY):")
    date = input()
    if(DateHandler.ValidateDate(date)):
        Formatted_Date = DateHandler.FormatDate(date)
        find=False
        temperature=0
        for item in Weather_Data:
            if Formatted_Date in item.get("dt_txt"):
                temperature=item["main"]["temp"]
                find=True
                break
        if(find):
            print(f"\n ====> Temperature = {temperature} <====\n")
        else:
            print("\n-----No Data Available for this Date!!------\n")

    else:
        print("\n-------⚠ Error: Enter a Valid Date(DD-MM-YYYY)!!--------\n")

def HandleChoice2():
    print("Enter A Date(DD-MM-YYYY):")
    date = input()
    if(DateHandler.ValidateDate(date)):
        Formatted_Date = DateHandler.FormatDate(date)
        find=False
        wind_speed=0
        for item in Weather_Data:
            if Formatted_Date in item.get("dt_txt"):
                wind_speed=item["wind"]["speed"]
                find=True
                break
        if(find):
            print(f"\n ====> Wind Speed = {wind_speed} <====\n")
        else:
            print("\n-----No Data Available for this Date!!------\n")
    else:
        print("\n-------⚠ Error: Enter a Valid Date(DD-MM-YYYY)!!--------\n")

def HandleChoice3():
    print("Enter A Date(DD-MM-YYYY):")
    date = input()
    if(DateHandler.ValidateDate(date)):
        Formatted_Date = DateHandler.FormatDate(date)
        find=False
        pressure=0
        for item in Weather_Data:
            if Formatted_Date in item.get("dt_txt"):
                pressure=item["main"]["pressure"]
                find=True
                break
        if(find):
            print(f"\n ====> Pressure = {pressure} <====\n")
        else:
            print("\n-----No Data Available for this Date!!------\n")
    else:
        print("\n-------⚠ Error: Enter a Valid Date(DD-MM-YYYY)!!--------\n")

if __name__=='__main__':
    URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    res = requests.get(URL)
    es = requests.get(URL)
    Weather_Data = res.json().get("list")
    while True:
        print(
            "\n Hey, Welcome to Weather Station Console! ☁\n Please Select a choice of action: \n 1. Temperature. 🌡\n 2. Wind Speed. 💨 \n 3. Pressure. 🧪\n 0. Terminate Program ❌"
        )
        try:
            choice = int(input())
            if choice == 0:
                print("\n Thank You for Calling weather Station. Hava A Nice Day! 🌻 \n")
                break
            elif choice == 1:
                HandleChoice1()
            elif choice == 2:
                HandleChoice2()
            elif choice == 3:
                HandleChoice3()
            else:
                print("\n-----------⚠ Error: You have entered wrong Choice!--------------\n")
        except ValueError:
            print("\n----------⚠ Error: Please Select a numercial choice!------------\n")