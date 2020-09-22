#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Don't forget the "pip install pynput"
from pynput.keyboard import Key, Controller
import time

keypress = Controller()

# Variables
textToPress = 'PhineasPhreak'

time.sleep(4)

# Create new tab for your navigator and defind a address is 'monip.org'
keypress.press(Key.ctrl_l), keypress.press("t")
keypress.release(Key.ctrl_l), keypress.release("t")

for address in "monip.org":
    keypress.press(address)
    keypress.release(address)

keypress.press(Key.enter)
keypress.release(Key.enter)

time.sleep(5)
keypress.press(Key.f5)
keypress.release(Key.f5)
