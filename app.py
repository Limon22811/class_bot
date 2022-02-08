from datetime import datetime
import time
import sys
import os
import json


def clear():
    if sys.platform == 'linux' or sys.platform == 'darwin':
        os.system('clear')
    else:
        os.system('cls')


def query():
    while True:
        clear()
        browser_choice = input("""What type of browser will you use for opening zoom link?
                [1] Firefox
                [2] Chromium web browser
                [3] Opera
                [4] Safari/Webkit
        >""").lower()
        if bc == 'firefox' or bc.find('1') != -1:
            browser_choice = 'firefox'
            break
        elif bc == 'chrom' or bc.find('2') != -1 or bc.find('edge') != -1:
            browser_choice = 'chromium'
            break
        elif bc == 'opera' or bc.find('3') != -1:
            browser_choice = 'opera'
            break
        elif bc == 'safari' or bc == 'webkit' or cb.find('4'):
            browser_choice = 'safari'
            break
        else:
            continue
    while True:
        clear()
        try:
            browser_path = input(r"Enter your browser path>")
        except:
            print("Invalid!")
            time.sleep(2)
        else:
            break
    while True:
        clear()
        try:
            class_url = input("Enter your custom class url>")
        except:
            print('Invalid!')
            time.sleep(2)
        else:
            break
    data = {'browser_choice': browser_choice,
            'browser_path': browser_path, 'url': class_url}
    data_json = json.dumps(data)
    with open('user_data.json', 'w') as f:
        f.write(data_json)


def title(title):
    if sys.platform == 'linux' or sys.platform == 'darwin':
        sys.stdout.write(f"\x1b]2;{title}\x07")
    elif sys.platform == 'win32':
        os.system(f"Title {title}")


def cell(data1, data2):
    with open('user_data.json', 'r') as f:
        user_data = f.read()
    data = json.loads(user_data)
    import re
    import gspread
    gc = gspread.service_account(filename='credentials.json')
    sh = gc.open_by_url(data['url'])
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


if os.path.isfile('user_data.json'):
    pass
else:
    query()


def browser(link):
    with open('user_data.json', 'r') as f:
        user_data = f.read()
    data = json.loads(user_data)
    import webbrowser
    path = data['browser_path']
    if data['browser_choice'] == 'firefox':
        webbrowser.register(data['browser_choice'],
                            None, webbrowser.Mozilla(path))
    elif data['browser_choice'] == 'chromium':
        webbrowser.register(data['browser_choice'],
                            None, webbrowser.Chrome(path))
    elif data['browser_choice'] == 'opera':
        webbrowser.register(data['browser_choice'],
                            None, webbrowser.Opera(path))
    elif data['browser_choice'] == 'safari':
        webbrowser.register(data['browser_choice'],
                            None, webbrowser.MacOSX(path))
    webbrowser.get(data['browser_choice']).open_new_tab(link)


title('Class Bot For ACC S7')
day = datetime.now().isoweekday()
if day not in [5, 6]:
    while period_time(8, 0) <= current_time() <= period_time(11, 20):
        if period_time(8, 50) < current_time() < period_time(9, 25):
            clear()
            colm = 3
            title(f'Class Bot For ACC S7 | {cell(day,2)}')
            print(f"""Current Class: {cell(day,2)}
Next Class: {cell(day, 4)}""")
            browser(cell(day, colm))
            till = period_time(9, 25) - current_time()
            hour, minute, second = str(till).split(':')
            time.sleep(int(minute)*60 + int(second))
        elif period_time(9, 35) < current_time() < period_time(10, 10):
            clear()
            title(f'Class Bot For ACC S7 | {cell(day,4)}')
            colm = 5
            print(f"""Current Class: {cell(day,4)}
Next Class: {cell(day, 6)}""")
            browser(cell(day, colm))
            till = period_time(10, 10) - current_time()
            hour, minute, second = str(till).split(':')
            time.sleep(int(minute)*60 + int(second))
        elif period_time(10, 20) < current_time() < period_time(10, 55):
            title(f'Class Bot For ACC S7 | {cell(day,6)}')
            clear()
            colm = 7
            print(f"""Current Class: {cell(day,6)}
Next Class: {cell(day, 8)}""")
            browser(cell(day, colm))
            till = period_time(10, 55) - current_time()
            hour, minute, second = str(till).split(':')
            time.sleep(int(minute)*60 + int(second))
        elif period_time(11, 5) < current_time() < period_time(11, 40):
            clear()
            if day == 4:
                title(f'Class Bot For ACC S7 | Class Finished')
                print("Your College class has finished!")
                sys.exit()
            else:
                title(f'Class Bot For ACC S7 | {cell(day,8)}')
                colm = 9
                print(f"""Current Class: {cell(day,8)}
Next Class: {cell(day, 10)}""")
                browser(cell(day, colm))
                till = period_time(11, 40) - current_time()
                hour, minute, second = str(till).split(':')
                time.sleep(int(minute)*60 + int(second))
    else:
        clock = datetime.today().strftime("%I:%M %p")
        print(f"There is no class at {clock}")
        time.sleep(3)
        sys.exit()
else:
    print("Today is holiday.")
    time.sleep(3)
    sys.exit()
