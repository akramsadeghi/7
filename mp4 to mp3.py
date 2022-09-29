from moviepy.editor import *
video_file = "video.mp4"
audio_file = "seda.mp3"
video = VideoFileClip(video_file)
seda = video.audio
print("please wait!")
seda.write_audiofile(audio_file)

video.close()
seda.close()
print("Done!")
