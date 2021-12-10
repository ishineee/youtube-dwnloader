import requests
from time import sleep


def downloadlatestversion():
    print("LOGS:")
    print("[1] Opening the newest version from github...")
    url = "https://raw.githubusercontent.com/ishineee/youtube-dwnloader/main/Youtube_Downloader.py"
    print("Done.")
    print("[2] Checking if Youtube_Downloader.py exists...")
    r = requests.get(url)
    f = open("Youtube_Downloader.py",'w')
    print("Done.")
    print("[3] checking the type of the raw file...")
    print(type(r.content))
    print("Done.")
    print("[4] Decoding the code...")
    dowolnie = r.content
    dowolnie = dowolnie.decode("utf-8")
    print("Done.")
    print("[5] Writing decoded code...")
    f.write(dowolnie)
    sleep(3)
    print("Done.")
    print("Newest version has been downloaded.")
    sleep(2)
