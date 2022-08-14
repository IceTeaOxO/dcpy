from pytube import YouTube
import os
# import moviepy
# from moviepy.editor import *


url = 'https://www.youtube.com/watch?v=i-d-s01gIrs'
def makeMusic(url):
    url = url[6:]
    yt = YouTube(url)
    yt.streams.filter(only_audio=True)
    stream = yt.streams.get_by_itag(251)
    if(os.path.isfile("./music/"+stream.default_filename)):
        print("./music/"+stream.default_filename)
        pass
    else:
        stream.download(output_path="./music")
    #轉換成mp3
    # new_file = './music/'+stream.default_filename + '.mp3'
    # os.rename('./music/'+stream.default_filename, new_file)
    return stream.default_filename
# makeMusic(url)


# video = VideoFileClip('Sora no Kiseki the 3rd Evolution [BGM RIP] - Cry for your Eternity.3gpp')
# video.audio.write_audiofile('test.mp3')