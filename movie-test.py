from moviepy.editor import *
from moviepy.video.fx import resize
import math
clip1 = VideoFileClip("rabbit.mp4").subclip(0, 2)              # 動画の切り出し
clip2 = (
    ImageClip("image.jpg")
    .set_start(0)
    .set_duration(5)
    .fx(resize.resize, 0.5)
)
clip3 = (
    ImageClip("reimu/223.png")
    .set_start(0)
    .set_duration(5)
    .set_position(lambda t: (50+2*math.cos(3*t), 300+5*math.sin(5*t)))
)
clip4 = (
    ImageClip("立ち絵まりさ/226.png")
    .set_start(0)
    .set_duration(5)
    .set_position(lambda t: (800+2*math.cos(4*t), 300+5*math.sin(5*(t+1))))
)
clip5 = AudioFileClip("test.wav").subclip(1, 50)

new_audioclip = CompositeAudioClip([clip5])
clip6 = (
    TextClip("一体どうなってんだ", fontsize=70, color='white',
             stroke_color='black')
    .set_start(0)
    .set_duration(50)
    .set_position('center')
)
txt_clip = (TextClip("My Holidays 2013", fontsize=70, color='white')
            .set_position('center')
            .set_duration(10))
final_clip = CompositeVideoClip(
    [clip1, clip2, clip3, clip4, txt_clip])  # 動画の結合
final_clip.audio = clip5

final_clip.write_videofile(
    "final_rabbit.mp4")                 # 動画の書き出し
