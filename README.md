# Class Bot for S7 by Nahian Labib Limon

### Feature
    🔵 Read google spreadsheet 1s before class
    🔵 you can specify web browser
    🔵 support Windows, Linux & MacOS
    🔵 User friendly
    🔵 You don't need to do anything

### Installation:
Listen all you gotta need is python3.9.x and python3.8 will work as well
Make sure you run:  
```python3.x -m pip install -r requirements.txt``` or ```python3.x -m pip install gspread```
   
  

After installation make sure you configure the right path in browser() function at path section just enter the 
browser path with application as well sample is given the script. I use firefox since it doesn't f up my privacy 
and its fast. You can choose yours.
Here is the sample:
```python
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
```
On the `'firefox'` section you enter your browser or any browser or your name as your wish.
and `webbrowser.Mozilla(path)` if your using google chrome use `webbrowser.Chrome(path)`
And if your using other browser and super confuse then let me save you:
```python
webbrowser.register('name_whatever_you_wish',
                        None,
                        webbrowser.BackgroundBrowser(path))
    webbrowser.get('name_whatever_wish').open_new_tab(url)
```

And yes you need match your spreadsheet according to your class.
My spreadsheet was shitty so i create my own structure like this
![](https://github.com/Limon22811/class_bot/blob/main/image/spreadsheet.PNG)
I use `=importrange('another-spreadsheet_url','sheet_name!A:B')`
it will sync my original class spreadsheet to this spreadsheet if any changes were made on that spreadsheet.
