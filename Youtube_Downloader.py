import os
import pytube
from time import sleep, strftime
import webbrowser

version = 1.0
print("checking if program is up to date.")
print("up to date!")
sleep(2)

def main():
    print("""
    ╋╋╋╋╋╋╋╋╋╋┏┓╋╋╋┏┓╋╋╋╋╋╋╋┏┓╋╋╋╋╋╋╋┏┓╋╋╋╋╋╋╋╋┏┓
    ╋╋╋╋╋╋╋╋╋┏┛┗┓╋╋┃┃╋╋╋╋╋╋╋┃┃╋╋╋╋╋╋╋┃┃╋╋╋╋╋╋╋╋┃┃
    ┏┓╋┏┳━━┳┓┣┓┏╋┓┏┫┗━┳━━┓┏━┛┣┓┏┓┏┳━┓┃┃┏━━┳━━┳━┛┣━━┳━┓
    ┃┃╋┃┃┏┓┃┃┃┃┃┃┃┃┃┏┓┃┃━┫┃┏┓┃┗┛┗┛┃┏┓┫┃┃┏┓┃┏┓┃┏┓┃┃━┫┏┛
    ┃┗━┛┃┗┛┃┗┛┃┗┫┗┛┃┗┛┃┃━┫┃┗┛┣┓┏┓┏┫┃┃┃┗┫┗┛┃┏┓┃┗┛┃┃━┫┃D
    ┗━┓┏┻━━┻━━┻━┻━━┻━━┻━━┛┗━━┛┗┛┗┛┗┛┗┻━┻━━┻┛┗┻━━┻━━┻┛
    ┏━┛┃
    ┗━━┛
    """ + "\nVersion: " + str(version))
    date = str(strftime('[%y-%m-%d]'))
    print(f'Todays Date: {date}')
    print("Welcome!\nChoose Opion\n1.Download\n2.Discord Community")
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
        webbrowser.open_new_tab("https://discord.gg/xthqMZjp")
        sleep(2)
        main()
    if anwser == "1":
        clear()
        print("Before you download a video, please input what do you want to download\nFor 1 download ONLY one video\nfor 2 download playlists")
        
        downloadwhat = input(" >> ")
        if int(downloadwhat) == 1:
            print("To start, you need to give the directory where you want to save.\nPlease input the directory.")
            path = input(" >> ")
            if not os.path.exists(path):
                print("ERROR")
                print("Seems like directory you want to save the file doesn't exist. Please input the valid directory")
            else:
                os.chdir(path)
            
                print("Sweet! Now you need to give the youtube link that you want to download.")
                while True:
                    link = str(input(" >> "))
                
                    print("checking the link if it's valid to avoid the errors...")
                    checking = "https://www.youtube.com/watch?v="
                    if link.startswith(checking):
                        print("valid url!")
                        
                        clear()
                        url = pytube.YouTube(str(link))
                        print(f'Downloading the video: {url.title}')
                        video = url.streams.filter(progressive=True).last()
                        video.download()
                        video_check = f'{path}\{url.title}.mp4'
                        if os.path.exists(video_check):
                            clear()
                            print("Success! Going back into the menu...")
                            sleep(2)
                            main()
                        else:
                            clear()
                            print("Semms like video didn't downloaded. To make sure, please check your directory to just make sure.")
                            print("Going into the menu in 10 seconds...")
                            sleep(10)
                            main()
                                
                    else:
                        print("Link is not valid. Enter valid one.")


        if int(downloadwhat) == 2:
            print("To start, you need to give the directory where you want to save.\nPlease input the directory.")
            path = input(" >> ")
            if not os.path.exists(path):
                print("ERROR")
                print("Seems like directory you want to save the file doesn't exist. Please input the valid directory")

            else:
                os.chdir(path)
                print("Sweet! Now you need to give the link to playlist that you want to download.")
                while True:
                    link = str(input(" >> "))
                    print("checking the link if it's valid to avoid the errors...")
                    checking = "https://www.youtube.com/playlist?list="
                    if link.startswith(checking):
                        print("valid url!")
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

main()
