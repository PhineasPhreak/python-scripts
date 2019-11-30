#! /usr/bin/env python3
# -*- encoding: utf-8 -*-


# ----- BEGIN Manage access to less secure apps -----
# You can allow users to turn on or off access by less secure apps,
# disable their ability to allow less secure apps, or force users to always
# allow less secure apps.
#
#     1) Sign in to your Google Admin console.
#        Sign in using an administrator account, not your current
#        account ********@gmail.com
#
#     2) From the Admin console Home page, go to Securityand thenBasic settings.
#        To see Security on the Home page, you might have to click
#        More controls at the bottom.
#
#     3) Under Less secure apps, select Go to settings for less secure apps.
#
#     4) On the left, select an organizational unit where you want to manage
#        access to less secure apps.
#
#         - If you don’t select an organizational unit, your setting applies
#           to your entire top-level organization.
#
#         - If you want an organizational unit to use the same setting
#           as its parent organization, click Use Inherited on the top right.
#
#     5) Select an option:
#           Disable access to less secure apps for all users (Recommended)
#           Access to less secure apps is disabled for everyone.
#           Users can’t turn on access to less secure apps.
#           When you disable access to less secure apps while a less secure
#           app has an open connection with a user account,
#           the app will time out when it tries to refresh the connection.
#           Timeout periods vary per app.
#           Allow users to manage their access to less secure apps
#           Users can turn on or turn off access to less secure apps.
#           Enforce access to less secure apps for all users (Not recommended)
#           Access to less secure apps is required for everyone.
#           Users can’t turn off access to less secure apps.
#           This option isn't recommended, because it potentially increases
#           the exposure of user accounts to hijacking.
#           Use this option only when you want to ensure that access
#           by a less secure app is available to all users for a limited time,
#           such as for an upgrade.
#
#     6) On the bottom right, click Save.
# ----- END Manage access to less secure apps -----


# For manually enter password with
from getpass import getpass

# Use import for knows the current directory
from os import getcwd

# Import to know the host system 'LINUX' or 'WINDOWS'
import platform as plt

# For send email
import urllib.request 
import smtplib
import ssl
from email.message import EmailMessage

# For history log and csv file
from datetime import datetime
import csv


# ##### Declaration of environment variables ######
actual_time = datetime.now().strftime(format('%H:%M:%S'))
actual_date = datetime.now().strftime(format('%d/%m/%Y'))
log_file = 'history.log'
saved_ip_file = 'saved-ip.csv'
delimiter_csv = ','

api_address = 'https://api.ipify.org'
external_ip = ''
saved_external_ip = ''

password = ''
port = 587  # For starttls 587 or SSL 465
smtp_server = 'smtp.gmail.com'
sender_email = 'dejesusk38@gmail.com'
receiver_email = 'dejesusk38@gmail.com'


# Write the location of the history files and IP backup files
# according to the machine.
def machine():
    name_machine = getpass.getuser()
    if plt.system().upper() == 'WINDOWS':
        directory = f'C:\\Users\\{name_machine}\\Documents\\'
        return directory

    if plt.system().upper() == 'LINUX':
        directory = f'/home/{name_machine}/Documents/'
        return directory

    return getcwd()


# Generation of the public address with the library "urllib.requests",
# as it is available in the standard library.
def extip():
    """
    To get the external IP address.
    Other site to get this 'https://ident.me'
    """

    api_status_code = urllib.request.urlopen(api_address).getcode()
    if api_status_code == 200:
        ip = urllib.request.urlopen(api_address)\
            .read().decode('utf8')
        return ip

    return 'Site API is down...'


# Creation of the log file, with a return according to errors.
def history(try_error):
    time_and_date = f'[{actual_time}] [{actual_date}]'

    with open(file=log_file, mode='a', encoding='utf8') as file:
        file.writelines(f'{time_and_date} '
                        f'Create (or append) LOG file {log_file}\n')
        file.writelines(f'{time_and_date} IP : {external_ip}\n')
        file.writelines(f'{time_and_date} Email Send...\n')
        file.writelines(f'{time_and_date} PORT using : [{port}]\n')
        file.writelines(f'{time_and_date} SMTP SERVER : [{smtp_server}]\n')
        file.writelines(f'{time_and_date} SENDER EMAIL : [{sender_email}]\n')
        file.writelines(f'{time_and_date} '
                        f'RECEIVER EMAIL : [{receiver_email}]\n')

        if try_error == 'SMTPAuthenticationError':
            file.writelines(f'{time_and_date} '
                            f'ERROR : SMTPAuthenticationError\n')

        elif try_error == 'TimeoutError':
            file.writelines(f'{time_and_date} ERROR : TimeoutError\n')

        elif try_error == 'IP_has_not_changed':
            file.writelines(f'{time_and_date} '
                            f'SENDING : '
                            f'Sending is not necessary, same address\n')

        else:
            file.writelines(f'{time_and_date} MESSAGE : [\n{msg}]\n')


# Creation of the *.csv file for the list of all public addresses,
# with time and date
def write_saved_ip():
    # headers = ['TIME', 'DATE', 'PUBLIC IP']
    time_date_and_ip = [actual_time, actual_date, external_ip]

    with open(saved_ip_file, 'a', encoding='utf8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=delimiter_csv)
        # csv_writer.writerow(headers)
        csv_writer.writerow(time_date_and_ip)


# Read the *.csv file with the reversal of the list
# to get the last public IP address saved.
def read_saved_ip():
    with open(saved_ip_file, 'r', encoding='utf8', newline='') as read_file:
        reader = csv.reader(read_file, delimiter=delimiter_csv)
        for row in reversed(list(reader)):
            return row


# this try is for 'KeyboardInterrupt' Error
try:
    print('[*]', f'Date : {actual_date}', '\n'
          '[*]', f'Time : {actual_time}', '\n')

    print('[*]', 'Creating history files and backup IP addresses.')
    print('[*]', 'Wait a few seconds to get the public ip address...')
    external_ip = extip()  # Get the public address
    write_saved_ip()  # Ecriture du fichier 'saved_ip_file' (variable)
    print('[+]', f'Your public address is : {external_ip}', '\n')

    # Create the email content with 'Subject', 'From', 'To' and 'Content'
    msg = EmailMessage()
    msg['Subject'] = 'Changing public IP address'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    msg.set_content(f'Hi there,\n\n'
                    f'New Address is : {external_ip}\n\n'
                    f'Bye, Bye\n\n'
                    f'This message is sent from Server, Please do not reply.')

    # This try is for 'TimeoutError' and 'SMTPAuthenticationError'
    try:
        # Executing the instruction block if the public addresses are different
        if external_ip != read_saved_ip()[2]:
            # Use manually getpass or with standard input.
            password = getpass(prompt='Type your password and press enter : ')
            # password = input('Your Password : ')

            print('Email in progress, wait a few seconds.')
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(sender_email, password)
                server.send_message(msg)

            # Check if error on the history function
            print('\n[+] Sending status is OK.')
            history(try_error='')

        else:
            print('\n[+] The public IP address has not changed,\n'
                  'sending the email is not necessary.')
            history(try_error='IP_has_not_changed')

    except smtplib.SMTPAuthenticationError:
        history(try_error='SMTPAuthenticationError')
        print('\n[-] Wrong password!\n'
              f'see log({log_file}) for more information on the error.')

    except TimeoutError:
        history(try_error='TimeoutError')
        print('\n[-] A connection attempt failed because the connected\n'
              'party did not respond properly beyond a certain time\n'
              'or an established connection failed because the\n'
              'connection host did not respond\n'
              f'see log({log_file}) for more information on the error.')

except KeyboardInterrupt:
    print('\n[-] Press "CTRL-C" again to quit', '\n')
