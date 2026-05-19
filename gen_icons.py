#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('icons', exist_ok=True)

for size in [192, 512]:
    img = Image.new('RGB', (size, size), color='#0d0d0d')
    draw = ImageDraw.Draw(img)
    
    # Draw a rounded rect accent bar at top
    bar_h = size // 12
    draw.rectangle([0, 0, size, bar_h], fill='#33ff99')
    
    # Emoji-style grass icon — draw simple text
    emoji_size = int(size * 0.55)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', emoji_size)
    except:
        font = ImageFont.load_default()
    
    text = '🌿'
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size - tw) // 2
    y = (size - th) // 2 + bar_h // 2
    draw.text((x, y), text, font=font, fill='white')
    
    img.save(f'icons/icon-{size}.png')
    print(f'Generated icon-{size}.png')
