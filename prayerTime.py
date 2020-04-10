import requests
import re
import datetime
import time

def strToTime(time):
    timeArray = str.split(str(time), ':')
    return datetime.datetime.now().replace(hour=int(timeArray[0]), minute=int(timeArray[1]), second=0)


def getPrayerTimes(today=False):
    server = "https://www.e-solat.gov.my/index.php"
    date = str(datetime.date.today() + datetime.timedelta(days=1))
    params = {"r": "esolatApi/TakwimSolat", "zone": "WLY01",
              "period": "today" if today else "date", "date": date}
    try:
        r = requests.get(server, params)
        return r.json()["prayerTime"][0]
    except requests.exceptions.RequestException:
        return []

def getNext(prayerTimes):
    prayerTimeNames = ["fajr", "syuruk", "dhuhr", "asr", "maghrib", "isha"]
    FMT = '%H:%M:%S'
    if not prayerTimes:
        prayerTimes = getPrayerTimes(True)
    if not prayerTimes:
        return [0,0], "Fail to fetch data. (0:0)", [] 
    nextPrayer = ""
    for name in prayerTimeNames:
        if datetime.datetime.now().replace(second=59) < strToTime(prayerTimes[name]):
            nextPrayer = name
            break

    if nextPrayer == "":
        nextPrayer = prayerTimeNames[0]
        prayerTimes = getPrayerTimes()

    nextPrayerCap = nextPrayer.capitalize()
    tdelta = datetime.datetime.strptime(
        prayerTimes[nextPrayer], FMT) - datetime.datetime.strptime(str(datetime.datetime.now().replace(second=0).strftime(FMT)), FMT)
    tDiff = [(int(i)) for i in str.split(str(datetime.timedelta(seconds=tdelta.seconds)), ":")]

    timeLeft = []
    timeLeft.append(str(tDiff[0]) + " hour" + \
        ("s" if tDiff[0] > 1 else "") if tDiff[0] != 0 else "")
    timeLeft.append(str(tDiff[1]) + " minute" + \
        ("s" if tDiff[1] > 1 else "") if tDiff[1] != 0 else "")
    timeLeft = [x for x in timeLeft if x]
    return tDiff, nextPrayerCap+" ("+prayerTimes[nextPrayer][:-3]+")", prayerTimes
