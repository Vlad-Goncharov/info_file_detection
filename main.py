import cv2
import pytesseract
from wand.image import Image
from PyPDF2 import PdfFileReader

def ocr(image_path):
    # Чтение изображения
    image = cv2.imread(image_path)

    # Преобразование изображения в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Применение алгоритма бинаризации для улучшения распознавания текста
    threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Применение OCR для распознавания текста из изображения
    recognized_text = pytesseract.image_to_string(threshold_image, lang='eng')

    return recognized_text


def convert_pdf_to_jpg(pdf_path, output_path):
    # Чтение PDF файла
    pdf = PdfFileReader(open(pdf_path, 'rb'))

    # Проход по каждой странице PDF и сохранение ее как изображения в формате JPG
    for page_number in range(pdf.numPages):
        with Image(filename=f'{pdf_path}[{page_number}]') as image:
            # Преобразование изображения в формат JPG
            image.format = 'jpg'
            # Сохранение изображения на диск
            image.save(filename=f'{output_path}/{page_number}.jpg')



pdf_path = 'path/to/pdf.pdf'
output_directory = 'path/to/output/directory'
convert_pdf_to_jpg(pdf_path, output_directory)


image_path = 'path/to/image.jpg'
text = ocr(image_path)
print(text)