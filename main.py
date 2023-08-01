import requests;

if __name__==__main__:
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