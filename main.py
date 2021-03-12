import pafy
import youtube_dl

url = input("Enter url: ")
video = pafy.new(url)

streams = video.streams
for i in streams:
    print(i)

best = video.getbest()
print("Resolution will be" + best.resolution)

best.download()
print("Done")
