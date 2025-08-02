from pdf2image import convert_from_path

pdf_path = 'ExampleCV.pdf'

images = convert_from_path(pdf_path, dpi=200)

for i, image in enumerate(images):
    image.save(f'page_{i+1}.jpg', 'JPEG')
