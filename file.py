from pytube import YouTube
link=input("Enter link of youtube video:")
yt=YouTube(link)
videos=yt.streams.all()
i=1
for stream in videos:
    print(str(i) +" "+ str(stream))
    i+=1
stream_number=int(input("Enter number: "))
video=videos[stream_number-1]
video.download("./Download")
print("Downloaded")


