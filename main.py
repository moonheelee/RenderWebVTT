import webvtt
from moviepy.editor import TextClip, concatenate_videoclips, ColorClip, CompositeVideoClip

# Read the VTT file and create a list of text clips
vtt = webvtt.read('simple_hello.vtt')
clips = []
for caption in vtt:
    start = caption.start_in_seconds or 0
    end = caption.end_in_seconds or 0
    duration = end - start

    # Skip captions with None or negative duration
    if duration <= 0:
        continue

    # Create a text clip for the caption
    txt_clip = TextClip(caption.text, fontsize=24, color='white').set_duration(duration)

    # Create a background clip with the same duration as the text clip
    background = ColorClip((1280, 720), col=(0, 0, 0)).set_duration(duration)

    # Overlay the text clip on the background
    clip = CompositeVideoClip([background, txt_clip.set_pos('center', 'bottom')])

    # Add the clip to the list
    clips.append(clip)

# Concatenate the clips and write the output video
final_clip = concatenate_videoclips(clips, method="compose")
final_clip.write_videofile("output.mp4", fps=24)
