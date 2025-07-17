#!/usr/bin/env python3
"""
speedup_mp4_fixed.py – double video speed while keeping audio in‑pitch,
and survive >2‑channel or legacy FFmpeg setups.
"""
import argparse, shutil, subprocess, sys
from pathlib import Path

def run(cmd):
    subprocess.check_call(cmd)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src_mp4")
    ap.add_argument("-o", "--out")
    args = ap.parse_args()

    src = Path(args.src_mp4).expanduser().resolve()
    if not src.is_file():
        sys.exit(f"Input not found: {src}")
    dst = Path(args.out).expanduser().resolve() if args.out \
          else src.with_stem(src.stem + "_2x")

    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg not in PATH")

    chs = subprocess.check_output(
        ["ffprobe", "-v", "error", "-select_streams", "a:0",
         "-show_entries", "stream=channels", "-of", "csv=p=0", str(src)],
         text=True).strip() or "2"
    chs = int(chs)

    audio_filter = "atempo=2" if chs <= 2 else \
                   "pan=stereo|FL=FL|FR=FR,atempo=2"

    cmd = [
        "ffmpeg", "-i", str(src),
        "-filter_complex",
        f"[0:v]setpts=PTS/2[v];[0:a]{audio_filter}[a]",
        "-map", "[v]", "-map", "[a]",
        "-c:v", "libx264", "-preset", "fast",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        str(dst)
    ]

    try:
        print("Encoding …"); run(cmd); print("Done →", dst)
    except subprocess.CalledProcessError as e:
        sys.exit(f"ffmpeg failed ({e.returncode})")

if __name__ == "__main__":
    main()
