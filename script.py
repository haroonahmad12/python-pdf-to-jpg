import argparse
import logging
import os
import time

from pdf2image import convert_from_path

# Configure logging
logging.basicConfig(level=logging.INFO)

def pdf_to_images(pdf_path, dpi=400, thread_count=4):
    # Get the directory of the PDF file
    pdf_dir = os.path.dirname(pdf_path)
    # Create output folder in the same directory as the PDF
    output_folder = os.path.join(pdf_dir, "output_images")
    os.makedirs(output_folder, exist_ok=True)
    
    # Log start timestamp
    start_time = time.time()
    logging.info("Converting PDF to images...")

    # Load the PDF document using multiple threads
    pdf = convert_from_path(pdf_path, dpi=dpi, output_folder=output_folder, fmt="jpg", thread_count=thread_count)

   # Log end timestamp and calculate duration
    end_time = time.time()
    duration = end_time - start_time
    logging.info(f"PDF converted to {len(images)} images successfully in {duration:.2f} seconds")

    # Save each page as an image
    for i, image in enumerate(pdf):
        image_path = os.path.join(output_folder, f"page_{i+1}.jpg")  # Change extension if needed
        image.save(image_path, "JPEG")  # Change format if needed
        logging.info(f"Page {i+1}: Image saved at {image_path}")   
        # Close the image to release resources
        image.close()
       
    print(f"PDF converted to {len(pdf)} images successfully!")

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Convert PDF to images")
    parser.add_argument("--p", dest="pdf_path", required=True, help="Path to the PDF file")
    args = parser.parse_args()

    # Convert PDF to images with DPI set to 400 and using 4 threads
    pdf_to_images(args.pdf_path, dpi=400, thread_count=4)
