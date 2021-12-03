import requests
from time import sleep
from bs4 import BeautifulSoup
import os

print("LOGS:")
print("[1] Opening the newest version from github...")
url = "https://raw.githubusercontent.com/ishineee/youtube-dwnloader/main/Youtube_Downloader.py?token=ATGAC5WOYQWHXAWV52CYEQTBVJ25S"
print("Done.")
print("[2] Checking if Youtube_Downloader.py exists...")
directory = os.getcwd()
r = requests.get(url)

f = open("Youtube_Downloader.py",'w')
print(type(r.content))
dowolnie = r.content
dowolnie = dowolnie.decode("utf-8")
f.write(dowolnie)
print("Done.")
print("[3] Starting the protocol...")

print("Done.")
print("Newest version has been downloaded. Have fun!\n Closing Program in 2 seconds.")
sleep(2)