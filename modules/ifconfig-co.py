#!/bin/env python3
# -*- coding: utf-8 -*-
#
# The best tool to find your own IP address, and information about it.
# https://ifconfig.co/
#


import argparse
import textwrap
import json
import requests
from timeit import timeit


# Link for the requests
status_link = "https://ifconfig.co/"
req_link = "https://ifconfig.co/json"


def status():
    """
    Show the server status
    """
    server = requests.get(status_link).status_code
    execution = timeit() * 60
    tmp_second = "{:,.2f}".format(execution)
    return server, tmp_second


def show_all():
    """
    Show all information in json format
    """
    try:
        answer_all = requests.get(req_link).json()
        json_answer = json.dumps(answer_all, indent=4)
        return json_answer

    except requests.exceptions.ConnectionError as req_error:
        return f"Failed to establish a connection\n\n" f"{req_error.args}"


def ifconfig(code):
    """
    Show all output for specific code
    List code : ip, ip_decimal, country, country_iso, country_eu,
                latitude, longitude, time_zone, asn, asn_org, hostname,
                user_agent, product, version, raw_value
    """
    try:
        answer_req = requests.get(req_link).json()
        json_answer = json.dumps(answer_req[code], indent=4).strip('"')
        json_answer_user_agent = json.dumps(
            answer_req["user_agent"]["raw_value"], indent=4
        ).strip('"')
        return json_answer, json_answer_user_agent

    except ConnectionError as req_error:
        return req_error

    except requests.exceptions.ConnectionError as con_error:
        return con_error


parser = argparse.ArgumentParser(
    formatter_class=argparse.RawTextHelpFormatter,
    description=textwrap.dedent(
        """\
What is my IP address?
The best tool to find your own IP address, and information about it.
Site : https://ifconfig.co/"""
    ),
)

# Command for STATUS SERVER
status_server = parser.add_argument_group("Show Status Server")
status_server.add_argument(
    "-z",
    "--status",
    action="store_true",
    help="Show the server status code and time",
)

# Command for ALL
all_info = parser.add_argument_group("Show All Information")
all_info.add_argument(
    "-a",
    "--all",
    action="store_true",
    help="All information : ip, country, time_zone, etc",
)

# Command for IP
options = parser.add_argument_group("Show Option")
options.add_argument(
    "-i", "--ip", action="store_true", help="What is my IP address"
)

options.add_argument(
    "-d", "--ip-decimal", action="store_true", help="Show ip in decimal"
)

options.add_argument(
    "-c", "--country", action="store_true", help="Show your country"
)

options.add_argument(
    "-C",
    "--country-iso",
    action="store_true",
    help="Show your country on ISO format",
)

options.add_argument(
    "-t", "--time-zone", action="store_true", help="Show your time zone"
)

options.add_argument(
    "-n", "--hostname", action="store_true", help="Show the hostname"
)

options.add_argument(
    "-u",
    "--user-agent",
    action="store_true",
    help="Show your User-Agent for your requests",
)

# Information version of the python file
parser.add_argument(
    "-V", "--version", action="version", version="%(prog)s version 0.1"
)

# Group for verbose or quiet
output = parser.add_mutually_exclusive_group()

# output.add_argument('-q', '--quiet', action='store_true', help='print quiet')
output.add_argument(
    "-v", "--verbose", action="store_true", help="increase output visibility"
)

args = parser.parse_args()

if args.verbose:
    if args.all:
        print(f"IP is : {ifconfig(code='ip')[0]}")
    if args.ip:
        print(f"My ip address is : {ifconfig(code='ip')[0]}")

else:
    if args.status:
        print(f"Status : {status()[0]} in {status()[1]}sec")

    if args.all:
        print(show_all())

    if args.ip:
        print(ifconfig(code="ip")[0])

    if args.ip_decimal:
        print(ifconfig(code="ip_decimal")[0])

    if args.country:
        print(ifconfig(code="country")[0])

    if args.country_iso:
        print(ifconfig(code="country_iso")[0])

    if args.time_zone:
        print(ifconfig(code="time_zone")[0])

    if args.hostname:
        print(ifconfig(code="hostname")[0])

    if args.user_agent:
        print(ifconfig(code="user_agent")[1])
