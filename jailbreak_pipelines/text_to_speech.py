"""
OpenAI Text-to-Speech Script
Converts text string to high-quality MP3 audio using OpenAI's TTS API.

Usage:
    python text_to_speech.py "Hello world"
    python text_to_speech.py "Hello world" --output my_audio.mp3
    python text_to_speech.py "Hello world" --voice alloy --model tts-1-hd
"""

import argparse
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def text_to_speech(text: str, output_file: str = None, voice: str = "alloy", model: str = "tts-1"):
    """
    Convert text to speech using OpenAI's TTS API and save as MP3.
    
    Args:
        text: Text to convert to speech
        output_file: Output MP3 file path (default: generated from text)
        voice: Voice to use - alloy, echo, fable, onyx, nova, shimmer
        model: Model to use - tts-1 (faster) or tts-1-hd (higher quality)
    """
    try:
        client = OpenAI() 
        
        if not output_file:

            safe_text = "".join(c for c in text[:30] if c.isalnum() or c in (' ', '-', '_')).rstrip()
            safe_text = safe_text.replace(' ', '_')
            output_file = f"speech_{safe_text}.mp3"
        
        if not output_file.endswith('.mp3'):
            if '.' not in os.path.basename(output_file):
                output_file += '.mp3'
            else:
                output_file = os.path.splitext(output_file)[0] + '.mp3'
        
        print(f"[+] Converting text to speech with OpenAI...")
        print(f"[+] Text: '{text}'")
        print(f"[+] Output: {output_file}")
        print(f"[+] Voice: {voice}")
        print(f"[+] Model: {model}")
        print(f"[+] Format: MP3")
        
        response = client.audio.speech.create(
            model=model,
            voice=voice,
            input=text
        )
        
        response.stream_to_file(output_file)
        
        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file)
            print(f"[+] Success! Audio saved to: {output_file}")
            print(f"[+] File size: {file_size} bytes")
            print(f"[+] High-quality MP3 audio ready to play!")
            return output_file
        else:
            print(f"[!] Error: Audio file was not created")
            return None
            
    except Exception as e:
        print(f"[!] Error: {e}")
        print(f"[!] Make sure you have:")
        print(f"    1. OpenAI API key set: export OPENAI_API_KEY='your-key'")
        print(f"    2. OpenAI library installed: pip install openai")
        return None

def list_voices():
    """List available OpenAI TTS voices"""
    voices = {
        "alloy": "Neutral, balanced voice",
        "echo": "Male voice with clear articulation", 
        "fable": "British accent, storytelling voice",
        "onyx": "Deep male voice",
        "nova": "Young female voice",
        "shimmer": "Soft female voice"
    }
    
    print("[+] Available OpenAI TTS voices:")
    for voice_name, description in voices.items():
        print(f"    {voice_name}: {description}")

def main():
    parser = argparse.ArgumentParser(
        description="Convert text to high-quality MP3 speech using OpenAI TTS",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python text_to_speech.py "Hello world"
    python text_to_speech.py "Hello world" --output greeting.mp3
    python text_to_speech.py "Hello world" --voice nova --model tts-1-hd
    python text_to_speech.py --list-voices
    
Setup:
    export OPENAI_API_KEY='your-openai-api-key'
    pip install openai
        """
    )
    
    parser.add_argument("text", nargs='?', help="Text to convert to speech")
    parser.add_argument("--output", "-o", help="Output MP3 file path (default: auto-generated)")
    parser.add_argument("--voice", choices=["alloy", "echo", "fable", "onyx", "nova", "shimmer"], 
                        default="alloy", help="Voice to use (default: alloy)")
    parser.add_argument("--model", choices=["tts-1", "tts-1-hd"], default="tts-1",
                        help="Model: tts-1 (faster) or tts-1-hd (higher quality, default: tts-1)")
    parser.add_argument("--list-voices", action="store_true",
                        help="List available voices and exit")
    
    args = parser.parse_args()
    
    if args.list_voices:
        list_voices()
        return
    
    if not args.text:
        print("[!] Error: Please provide text to convert to speech")
        print("Usage: python text_to_speech.py \"Your text here\"")
        sys.exit(1)
    
    if not os.getenv('OPENAI_API_KEY'):
        print("[!] Error: OPENAI_API_KEY environment variable not set")
        print("[!] Set it with: export OPENAI_API_KEY='your-api-key'")
        print("[!] Get your API key from: https://platform.openai.com/api-keys")
        sys.exit(1)
    
    result = text_to_speech(
        text=args.text,
        output_file=args.output,
        voice=args.voice,
        model=args.model
    )
    
    if result:
        print(f"[+] Complete! You can play the MP3 file: {result}")
    else:
        print("[!] Failed to create audio file")
        sys.exit(1)

if __name__ == "__main__":
    main()
