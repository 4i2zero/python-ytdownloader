import youtube_dl

print("**** WELCOME TO YOUTUBE VIDEO DOWNLOADER BY DESI-DISTRO.COM *****")
url = input("Pate Youtube Video Url Here : ")
ydl_opts = {}
ydl = youtube_dl.YoutubeDL(ydl_opts)
print('(‿ˠ‿)' * 10)
print("Starting Your Download Now !!!!")
print('(‿ˠ‿)' * 10)
ydl.download([url])




