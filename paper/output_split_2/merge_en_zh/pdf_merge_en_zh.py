from glob import glob
import os
from os.path import dirname, splitext, basename, join
import pypdf
from tqdm import tqdm

if __name__ =="__main__":
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # 原文分割pdf
    # all_src_pdfs = glob(join(dirname(current_dir), '*.pdf'))
    # all_src_pdfs.sort(key=lambda x: int(splitext(basename(x))[0]))
    src_pdf = 'A Recurrent Convolutional Neural Network (RCNN) based Visual Odometry Approach for Endoscopic Capsule Robots.pdf'
    translate_pdf = 'merge2.pdf'
    
    output_pdf = pypdf.PdfWriter()
    # for _ in tqdm(all_pdf, desc='合并pdf'):
    input_pdf_1 = pypdf.PdfReader(
        stream=open(join(current_dir, src_pdf), 'rb'))
    input_pdf_2 = pypdf.PdfReader(
        stream=open(join(current_dir, translate_pdf), 'rb'))
    
    for i in range(len(input_pdf_1.pages)):
        output_pdf.insert_page(
            input_pdf_1.pages[i], 
            index=len(output_pdf.pages)
        )
    for i in range(len(input_pdf_2.pages)):
        output_pdf.insert_page(
            input_pdf_2.pages[i], 
            index=len(output_pdf.pages)
        )
    output_pdf.write(open('merge_en_zh.pdf', 'wb'))
    output_pdf.close()