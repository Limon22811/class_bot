# Class Bot for ACC by Nahian Labib Limon

### Feature
    🔵 Read google spreadsheet 1s before class
    🔵 you can specify web browser
    🔵 support Windows, Linux & Mac
    🔵 Fast & Lite because command line application
    🔵 User friendly
    🔵 You don't need to do anything

### Installation:
Listen all you gotta need is python3.9.x and python3.8 will work as well
Make sure you run:  ```python3.x -m pip install -r requirements.txt``` or ```python3.x -m pip install gspread```
That's it.
## Instruction
Now before you jump into the program follow the below instruction its mandatory.
##### Spreadsheet Setup
    
And yes you need match your spreadsheet according to my one.
Here is the sample:
![](https://github.com/Limon22811/class_bot/blob/main/image/spreadsheet.PNG)
I use `=importrange('another-spreadsheet_url','sheet_name!A:B')` to my spreadsheet
it will sync th original class spreadsheet to my spreadsheet.

##### Browser Preferrence
If you are running this script or command line application for the first time it will ask you to choose what type of
browser do you want to run this operation. It will look something like this.
```What type of browser will you use for opening zoom link?
                [1] Firefox
                [2] Chromium web browser
                [3] Opera
                [4] Safari/Webkit
        ❯
```
###### [1] Firefox - it means Firefox based browser for example:
- Firefox
- Waterfox 
- Tor Browser 
- Firefox Nightly 
- Firefox Beta 
- Firefox Developer Edition
###### [2] Chromium web browser - it means chromium based browser like:
- Google Chrome 
- Google Chrome Beta 
- Google Chrome Canary 
- Brave 
- Chromium 
- Microsoft Edge
###### [3] Opera - it means product of opera:
- Opera
- Opera GX
###### [4] Safari/Webkite - Support safari and webkit browser
- Safari
- Webkit
##### Browser Path
And finally you need to enter the browser path or location.
For example If you have selected firefox then for Windows user:
```‪C:\Program Files\Mozilla Firefox\firefox.exe```
For linux and Mac Users:
```/usr/lib/firefox/firefox.sh```
That's it.
##### Reset Browser Config
Just delete the `user_data.json` file.
