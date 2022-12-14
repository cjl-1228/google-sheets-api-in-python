# -*- coding: utf-8 -*-
"""Use google sheets api using python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NF0d5hjhov8bnsnLXgW1jOnC8mIHpg0h

[Read and write Google Sheet with 5 lines of Python code
](https://www.codeforests.com/2020/11/22/gspread-read-write-google-sheet/)

[Read and Write Data in Google Sheets using Python and the Google Sheets API
](https://aryanirani123.medium.com/read-and-write-data-in-google-sheets-using-python-and-the-google-sheets-api-6e206a242f20)

[Pandas套件讀寫Google Sheets試算表資料秘訣
](https://www.learncodewithmike.com/2021/06/pandas-and-google-sheets.html)

[Get Google Sheets data with Python in 1 minute 👆
](https://www.youtube.com/watch?v=2IYJ3B1ymA8)

[Python Google Sheets API Tutorial 
](https://www.youtube.com/watch?v=cnPlKLEGR7E)

<ul>
  <li>啟用Google Sheets API</li>
  <li>建立Google Sheets憑證</li>
  <li>建立Google Sheets試算表</li>
  <li>Pandas寫入Google Sheets試算表</li>
  <li>Pandas讀取Google Sheets試算表</li>
</ul>

如在本地電腦上使用需在終端機安裝

$ pip install pandas

$ pip install gspread

$ pip install google-auth
"""

from google.oauth2.service_account import Credentials    #安裝Google APIs驗證
import gspread                                           #安裝Google Sheets Python API
import pandas as pd                                      #安裝pandas套件

"""write to a sheet"""

scope = ['https://www.googleapis.com/auth/spreadsheets'] #Google擁有許多的雲端服務，所以需要定義存取的Scope(範圍)，也就是Google Sheets(試算表)
 
creds = Credentials.from_service_account_file("gs_credentials.json", scopes=scope)#將JSON憑證檔上傳至colab，傳入google-auth套件的Credentails模組(Module)，來建立憑證物件
gs = gspread.authorize(creds)

sheet = gs.open_by_url('https://docs.google.com/spreadsheets/d/1XebW4ZryhCO2MEjZ3tKf0F7wgZBZFbTR_cJ5_zbDPCk/edit?usp=sharing')  #呼叫gspread模組(Module)的open_by_url()方法(Method)，傳入Google Sheets試算表的網址
worksheet = sheet.get_worksheet(0) #選擇工作表

df = pd.DataFrame({'Yes': [10, 20], 'No': [30, 40]}) #建立一組表格

worksheet.update([df.columns.values.tolist()] + df.values.tolist()) #寫入全部檔案

"""read sheet data"""

new_df = pd.DataFrame(worksheet.get_all_records()) #獲取試算表全部的資料
print(new_df)

"""English word practice"""

scope = ['https://www.googleapis.com/auth/spreadsheets'] 
 
creds = Credentials.from_service_account_file("gs_credentials.json", scopes=scope)
gs = gspread.authorize(creds)
 
sheet = gs.open_by_url('https://docs.google.com/spreadsheets/d/1EeAt7d8jy2M_U0rXd6cwRVdhzAmzR6iXakzMExfNsJw/edit?usp=sharing') 
worksheet = sheet.get_worksheet(0) 

df = pd.DataFrame() 

new_df = pd.DataFrame(worksheet.get_all_records())

print(new_df)

import random


ch = []
en = []

for i in range(len(new_df['DAY1 辦公達人'])):
  
  ch.append(new_df['DAY1 翻譯'][i])
  en.append(new_df['DAY1 辦公達人'][i])
  #print(f"{new_df['DAY1 辦公達人'][i]:15}{new_df['DAY1 翻譯'][i]}")'

en_last = [x.strip() for x in en if x.strip()!='']
ch_last = [x.strip() for x in ch if x.strip()!='']


t=0
while True:
  i = random.randint(0, len(ch))
  if t == i :
      i = random.randint(0, len(ch))
  
  s = str(input(f"請輸入對應的英文(輸入結束即可結束程式) {ch_last[i],en_last[i]}=>："))
  if s == "結束" : break
  elif en_last[i] == s: print('\033[1;32;1m 答對了！ \033[0m')
  else: print('\033[1;31;1m 答錯了～ \033[0m')
  t = i