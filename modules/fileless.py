#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import datetime


path = os.getcwd()
listing_current_dir = os.listdir(path)
date_today = datetime.date.today()

with open('Listing-{}.txt'.format(date_today), 'w') as files:
    for listing in listing_current_dir:
        files.write(listing + '\n')
