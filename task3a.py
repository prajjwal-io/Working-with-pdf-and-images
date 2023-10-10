import fitz  
import os
import cv2
import numpy as np

class PDFAnonymizer:
    def __init__(self, pdf_folder_path, output_folder_path, blur_regions):
        self.pdf_folder_path = pdf_folder_path
        self.output_folder_path = output_folder_path
        self.blur_regions = blur_regions

    # Function to convert PDF pages to JPEG images
    def pdf_to_jpg(self, pdf_path):
        pdf_document = fitz.open(pdf_path)
        page = pdf_document.load_page(0)  # Load only the first page
        image = page.get_pixmap()
        
        # Get the name of the PDF file without the extension
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        
        # Create the output folder if it doesn't exist
        os.makedirs(self.output_folder_path, exist_ok=True)
        
        # Save the image with the same name as the PDF file but with a .jpg extension
        image_path = os.path.join(self.output_folder_path, f"{pdf_name}.jpg")
        image.save(image_path)
        
        pdf_document.close()

    # Function to blur a region of an image
    def blur_region(self, image, region):
        x, y, w, h = region
        #roi = image[y:y+h, x:x+w]
        #fill with black color to region
        image[y:y+h, x:x+w] = (0, 0, 0)
        # blurred_roi = cv2.GaussianBlur(roi, (21, 21), 0)
        # image[y:y+h, x:x+w] = blurred_roi
        return image

    # Function to anonymize PDFs
    def anonymize_pdfs(self):
        # Iterate through the PDFs and convert each page to an image
        for pdf_file in os.listdir(self.pdf_folder_path):
            if pdf_file.endswith(".pdf"):
                pdf_path = os.path.join(self.pdf_folder_path, pdf_file)
                self.pdf_to_jpg(pdf_path)

        # Iterate through the images and apply blur to the specified regions
        for image_file in os.listdir(self.output_folder_path):
            if image_file.endswith(".jpg"):
                image_path = os.path.join(self.output_folder_path, image_file)
                image = cv2.imread(image_path)
                
                for region in self.blur_regions:
                    image = self.blur_region(image, region)
                
                # Save the processed image
                cv2.imwrite(image_path, image)

        return "PDFs converted to images with anonymized certain parts."

if __name__ == '__main__':
    # Specify the PDF folder path and output folder for images
    pdf_folder_path = 'PDFs'
    output_folder_path = 'Images'

    # Define the region to blur (x, y, width, height) for each image
    blur_regions = [
        (115, 141, 160, 22),
        (80, 170, 160, 22),
        (510, 111, 80, 20),
        (184, 37, 206, 50),
        (455, 18, 100, 70)  # Example region to blur on the first page
    ]

    # Create PDFAnonymizer object and call anonymize_pdfs method
    pdf_anonymizer = PDFAnonymizer(pdf_folder_path, output_folder_path, blur_regions)
    result = pdf_anonymizer.anonymize_pdfs()
    print(result)
