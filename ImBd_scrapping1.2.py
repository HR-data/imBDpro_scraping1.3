import time
import pandas as pd
import numpy as np
from tqdm import tqdm
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.request import urlopen as uReq

#Automation
chrome_path = r"C:\Users\Jarvis\Desktop\chromedriver.exe"
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
browser = webdriver.Chrome(chrome_path,options=chrome_options)
browser.get("https://secure.imdb.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fregistration%2Fap-signin-handler%2Fimdb_pro_us&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_pro_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl9wcm9fdXMiLCJyZWRpcmVjdFRvIjoiaHR0cHM6Ly9wcm8uaW1kYi5jb20vIn0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
usernameStr = "raj406627@gmail.com"
passwordStr = "Rajdata123@"
username = browser.find_element_by_id('ap_email')
username.send_keys(usernameStr)
password = browser.find_element_by_id('ap_password')
password.send_keys(passwordStr)
nextButton = browser.find_element_by_id('signInSubmit')
nextButton.click()

#scrapping
req_url = 'https://pro.imdb.com/inproduction?ref_=hm_nv_tt_tmm#type=movie%2CtvSeries%2CtvEpisode%2CtvMovie%2CtvMiniSeries&country=US%2CGB%2CCA%2CAU%2CFR&filmingLocation=india&sort=ranking&pos=0'
browser.get(req_url)
res=browser.execute_script("return document.documentElement.outerHTML")
soup=BeautifulSoup(res,'lxml')
t=soup.findAll("div",{"class":"full_page logged_in default_search"})
print(len(t))