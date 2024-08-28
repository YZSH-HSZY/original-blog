# import PyMuPDF
import fitz
import os


def covert2pic(zoom):
    if os.path.exists('.pdf'):       # 临时文件，需为空
        #  os.removedirs('.pdf')
        #  os.remove('.pdf')
        for root,dirs,files in os.walk('.pdf'):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir('.pdf')
    os.mkdir('.pdf')
    for pg in range(totaling):
        page = doc[pg]
        zoom = int(zoom)            #值越大，分辨率越高，文件越清晰
        rotate = int(0)
        print(page)
        trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).prerotate(rotate)
        pm = page.get_pixmap(matrix=trans, alpha=False)
      
        lurl='.pdf/%s.jpg' % str(pg+1)
        # pm.writePNG(lurl)
        pm._writeIMG(lurl,format=7,jpg_quality=95)
    doc.close()

def pic2pdf(obj):
    doc = fitz.open()
    for pg in range(totaling):
        img = '.pdf/%s.jpg' % str(pg+1)
        imgdoc = fitz.open(img)                 # 打开图片
        pdfbytes = imgdoc.convert_to_pdf()        # 使用图片创建单页的 PDF
        os.remove(img)  
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insert_pdf(imgpdf)                   # 将当前页插入文档
    if os.path.exists(obj):         # 若文件存在先删除
        os.remove(obj)
    doc.save(obj)                   # 保存pdf文件
    doc.close()


def pdfz(sor, obj, zoom):    
    covert2pic(zoom)
    pic2pdf(obj)


def get_test(dirname:str):
    if os.path.exists(dirname):       
        #  os.removedirs('.pdf')
        #  os.remove('.pdf')
        for root,dirs,files in os.walk(dirname,topdown=False): # topdown代表是深搜还是广搜，默认true广搜
            for name in files:
                print(os.path.join(root,name))
            for name in dirs:
                print(os.path.join(root,name))
    
if __name__  == "__main__":

    # sor = "相关证书.pdf"              # 需要压缩的PDF文件
    # obj = "new" + sor
    # doc = fitz.open(sor) 
    # totaling = doc.page_count
    
    # zoom = 200                     # 清晰度调节，缩放比率
    # pdfz(sor, obj, zoom)
    # os.removedirs('.pdf')
    get_test('.')