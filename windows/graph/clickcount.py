##https://gobo66g2oj.execute-api.us-east-1.amazonaws.com/dev/item/zodicalpeak
import time
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
user = input('Enter Username: ')

def waitSeconds(timeToWait):
    timerCD = timeToWait
    print('Server is dropping count request')
    for x in range(timeToWait):
        print("Trying again in " + str(timerCD) + " seconds..", end="\r", flush=True)
        timerCD = timerCD - 1
        time.sleep(1)
    print('trying...')
def getClickCount():
    while True:
        try:
            global user
            req = urllib.request.Request('https://gobo66g2oj.execute-api.us-east-1.amazonaws.com/dev/item/' + str(user))
            with urllib.request.urlopen(req) as response:
                the_page = response.read()
            newlist = str(the_page).split(":")
            clickcount = newlist[4]
            clickcount = clickcount.split(",")
            clickcount = clickcount[0]
            try:
                clickcount = clickcount.split(".")
                clickcount = clickcount[0]
            except:
                pass
        except:
            waitSeconds(10)
            continue
        if clickcount is None:
            waitSeconds(10)
            continue
        else:
            clickcount = clickcount.replace(' ', '')
            return int(clickcount)
            break

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
prevClickC = getClickCount()
a = 0
# This function is called periodically from FuncAnimation
def animate(i, xs, ys):
    global user
    global prevClickC
    temp_c = (getClickCount() - prevClickC)
    prevClickC = getClickCount()
    # Add x and y to lists
    global a
    a = a + 1
    xs.append(a)
    ys.append(temp_c)

    # Limit x and y lists to 20 items
    xs = xs[-50:]
    ys = ys[-50:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    #plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title(str(user) + "'s Change In CPM Over 10 Seconds")
    plt.ylabel('Change in clicks')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=10000)
plt.show()

