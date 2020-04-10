from sense_hat import SenseHat
import nmap
import time

sense = SenseHat()
sense.set_rotation(270)
sense.low_light = True
number = [
0,1,1,1, # Zero
0,1,0,1,
0,1,0,1,
0,1,1,1,
0,0,1,0, # One
0,1,1,0,
0,0,1,0,
0,1,1,1,
0,1,1,1, # Two
0,0,1,1,
0,1,1,0,
0,1,1,1,
0,1,1,1, # Three
0,0,1,1,
0,0,1,1,
0,1,1,1,
0,1,0,1, # Four
0,1,1,1,
0,0,0,1,
0,0,0,1,
0,1,1,1, # Five
0,1,1,0,
0,0,1,1,
0,1,1,1,
0,1,0,0, # Six
0,1,1,1,
0,1,0,1,
0,1,1,1,
0,1,1,1, # Seven
0,0,0,1,
0,0,1,0,
0,1,0,0,
0,1,1,1, # Eight
0,1,1,1,
0,1,1,1,
0,1,1,1,
0,1,1,1, # Nine
0,1,0,1,
0,1,1,1,
0,0,0,1
]

champ = False
a = "<MAC Address>"  # green
b = "<MAC Address>"  # blue
r = "<MAC Address>"  # red
q = "<MAC Address>"  # neon
f = "<MAC Address>"  # chocolate
m = "<MAC Address>"  # pink
l = "<MAC Address>"  # yellow
n = "<MAC Address>"  # purple

y = ""
ma = "<MAC Address>"
s = "<MAC Address>"
k = "<MAC Address>"

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (255, 0, 255)
neon = (0, 255, 255)
chocolate = (210, 105, 30)
pink = (255, 105, 180)

all = [a, b, r, q, f, m, l, n] if champ else [ma, f, m, s, k]

hour_color = red
minute_color = neon
empty = black

clock_image = [
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0
]

def drawTime(hour, minute, result=[]):
    # Map digits to the clock_image array
    pixel_offset = 0
    index = 0
    for index_loop in range(0, 4):
        for counter_loop in range(0, 4):
            #if (hour >= 10):
            clock_image[index] = number[int(hour/10)*16+pixel_offset]
            clock_image[index+4] = number[int(hour%10)*16+pixel_offset]
            clock_image[index+32] = number[int(minute/10)*16+pixel_offset]
            clock_image[index+36] = number[int(minute%10)*16+pixel_offset]
            pixel_offset = pixel_offset + 1
            index = index + 1
        index = index + 4

    # Color the hours and minutes
    for index in range(0, 64):
        if (clock_image[index]):
            if index < 32:
                clock_image[index] = hour_color
            else:
                clock_image[index] = minute_color
        else:
            clock_image[index] = empty

    # Display the time
    sense.low_light = True # Optional
    if champ:
        clock_image[0] = green if a in result else black
        clock_image[8] = blue if b in result else black
        clock_image[16] = red if r in result else black
        clock_image[24] = neon if q in result else black
    else:
        #clock_image[16] = red if y in result else black
        clock_image[24] = neon if ma in result else black
    clock_image[32] = chocolate if f in result else black
    clock_image[40] = pink if m in result else black
    if champ:
        clock_image[48] = yellow if l in result else black
        clock_image[56] = purple if n in result else black
    else:
        clock_image[48] = yellow if s in result else black
        clock_image[56] = purple if k in result else black
    sense.set_pixels(clock_image)

def getAttendance():
    nm = nmap.PortScanner()
    nm.scan(hosts='192.168.0.0/24', arguments='-n -sP -PE -PA21,23,80,3389')

    hosts_list = [(nm[x]['addresses']['mac'] if 'mac' in nm[x]
                ['addresses'] else '') for x in nm.all_hosts()]

    return [x for x in hosts_list if x in all]


O = black
V = green
X = red

def animOn():
    on = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
    ]
    x = [32, 41, 50, 43, 36, 29, 22, 15]
    for i in x:
        on[i] = V
        sense.set_pixels(on)
        time.sleep(.1)

def animOff():
    off = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
    ]
    x = [0, 9, 18, 27, 36, 45, 54, 63, 7, 14, 21, 28, 35, 42, 49, 56]
    for i in x:
        off[i] = X
        sense.set_pixels(off)
        time.sleep(.05)

def animAzan():
    god = [
        O, O, O, O, O, O, O, V,
        O, O, O, O, O, O, V, V,
        O, O, O, O, V, O, V, V,
        O, O, V, O, V, O, V, V,
        O, V, V, O, V, O, V, V,
        V, O, V, O, V, O, V, V,
        V, O, V, O, V, O, V, V,
        V, V, V, V, V, V, V, V
    ]

    great = [
        O, O, O, O, O, O, O, V,
        O, O, O, O, O, V, O, V,
        O, O, O, O, V, O, O, V,
        O, O, O, O, V, O, O, V,
        O, O, O, O, V, O, O, V,
        O, O, V, V, V, O, O, V,
        O, V, O, O, O, O, O, V,
        V, O, O, V, O, O, O, V
    ]
    delay = 1.5
    for i in range(0, 2):
        sense.set_pixels(god)
        time.sleep(delay)
        sense.set_pixels(great)
        time.sleep(delay)

def animSplash():
    first = [
        V, V, V, V, V, V, V, O,
        O, O, O, O, O, O, V, O,
        O, V, V, V, V, O, V, O,
        O, V, O, O, V, O, V, O,
        O, V, O, V, V, O, V, O,
        O, V, O, O, O, O, V, O,
        O, V, V, V, V, V, V, O,
        O, O, O, O, O, O, O, O
    ]

    second = [
        O, O, O, O, O, O, O, V,
        O, V, V, V, V, V, O, V,
        O, V, O, O, O, V, O, V,
        O, V, O, V, O, V, O, V,
        O, V, O, V, V, V, O, V,
        O, V, O, O, O, O, O, V,
        O, V, V, V, V, V, V, V,
        O, O, O, O, O, O, O, O
    ]

    third = [
        O, O, O, O, O, O, O, O,
        O, V, V, V, V, V, V, O,
        O, V, O, O, O, O, V, O,
        O, V, O, V, V, O, V, O,
        O, V, O, V, O, O, V, O,
        O, V, O, V, V, V, V, O,
        O, V, O, O, O, O, O, O,
        O, V, V, V, V, V, V, V
    ]

    fourth = [
        O, O, O, O, O, O, O, O,
        V, V, V, V, V, V, V, O,
        V, O, O, O, O, O, V, O,
        V, O, V, V, V, O, V, O,
        V, O, V, O, V, O, V, O,
        V, O, V, O, O, O, V, O,
        V, O, V, V, V, V, V, O,
        V, O, O, O, O, O, O, O
    ]
    delay = .08
    for i in range(0, 10):
        sense.set_pixels(first)
        time.sleep(delay)
        sense.set_pixels(second)
        time.sleep(delay)
        sense.set_pixels(third)
        time.sleep(delay)
        sense.set_pixels(fourth)
        time.sleep(delay)
