# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 10:31:47 2022
v0.0.1 - 모듈 배포

@author: 이기성
"""

import cv2
import numpy as np
import os
from PIL import ImageFont, ImageDraw, Image
import numpy as np

    
def kr_imread(path):
    img_array = np.fromfile(path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return img

def kr_imwrite(path, img):
    extension = os.path.splitext(path)[1]
    # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    result, img = cv2.imencode(extension, img)
    if result:
        with open(path, mode='w+b') as f:
            img.tofile(f)
    else:
        raise TypeError
        
def kr_putText(img: np.ndarray, text: str, axes: tuple, font_size: int=50, color: tuple=(255,255,255), outline: bool=True):
    """_summary_

    Args:
        img (np.ndarray): cv2로 불러온 이미지
        text (str): 들어갈 텍스트.
        axes (tuple): 텍스트 넣을 좌표 값 (x, y).
        font_size (int, optional): 글씨 크기. Defaults to 50.
        color (tuple, optional): 색상 (B, G, R). Defaults to (255,255,255).
        outline (bool, optional): 외각선 유무. Defaults to True.

    Returns:
        np.ndarray: cv2 이미지 타입
    """    
    font = ImageFont.truetype('fonts/gulim.ttc', font_size)
    x1, y1 = axes
    img = Image.fromarray(img)
    draw = ImageDraw.Draw(img)
    if outline:
        draw.text((x1, y1), text, font=font, fill=(0,0,0), stroke_width=1, strock_fill='#fff')
    draw.text((x1, y1), text, font=font, fill=color)
    return np.array(img)