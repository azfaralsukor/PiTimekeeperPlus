#!/usr/bin/python
import time
from sense_hat import SenseHat
from prayerTime import getNext
from pixeling import drawTime, getAttendance, animOn, animOff, animAzan, animSplash

sense = SenseHat()
sense.set_rotation(270)
sense.low_light = True
animSplash()
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 162, 26)
black = (0, 0, 0)
purple = (255, 0, 255)

nextTime = [-1,-1]
nextStr = ""
prayerTimes = []
curTime = time.localtime()
res = []
refresh = True
on = True
held = False

def saveNext(s):
    global nextStr
    global nextTime
    nextTime = [(int(i)) for i in s[s.find("(")+1:-1].split(":")]
    nextStr = s

def handleNext():
    global prayerTimes
    _, s, prayerTimes = getNext(prayerTimes)
    saveNext(s)

handleNext()

while True:
    for event in sense.stick.get_events():
        if event.action == "held":
            held = True
        if event.action == "released" and held:
            if event.direction == "up":
                sense.show_message(nextStr, text_colour=yellow)
            held = False
        if event.action == "pressed":
            if event.direction == "up":
                nextPT, _, prayerTimes = getNext(prayerTimes)
                drawTime(nextPT[0], nextPT[1], res)
                saveNext(_)
                time.sleep(3)
            if event.direction == "middle":
                on = not on
                if on:
                    animOn()
                else:
                    animOff()
                time.sleep(1)
            if event.direction == "right":
                sense.show_message("P: " + str(round(sense.get_pressure())) + " mbars", text_colour=blue)
            if event.direction == "down":
                sense.show_message("H: " + str(round(sense.get_humidity())) + "%", text_colour=purple)
            if event.direction == "left":
                sense.show_message("T: " + str(round(sense.get_temperature())) + " C", text_colour=red)

    curTime = time.localtime()
    if curTime.tm_hour == nextTime[0] and curTime.tm_min == nextTime[1]:
        on = True
        animAzan()
        sense.show_message("It is " + nextStr + " now.", text_colour=green)
        continue

    if on:
        drawTime(curTime.tm_hour, curTime.tm_min, res)
    else:
        sense.clear()

    if curTime.tm_hour == nextTime[0] and curTime.tm_min == nextTime[1] + 1:
        handleNext()

    if curTime.tm_min % 15 == 0:
        if refresh:
            res = getAttendance()
            refresh = False
            if nextTime[0] == 0 and nextTime[1] == 0:
                handleNext()
        else:
            res += getAttendance()
    else:
        refresh = True

