"""
OpenAI Text-to-Speech Script (single or batch)
Converts text to high-quality MP3 audio using OpenAI's TTS API.

Usage (single):
    python text_to_speech.py "Hello world"
    python text_to_speech.py "Hello world" --output my_audio.mp3
    python text_to_speech.py "Hello world" --voice alloy --model tts-1-hd

Usage (batch):
    # TXT: one prompt per line
    python text_to_speech.py --input-file prompts.txt --output-dir out/

    # JSONL: each line can be a string, or an object with fields like:
    #   {"id":"S1","name":"PODCAST_2fa_trigger_walkthrough.mp3","text":"...","voice":"nova","model":"tts-1"}
    python text_to_speech.py --input-file prompts.jsonl --output-dir out/

    # JSON: list of strings or objects (same fields as JSONL)
    python text_to_speech.py --input-file prompts.json --output-dir out/ --voice nova --model tts-1

Notes:
- If an item has a 'name' (or 'filename'), that exact name is used for the MP3 (sanitized/forced to .mp3).
- If an item has an 'audio' path, the basename is used as name (e.g., '.../PODCAST_x.mp3' -> 'PODCAST_x.mp3').
- If no 'name' is provided, the script uses --output-template with placeholders:
  {id}, {index}, {index:02d}, {slug}, {voice}, {model}
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Iterable, List, Dict, Any, Tuple, Optional

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def sanitize_slug(text: str, max_len: int = 40) -> str:
    base = "".join(c for c in text[:max_len] if c.isalnum() or c in (" ", "-", "_")).strip()
    return base.replace(" ", "_") or "speech"


def ensure_mp3(path: str) -> str:
    if not path.endswith(".mp3"):
        if "." not in os.path.basename(path):
            return path + ".mp3"
        return os.path.splitext(path)[0] + ".mp3"
    return path


def safe_basename(name: str) -> str:
    # Keep directory basename only; strip unsafe chars except [-_. ]
    base = os.path.basename(name)
    allowed = []
    for c in base:
        if c.isalnum() or c in ("-", "_", ".", " "):
            allowed.append(c)
    base = "".join(allowed).strip().replace(" ", "_")
    return base or "speech"


def text_to_speech(text: str, output_file: str = None, voice: str = "alloy", model: str = "tts-1") -> Optional[str]:
    """Convert text to speech using OpenAI's TTS API and save as MP3."""
    try:
        client = OpenAI()

        if not output_file:
            safe_text = sanitize_slug(text, max_len=30)
            output_file = f"speech_{safe_text}.mp3"

        output_file = ensure_mp3(output_file)
        Path(os.path.dirname(output_file) or ".").mkdir(parents=True, exist_ok=True)

        print(f"[+] Converting text to speech with OpenAI...")
        print(f"[+] Text: '{text[:120]}{'...' if len(text) > 120 else ''}'")
        print(f"[+] Output: {output_file}")
        print(f"[+] Voice: {voice}")
        print(f"[+] Model: {model}")
        print(f"[+] Format: MP3")

        response = client.audio.speech.create(model=model, voice=voice, input=text)
        response.stream_to_file(output_file)

        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file)
            print(f"[+] Success! Audio saved to: {output_file} ({file_size} bytes)")
            return output_file
        else:
            print(f"[!] Error: Audio file was not created")
            return None
    except Exception as e:
        print(f"[!] Error: {e}")
        print(f"[!] Make sure you have:")
        print(f"    1. OPENAI_API_KEY set: export OPENAI_API_KEY='your-key'")
        print(f"    2. openai library installed: pip install openai python-dotenv")
        return None


def list_voices():
    voices = {
        "alloy": "Neutral, balanced voice",
        "echo": "Male voice with clear articulation",
        "fable": "British accent, storytelling voice",
        "onyx": "Deep male voice",
        "nova": "Young female voice",
        "shimmer": "Soft female voice",
    }
    print("[+] Available OpenAI TTS voices:")
    for voice_name, description in voices.items():
        print(f"    {voice_name}: {description}")


def _extract_text_from_json_obj(obj: Dict[str, Any]) -> Optional[str]:
    if isinstance(obj.get("text"), str):
        return obj["text"]
    if isinstance(obj.get("input"), list):
        for msg in obj["input"]:
            if not isinstance(msg, dict):
                continue
            content = msg.get("content")
            if isinstance(content, list):
                for part in content:
                    if isinstance(part, dict) and part.get("type") == "text" and isinstance(part.get("text"), str):
                        return part["text"]
    return None


def parse_input_file(path: str) -> List[Dict[str, Any]]:
    """Parse .txt / .jsonl / .json into structured items with optional per-item names."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    items: List[Dict[str, Any]] = []
    ext = p.suffix.lower()

    if ext == ".txt":
        # Support optional "NAME || TEXT" on each line.
        for idx, line in enumerate(p.read_text(encoding="utf-8").splitlines(), start=1):
            raw = line.strip()
            if not raw:
                continue
            name = None
            text = raw
            if "||" in raw:
                possible_name, maybe_text = raw.split("||", 1)
                if possible_name.strip():
                    name = possible_name.strip()
                    text = maybe_text.strip() or text
            items.append({"id": None, "name": name, "text": text, "voice": None, "model": None, "index": idx})
        return items

    def _coerce_name(obj: Dict[str, Any]) -> Optional[str]:
        n = obj.get("name") or obj.get("filename")
        if not n and isinstance(obj.get("audio"), str):
            n = os.path.basename(obj["audio"])  # e.g., adversarial_inputs/.../PODCAST_name.mp3
        return n

    if ext == ".jsonl":
        with p.open("r", encoding="utf-8") as f:
            for idx, raw in enumerate(f, start=1):
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    data = json.loads(raw)
                except json.JSONDecodeError:
                    items.append({"id": None, "name": None, "text": raw, "voice": None, "model": None, "index": idx})
                    continue
                if isinstance(data, str):
                    items.append({"id": None, "name": None, "text": data, "voice": None, "model": None, "index": idx})
                    continue
                if isinstance(data, dict):
                    text = _extract_text_from_json_obj(data) or data.get("script") or data.get("tts_text") or data.get("text")
                    if text is None:
                        continue
                    items.append({
                        "id": data.get("id"),
                        "name": _coerce_name(data),
                        "text": text,
                        "voice": data.get("voice"),
                        "model": data.get("model"),
                        "index": idx,
                    })
        return items

    if ext == ".json":
        data = json.loads(p.read_text(encoding="utf-8"))
        seq = data if isinstance(data, list) else (data.get("items") or data.get("samples") or [])
        for idx, item in enumerate(seq, start=1):
            if isinstance(item, str):
                items.append({"id": None, "name": None, "text": item, "voice": None, "model": None, "index": idx})
            elif isinstance(item, dict):
                text = _extract_text_from_json_obj(item) or item.get("script") or item.get("tts_text") or item.get("text")
                if text is None:
                    continue
                items.append({
                    "id": item.get("id"),
                    "name": _coerce_name(item),
                    "text": text,
                    "voice": item.get("voice"),
                    "model": item.get("model"),
                    "index": idx,
                })
        return items

    raise ValueError(f"Unsupported input extension: {ext} (use .txt, .jsonl, or .json)")


def render_output_name(template: str, base_dir: str, item: Dict[str, Any], default_voice: str, default_model: str) -> str:
    # If a per-item name is provided, use it directly.
    if item.get("name"):
        base = safe_basename(item["name"])
        name = ensure_mp3(base)
        return str(Path(base_dir) / name)

    # Otherwise, format with the template
    idx = item.get("index") or 1
    slug = sanitize_slug(item.get("text", ""))
    fid = item.get("id") or f"item_{idx:02d}"
    voice = item.get("voice") or default_voice
    model = item.get("model") or default_model

    try:
        name = template.format(id=fid, index=idx, slug=slug, voice=voice, model=model)
    except Exception:
        name = f"{fid}_{idx:02d}_{slug}.mp3"

    name = ensure_mp3(name)
    return str(Path(base_dir) / name)


def main():
    parser = argparse.ArgumentParser(
        description="Convert text (single or batch) to high-quality MP3 speech using OpenAI TTS",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("text", nargs="?", help="(Single mode) Text to convert to speech")
    parser.add_argument("--input-file", "-i", help="Batch mode: path to .txt / .jsonl / .json of prompts")
    parser.add_argument("--output", "-o", help="(Single mode) Output MP3 file path (default: auto-generated)")
    parser.add_argument("--output-dir", "-d", default="tts_out", help="(Batch mode) Directory to save MP3 files")
    parser.add_argument(
        "--output-template",
        default="{id}_{index:02d}_{slug}.mp3",
        help="(Batch mode) Filename template if no per-item 'name' is provided; placeholders: {id}, {index}, {slug}, {voice}, {model}",
    )
    parser.add_argument("--voice", choices=["alloy", "echo", "fable", "onyx", "nova", "shimmer"], default="alloy", help="Voice to use (default: alloy)")
    parser.add_argument("--model", choices=["tts-1", "tts-1-hd"], default="tts-1", help="Model: tts-1 (faster) or tts-1-hd (higher quality)")
    parser.add_argument("--list-voices", action="store_true", help="List available voices and exit")
    parser.add_argument("--dry-run", action="store_true", help="Parse inputs and print planned outputs without calling API")

    args = parser.parse_args()

    if args.list_voices:
        list_voices()
        return

    if not os.getenv("OPENAI_API_KEY"):
        print("[!] Error: OPENAI_API_KEY environment variable not set")
        print("[!] Set it with: export OPENAI_API_KEY='your-api-key'")
        print("[!] Get your API key from: https://platform.openai.com/api-keys")
        sys.exit(1)

    # Single-text mode
    if args.text and not args.input_file:
        out = text_to_speech(text=args.text, output_file=args.output, voice=args.voice, model=args.model)
        if out:
            print(f"[+] Complete! You can play the MP3 file: {out}")
            return
        else:
            print("[!] Failed to create audio file")
            sys.exit(1)

    # Batch mode
    if not args.input_file:
        print("[!] Error: Provide either a single TEXT or --input-file for batch mode")
        sys.exit(1)

    try:
        items = parse_input_file(args.input_file)
    except Exception as e:
        print(f"[!] Failed to parse input file: {e}")
        sys.exit(1)

    if not items:
        print("[!] No items found in input file")
        sys.exit(1)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"[+] Processing {len(items)} item(s) from {args.input_file} into {out_dir}")

    successes = 0
    outputs: List[str] = []
    for item in items:
        text = item["text"]
        voice = item.get("voice") or args.voice
        model = item.get("model") or args.model
        out_path = render_output_name(args.output_template, str(out_dir), item, args.voice, args.model)

        print(f"---\n[+] Item #{item.get('index')}: id={item.get('id')}, name={item.get('name')}, voice={voice}, model={model}")
        print(f"[+] Output -> {out_path}")
        if args.dry_run:
            outputs.append(out_path)
            continue

        out = text_to_speech(text=text, output_file=out_path, voice=voice, model=model)
        if out:
            successes += 1
            outputs.append(out)

    print(f"[+] Done. {successes}/{len(items)} succeeded.")
    if outputs:
        print("[+] Output files:")
        for p in outputs:
            print("   ", p)


if __name__ == "__main__":
    main()
