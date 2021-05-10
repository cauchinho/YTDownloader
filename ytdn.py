from pytube import YouTube
link = input("mete el link kpo: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
