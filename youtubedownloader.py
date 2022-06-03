from pytube import YouTube

link= input ('Enter the link of the youtube video:')
yt=YouTube(link)
ystream=yt.streams.get_highest_resolution()

ystream.download()

print('Download successful')