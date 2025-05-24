# Für 8-Bit-RGB Screenshots

#!/usr/bin/env python3
import time
import mss
from PIL import Image
import numpy as np
import serial

def grab_screenshot():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        return Image.frombytes('RGB', sct_img.size, sct_img.rgb)

def average_color(img):
    arr = np.array(img)
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    return int(r.mean()), int(g.mean()), int(b.mean())

def send_color_to_esp(r, g, b, port='/dev/ttyUSB0', baud=115200):
    with serial.Serial(port, baud, timeout=1) as ser:
        ser.write(f"{r},{g},{b}\n".encode())

def main():
    img = grab_screenshot()
    r, g, b = average_color(img)
    print(f"Durchschnittsfarbe: R={r}, G={g}, B={b}")
    send_color_to_esp(r, g, b)

if __name__=="__main__":
    while True:
        main()
        time.sleep(1)