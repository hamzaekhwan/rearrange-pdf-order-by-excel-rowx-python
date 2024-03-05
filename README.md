# PDF Page Rearranger

A Python script that reorganizes PDF pages based on indexing information. Utilizes PyPDF2, Pandas, and PyMuPDF (fitz) for processing. Suitable for custom document compilations and archive organization.

## Features

- Extracts page numbers associated with specific IDs from a PDF.
- Rearranges PDF pages according to sequences defined in text or Excel files.
- Outputs a newly structured PDF and a text file listing the new page order.

## Prerequisites

- Python 3.x
- PyPDF2
- Pandas
- PyMuPDF (fitz)

Ensure you have Python installed, then run:

```bash
pip install PyPDF2 pandas pymupdf

## usage
  Place the script in your project directory.
  Prepare your PDF and either a text or Excel file with the desired page order.
  Run the script:
  bash
   
