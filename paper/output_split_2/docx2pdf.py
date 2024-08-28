"""
 调用window app接口将docx文件转换为pdfwj
"""

from glob import glob
import os
from tqdm import tqdm
import win32com.client
def docx2pdf(docx_full_path: str, output_pdf_dir: str):
    doc = word.Documents.Open(docx_full_path)
    output_pdf_dir_max_num = len(os.listdir(output_pdf_dir))
    doc.SaveAs(
        os.path.join(
            output_pdf_dir, 
            str(output_pdf_dir_max_num) + '.pdf'), 
        FileFormat=17)
    doc.Close(0)

if __name__ == "__main__":
    word = win32com.client.Dispatch("Word.Application")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    all_docx_files = glob(
        os.path.join(current_dir, '*.docx')
    )
    assert len(all_docx_files) > 0
    for _ in tqdm(all_docx_files, desc='docx转换中'):
        output_dir = os.path.join(
            current_dir,
            'translate'
        )
        os.makedirs(output_dir, exist_ok=True)
        docx2pdf(_, output_dir)
