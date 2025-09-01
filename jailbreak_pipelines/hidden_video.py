"""
python hidden_video.py -i ../clean_inputs/2f.png -o  test.mp4 "Audio"
Show an optional image for 1 s, then flash each word and say it.
"""

import argparse, sys, os, tempfile
from moviepy import (
    TextClip, ColorClip, ImageClip, CompositeVideoClip,
    concatenate_videoclips, AudioFileClip, VideoFileClip, vfx
)
from gtts import gTTS

VIDEO_W, VIDEO_H = 800, 600
#FONT_PATH        = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_SIZE        = 60
BG_COLOR         = (255, 255, 255)
FONT_COLOR       = "black"
TARGET_SECS      = 0.25                 

def make_tts(word: str) -> AudioFileClip:
    """Return an AudioFileClip that pronounces *word* (temporary mp3)."""
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    gTTS(text=word, lang="en").write_to_fp(tmp)
    tmp.close()
    return AudioFileClip(tmp.name)

def create_word_video(text: str,
                      out: str,
                      image_path: str | None = None) -> None:
    clips      = []
    tmp_mp3s   = []  
    if image_path:
        lead = (ImageClip(image_path)
                .with_duration(1)                       
                .with_position(("center", "center"))
                .resized(height=VIDEO_H))                 
        clips.append(lead)     

    for word in text.split():
        speech = make_tts(word)
        tmp_mp3s.append(speech.filename)              
        dur = max(TARGET_SECS, speech.duration)

        bg  = ColorClip((VIDEO_W, VIDEO_H), color=BG_COLOR, duration=dur)
        txt = (TextClip(text = word,
                        #font="DejaVuSans",
                        font_size=FONT_SIZE,
                        color=FONT_COLOR,
                        margin=(0,40))
               .with_duration(dur)
               .with_position(("center", "center")))

        vw = (CompositeVideoClip([bg, txt], size=(VIDEO_W, VIDEO_H))
              .with_duration(dur)
              .with_audio(speech))   

        clips.append(vw)

    final_video = concatenate_videoclips(clips, method="compose")
    final_video.write_videofile(out, fps=24, codec="libx264")

    for fname in tmp_mp3s:
        try:
            os.remove(fname)
        except OSError:
            pass

def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate a speaking word-video.")
    p.add_argument("text", nargs="+",
                   help="The text to turn into a video (quote it if needed).")
    p.add_argument("-o", "--output", default="word_video.mp4",
                   help="Output filename (default: %(default)s)")
    p.add_argument("-i", "--image", metavar="PATH",
                   help="Optional image shown for 1 s before the words start.")
    return p.parse_args(argv)

def main() -> None:
    args = parse_args(sys.argv[1:])
    text_string = " ".join(args.text).strip()
    if not text_string:
        sys.exit("Error: no text supplied.")
    create_word_video(text_string, args.output, args.image)

if __name__ == "__main__":
    main()
