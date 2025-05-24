#!/usr/bin/env python3
"""
screenshot_to_esp.py

Macht einen Vollbild-Screenshot, berechnet die Durchschnittsfarbe 
und sendet "R,G,B\n" an das ESP32 über /dev/ttyUSB0 (115200 Baud).
"""

import time
import numpy as np
import serial
from PIL import ImageGrab

# --- Konfiguration ---
SERIAL_PORT = "/dev/ttyUSB0"  # ggf. anpassen (z.B. /dev/ttyACM0)
BAUDRATE    = 115200          # ESP32 üblicher Default
DELAY_BOOT  = 2               # Wartezeit, bis ESP32 nach Open-Fkt. verzögert ist

def grab_screenshot():
    """
    Macht einen Screenshot des gesamten Bildschirms
    und gibt ihn als PIL-Image im RGB-Modus zurück.
    """
    img = ImageGrab.grab()  
    return img.convert("RGB")

def avg_color(img):
    """
    Berechnet aus einem PIL-RGB-Image die 
    Durchschnittsfarbe als (r, g, b)-Tupel (0–255).
    """
    arr = np.array(img)                  # shape (H, W, 3)
    r, g, b = arr.mean(axis=(0,1))       # Mittel über Höhe+Breite
    return int(r), int(g), int(b)

def send_color_to_esp(r, g, b):
    """
    Öffnet die serielle Schnittstelle, wartet kurz und
    schickt das Kommando "r,g,b\n" ans ESP32.
    """
    with serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1) as ser:
        time.sleep(DELAY_BOOT)            # Abwarten von ESP32-Reset
        cmd = f"{r},{g},{b}\n".encode()
        ser.write(cmd)
    print(f"Gesendet an ESP: R={r}, G={g}, B={b}")

def main():
    # 1) Screenshot wird geholt
    img = grab_screenshot()
    # 2) Durchschnittsfarbe wird berechnet
    r, g, b = avg_color(img)
    print(f"Durchschnittsfarbe: R={r}, G={g}, B={b}")
    # 3) an ESP32 gesendet
    send_color_to_esp(r, g, b)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(1)
