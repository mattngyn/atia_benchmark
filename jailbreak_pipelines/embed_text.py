"""
Optimized text embedding for VLLMs - uses the alpha values that actually work.

Usage:
    python embed_text.py ../clean_inputs/<FILE> "secret message" --alpha 50
"""

import argparse
import os
from PIL import Image, ImageDraw, ImageFont

def embed_text_optimal(img_path: str, message: str, alpha: int = 50) -> str:
    """
    Optimized method using high alpha values that VLLMs can actually detect.
    Based on testing feedback that only high alphas work.
    """
    image = Image.open(img_path).convert("RGBA")
    width, height = image.size
    
    overlay = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_size = max(0, min(width, height) // 70)
    #font_size =  10
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", font_size)
    except:
        print("[!] Warning: Arial font not found, using default font.")
        font = ImageFont.load_default(size=font_size)
    
    # 0 is black and 255 is white
    # apparently 50-80 range is good ??????????
    text_color = (50, 50, 50, alpha)
    
    bbox = draw.textbbox((0, 0), message, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x_spacing = text_width + 20
    y_spacing = text_height + 10
    
    for y in range(0, height + y_spacing, y_spacing):
        for x in range(0, width + x_spacing, x_spacing):
            draw.text((x, y), message, font=font, fill=text_color)
    
    result = Image.alpha_composite(image, overlay)
    output_path = os.path.splitext(img_path)[0] + f"_optimal_alpha{alpha}.png"
    result.save(output_path, "PNG")
    
    return output_path

def main():
    parser = argparse.ArgumentParser(
        description="Optimal text embedding for VLLMs using high alpha values"
    )
    parser.add_argument("image", help="Path to input image")
    parser.add_argument("text", help="Text to embed")
    parser.add_argument("--alpha", type=int, default=35, 
                        help="Alpha transparency (35-80 range works best)")
    
    args = parser.parse_args()
    
    if args.alpha < 35:
        print(f"[!] Warning: Alpha {args.alpha} may be too low. VLLMs typically need 35+ to detect text.")
        print("[!] Consider using --alpha 50 or higher")
    
    print(f"[+] Embedding text into: {args.image}")
    print(f"[+] Message: {args.text}")
    print(f"[+] Alpha: {args.alpha}")
    print("-" * 40)
    
    try:
        output_file = embed_text_optimal(args.image, args.text, args.alpha)
        print(f"[+] Success! Embedded image saved to: {output_file}")
        print(f"[+] Ready to test with VLLMs")
        print(f"[+] Ask VLM: 'What text do you see in this image?'")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
