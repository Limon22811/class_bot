# Class Bot for ACC by Nahian Labib Limon

### Feature
    🔵 You don't need to copy or worry about changing link
    🔵 you can specify web browser
    🔵 support Windows, Linux & Mac
    🔵 Fast & Lite because command line application
    🔵 User friendly

### Installation:
Listen all you gotta need is python3.9.x and python3.8 will work as well
Make sure you run:  ```python3.x -m pip install -r requirements.txt``` or ```python3.x -m pip install gspread```
That's it.
## Instruction
Now before you jump into the program follow the below instruction its mandatory.
##### Create your own credential.json file
First got to [Google Cloud Platform](https://console.cloud.google.com/ "Google Cloud Platform")
Then Select Project or Create a Project (New Porject>>Create)
![](https://raw.githubusercontent.com/Limon22811/class_bot/main/image/Select%20Project.png)
On the search bar search `Google Sheets API` and Enable that.
After that you will see this screen and select credentials
![](https://raw.githubusercontent.com/Limon22811/class_bot/main/image/credentials.png)
Now click ont `+CREATE CREDENTIALS` and select `Service Account` 
Enter Service Account name and click done.
Now select Manage Service Account ![](https://raw.githubusercontent.com/Limon22811/class_bot/main/image/manage.png)
And click on the three dot and select manage keys ![](https://raw.githubusercontent.com/Limon22811/class_bot/main/image/manage%20key.png)
select `ADD KEY` and Select `Create new key` and select JSON
that json file will be downloaded now rename it to `credentials.json` make sure that app.py and credentials file are in the same directory.
##### Spreadsheet Setup
    
And yes you need match your spreadsheet according to my one.
Here is the sample:
![](https://raw.githubusercontent.com/Limon22811/class_bot/main/image/spreadsheet.PNG)
I use `=importrange('your_class_sheet_url','sheet_name!A:B')` to my spreadsheet
it will sync the original class spreadsheet to your spreadsheet. If your class sheet make any change then your own class sheet will made that change as well.
Now go ahead open `credentials.json` file with any text editor and copy the client_email
and click share your own spreadsheet and give viewer or editor access.

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
