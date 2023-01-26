# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 10:31:47 2022
v0.0.1 - 모듈 배포
v0.0.2 - putText list 추가 및 get font_size 추가
v0.0.3 - putText에 autofont 옵션 추가
v0.0.4 - putText에 docstrig 추가
v0.0.5 - expand_img 추가
v0.0.6 - expand_img 수정
@author: 이기성
"""

import cv2
import numpy as np
import os
from PIL import ImageFont, ImageDraw, Image
import numpy as np

__version__ = 'v0.0.6'
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
    img = Image.fromarray(img)
    draw = ImageDraw.Draw(img)
    
    x1, y1 = axes
    if outline:
        draw.text((x1, y1), text, font=font, fill=(0,0,0), stroke_width=1, strock_fill='#fff')
    draw.text((x1, y1), text, font=font, fill=color)
    return np.array(img)

def kr_putText_list(img: np.ndarray, text_axes: list, font_size: int=50, color: tuple=(255,255,255), outline: bool=True, auto_font: bool=False):
    """_summary_

    Args:
        img (np.ndarray): cv2로 불러온 이미지
        text_axes (list): (text, x, y) 로 이루어진 튜플의 리스트.
        font_size (int, optional): 글씨 크기. Defaults to 50.
        color (tuple, optional): 색상 (B, G, R). Defaults to (255,255,255).
        outline (bool, optional): 외각선 유무. Defaults to True.
        auto_font (bool, optional): 자동 폰트 사이즈. Defaults to False.

    Returns:
        np.ndarray: cv2 이미지 타입
    """    
    if auto_font:
        font = ImageFont.truetype('fonts/gulim.ttc', get_fontsize(img, font_size))
    else:
        font = ImageFont.truetype('fonts/gulim.ttc', font_size)

    img = Image.fromarray(img)
    draw = ImageDraw.Draw(img)
    for text, x, y in text_axes:
        if outline:
            draw.text((x, y), text, font=font, fill=(0,0,0), stroke_width=1, strock_fill='#fff')
        draw.text((x, y), text, font=font, fill=color)
    return np.array(img)

def get_fontsize(img: np.array, size: int):
    """_summary_

    Args:
        img (np.array): 이미지
        size (int): 1~3
    """
    font_size = (img.shape[0] * img.shape[1]) // (40000 * size)
    return font_size

def expand_img(img: np.array, width: int=0, height: int=0):
    """_summary_

    Args:
        img (np.array): 넘파이 이미지
        width (int): img.shape[1] 에서 더할 값
        height (int): img.shape[0] 에서 더할 값
    """    
    new_img = np.zeros((img.shape[0]+height, img.shape[1]+width, img.shape[2])) + 255
    new_img[:img.shape[0],:img.shape[1],:] = img
    new_img = np.array(new_img, dtype='uint8')
    return new_img