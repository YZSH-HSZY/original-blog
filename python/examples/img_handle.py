import cv2
import numpy as np
from glob import glob
from os import makedirs
from os.path import join, basename
from tqdm import tqdm

all_img = glob(join('.', '**', '*.jpg'), recursive=True)

def img_changing_quality(src_img_path: str, dst_path: str, quality: int):
    """ 图片质量压缩函数 """
    img = cv2.imdecode(np.fromfile(src_img_path), cv2.IMREAD_COLOR)
    makedirs(dst_path, exist_ok=True)
    cv2.imwrite(
        join(dst_path, basename(src_img_path)),
        img,
        [cv2.IMWRITE_JPEG_QUALITY,quality]
    )
if __name__ == "__main__":

    for a_img in tqdm(all_img, desc="handling..."):
        img_changing_quality(a_img, join('.', 'output'), 50)