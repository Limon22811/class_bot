from datetime import datetime
import time
import sys
import os


def clear():
    if sys.platform == 'linux' or sys.platform == 'darwin':
        os.system('clear')
    else:
        os.system('cls')


def title(title):
    if sys.platform == 'linux' or sys.platform == 'darwin':
        sys.stdout.write(f"\x1b]2;{title}\x07")
    elif sys.platform == 'win32':
        os.system(f"Title {title}")


def cell(data1, data2):
    import re
    import gspread
    # credentials = nahianlabiblimon@gmail.com
    gc = gspread.service_account(filename='credentials.json')

    sh = gc.open_by_key('1pcuMiFUVsEavYaVzshIfBHR5_juP_K_kntXN2sp-PII')
    worksheet = sh.sheet1

    link = worksheet.cell(data1, data2).value
    pattern_zoom_link = re.compile(
        r'(https://)?(zoom.us|us\d{2}web.zoom.us)/j/\d+\?pwd=.+')

    matches_url = pattern_zoom_link.search(link)
    if matches_url:
        url = matches_url.group()
        return url
    else:
        return link


def current_time(second=False):
    cyear = datetime.now().year
    cmonth = datetime.now().date().month
    cday = datetime.now().date().day
    chour = datetime.now().time().hour
    cmin = datetime.now().time().minute
    csec = datetime.now().time().second
    if second == True:
        return datetime(cyear, cmonth, cday, chour, cmin, csec)
    else:
        return datetime(cyear, cmonth, cday, chour, cmin)


def period_time(hour, minutes, second=0):
    cyear = datetime.now().year
    cmonth = datetime.now().date().month
    cday = datetime.now().date().day
    return datetime(cyear, cmonth, cday, hour, minutes, second)


def browser(link):
    import webbrowser
    url = link
    if sys.platform == 'linux' or sys.platform == 'darwin':
        path = "/usr/lib/firefox/firefox.sh"
    else:
        path = '‪C:/Program Files/Mozilla Firefox/firefox.exe'
    webbrowser.register('firefox',
                        None,
                        webbrowser.Mozilla(path))
    webbrowser.get('firefox').open_new_tab(url)


day = datetime.now().isoweekday()
x, y = [1, 2]
colm = {8: 3, 9: 5, 10: 7, 11: 9}
title("Class Bot by Nahian Labib Limon for S7")
if day not in [5, 6]:
    while period_time(7, 0) <= current_time() <= period_time(11, 35):
        if period_time(8, 5) <= current_time() <= period_time(11, 35):
            for x in range(8, 12):
                if period_time(x, 0) <= current_time() <= period_time(x, 59):
                    if period_time(x, 0) <= current_time() <= period_time(x, 35):
                        if period_time(x, 5) <= current_time():
                            clear()
                            print(f"""Current Class: {cell(day, colm[x]-1)}
    Next Class: {cell(day, colm[x]+1)}""")
                            browser(cell(day, colm[x]))
                            till = (60 - current_time().minute) * 60
                            time.sleep(till)
                        else:
                            while current_time() < period_time(x, 5):
                                clear()
                                till = period_time(x, 5) - current_time(second=True)
                                print(f'Your class is starting in {till}s...')
                                time.sleep(1)
                    else:
                        while period_time(x+1, 5) > current_time():
                            till = period_time(x+1, 5) - current_time(second=True)
                            print(f"""Please wait until your next class
    Your next class will start at {x+1}:05 AM.
    """)
                            time.sleep(till)
                else:
                    continue
        else:
            while current_time() < period_time(8, 5):
                clear()
                till = period_time(8, 5) - current_time(second=True)
                print(f'Your class is starting in {till}s...')
                time.sleep(1)
    else:
        clock = datetime.today().strftime("%I:%M %p")
        print(f"There is no class at {clock}")
        time.sleep(3)
        sys.exit()
else:
    print("Today is holiday.")
    time.sleep(3)
    sys.exit()
