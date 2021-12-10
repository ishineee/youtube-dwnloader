import os
import pytube
from time import sleep, strftime
import webbrowser
import requests
import threading
import itertools
import sys


def main():
    clear()
    print("""
    YOUTUBE DWNLOADER
    """ + f"\nVersion: {str(version)} " )
    date = str(strftime('[%y-%m-%d]'))
    print(f'Todays Date: {date}')
    print("Welcome!\nChoose Option\n1.Download\n2.Discord Community\n3.Info")
    anwsers()


def clear():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)


def anwsers():
    anwser = input(" >> ")

    if anwser == "2":
        print("discord link is opening...")
        webbrowser.open_new_tab("https://discord.gg/rD4xYt4ZrT")
        sleep(2)
        clear()
        main()
    if anwser == "1":
        clear()
        print("Before you download a video, please input what do you want to download\nFor 1 download ONLY one video\nfor 2 download playlist")        
        downloadwhat = input(" >> ")

        if int(downloadwhat) == 1:
            clear()
            print("To start, you need to give the directory where you want to save.\nPlease input the directory.")
            path = input(" >> ")
            if not os.path.exists(path):
                clear()
                print("ERROR")
                print("Seems like directory you want to save the file doesn't exist. Please input the valid directory")
            else:
                os.chdir(path)
                clear()
                print("Sweet! Now you need to give the youtube link that you want to download.")
                while True:
                    link = str(input(" >> "))
                    clear()
                    print("checking the link if it's valid to avoid the errors...")
                    checking = "https://www.youtube.com/watch?v="
                    if link.startswith(checking):
                        print("valid url!")

                        clear()
                        url = pytube.YouTube(str(link))
                        done = False
                        def animate():
                            for c in itertools.cycle(['|', '/', '-', '\\']):
                                if done:
                                    break
                                sys.stdout.write(f'\rDownloading the video: {url.title} {c}')
                                sys.stdout.flush()
                                sleep(0.1)
                            sys.stdout.write('\rDone!')
                        t = threading.Thread(target=animate)
                        t.start()
                        video = url.streams.filter(progressive=True).last()
                        video.download()
                        video_check = f'{path}\{url.title}.mp4'
                        if os.path.exists(video_check):
                            clear()
                            done = True
                            print("Success! Going back into the menu...")
                            sleep(2)
                            main()
                        else:
                            clear()
                            done = True
                            print("System didn't saw the file that this program made")
                            print("MAKE SURE TO LOOK AT YOUR FOLDER AND SEE IF YOUR VIDEO IS DOWNLOADED")
                            print("Going into the menu in 10 seconds...")
                            sleep(10)
                            main()           
                    else:
                        print("Link is not valid. Enter valid one.")


        if int(downloadwhat) == 2:
            clear()
            print("To start, you need to give the directory where you want to save.\nPlease input the directory.")
            path = input(" >> ")
            if not os.path.exists(path):
                clear()
                print("ERROR")
                print("Seems like directory you want to save the file doesn't exist. Please input the valid directory")
            else:
                os.chdir(path)
                clear()
                print("Sweet! Now you need to give the link to playlist that you want to download.")
                while True:                
                    link = str(input(" >> "))
                    clear()
                    print("checking the link if it's valid to avoid the errors...")
                    checking = "https://www.youtube.com/playlist?list="
                    if link.startswith(checking):
                        print("valid url!")
                        clear()
                        p = pytube.Playlist(link)
                        print(f'Downloading: {p.title}')
                        for video in p.videos:
                            geniusz = video.streams.filter(progressive=True).last()
                            geniusz.download()
                        print("Done! since i'm bad coder you should check your folder to see if your videos are downloaded.\nyour videos prob get downloaded")
                        print("Going to menu in 5 seconds...")
                        sleep(5)
                        main()
                    else:
                        print("not valid link!")
            

        if int(anwser) == 3:
            print("Main dev: ishineee")
            print("Download system has been made by PyTube developers not me!")
            print("\nTo Do List:")
            print("- My own download system")
            print("- Download system for other sites")
            print("free minecraft premium allah 100 percent legit")
            print("\n input 1 if u want to go back")
            goto = input(" >> ")
            if str(goto) == "1":
                main()
        if anwser != "1" or "2" or "3":
            print("Not valid anwser")
            anwsers()


version = f'1.1\n'
print("Checking the version")
url = "https://raw.githubusercontent.com/ishineee/youtube-dwnloader/main/current_version.txt"
r = requests.get(url)
content_dec = r.content
content_dec = content_dec.decode("utf-8")
current_version = content_dec
if str(version) == str(current_version):
    clear()
    print("Version is up to date!")
    main()
else:
    clear()
    print("Your version is Outdated!")
    print("This file will be updated in 5 seconds.")
    sleep(5)
    update_filename_check = "update.py"
    if os.path.exists(update_filename_check):
        clear()
        import update
        update.downloadlatestversion()
    else:
        clear()
        print("you didn't download update.py!")
        print("downloading it for you..")
        url2 = "https://raw.githubusercontent.com/ishineee/youtube-dwnloader/main/update.py"
        r2 = requests.get(url2)
        content_dec = r2.content
        content_dec = content_dec.decode("utf-8")
        f = open("update.py", "a")
        f.write(content_dec)
        print("Done.")
        sleep(2)
        clear()
        while True:
            print("restart the script!")        
