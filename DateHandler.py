from datetime import datetime

def FormatDate(date):
    l=date.split("-")
    day = "0"+l[0] if(len(l[0])==1) else l[0]
    month = "0"+l[1] if(len(l[1])==1) else l[1]
    year = l[2]
    newDate = "-".join([year,month,day])
    return newDate

def ValidateDate(date):
    try:
        dateObj = datetime.strptime(date, "%d-%m-%Y")
        return True
    except ValueError:
        return False