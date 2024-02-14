# PDF to Image Converter

This is a Python script that converts a PDF file into a series of images. Each page of the PDF will be converted into a separate image file.

## Requirements

- Python 3.x
- pdf2image library
- Poppler (PDF rendering library)

## Installation

1. **Install Python 3.x:** If you don't have Python installed on your system, download and install it from the [official Python website](https://www.python.org/).

2. **Install pdf2image library:** Install the `pdf2image` library using pip. Open a terminal or command prompt and run the following command:
```pip install pdf2image```


3. **Install Poppler:** Poppler is required for rendering PDF files. Depending on your operating system:

- **For macOS**: If you have Homebrew installed, you can install Poppler via Homebrew using the following command:
  ```
  brew install poppler
  ```

- **For Linux**: Use your package manager to install Poppler. For example, on Ubuntu, you can use:
  ```
  sudo apt-get install poppler-utils
  ```

- **For Windows**:
Go to the Poppler for Windows repository on [GitHub](https://github.com/oschwartz10612/poppler-windows/releases) and download the latest release. You'll typically want to download the poppler-x.x.x_x64 or poppler-x.x.x_x86 zip file, depending on whether your system is 64-bit or 32-bit.

Extract the zip file:
After downloading the zip file, extract its contents to a location on your system. For example, you could extract it to C:\poppler.

Add Poppler to PATH:
Next, you need to add the directory containing the Poppler binaries to your system's PATH environment variable. Here's how you can do it:

Right-click on "This PC" or "My Computer" and select "Properties."
Click on "Advanced system settings" on the left side.
In the System Properties window, click on the "Environment Variables" button.
In the Environment Variables window, under "System variables," find the "Path" variable and select it. Click on the "Edit" button.
In the Edit Environment Variable window, click on the "New" button and add the path to the directory containing the Poppler binaries (e.g., C:\poppler\bin).
Click "OK" on all windows to save the changes.
Verify installation:
Open a new command prompt window and type pdftoppm -v. You should see the version information for Poppler printed in the command prompt. If you see this information, Poppler has been installed successfully.

## Usage

To convert a PDF file to images, run the following command in your terminal or command prompt:
  
```bash 
python3 script.py --p path/to/your/pdf/file.pdf --t 8
```
## You can also specify the number of threads to use for the conversion process using the --t (or --threads) parameter. By default, the script uses 4 threads for the conversion process.

## Example

```bash
python script.py --p example.pdf --t 8

``` 
