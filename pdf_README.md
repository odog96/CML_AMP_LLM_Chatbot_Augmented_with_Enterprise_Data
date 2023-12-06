Script Usage Guide
This script processes PDF and TXT files. For PDFs, it extracts text and saves the text as TXT files. For TXT files, it processes and chunks the text into smaller pieces. The processed TXT files are then saved to a specific directory.

Required Folder Structure:
To effectively use this script, you need the following folder structure:

staged_files: Place all the PDF and TXT files you wish to process in this directory.
staged_files_completed: This directory will contain the PDF files that have been successfully processed. It will be automatically created if it doesn't exist.
output_text_files: (Not actively used in the current version of the script but kept for future reference.)
data: This directory will contain processed TXT files chunked into smaller pieces.
old_data: Any existing data in the data directory will be moved to this folder before the new processing begins.
If any of the above folders except staged_files_completed and output_text_files don't exist, they will be created automatically by the script.

Steps to Use the Script:
Place all the PDF and TXT files you wish to process into the staged_files directory.
Run the script.
If there are files in the old_data folder, you will receive a prompt asking if you want to delete those files. Confirm to proceed or decline to halt the script.
The script will process the PDF files first. Once processed, they will be moved to the staged_files_completed directory.
TXT files will then be processed and chunked. The processed files will be saved to the data directory.
Error Handling:
If the staged_files directory is not found, an error will be raised.
If no .txt files are found in the staged_files directory, an error will be raised.
Other Notes:
The script uses the PDFMiner library to extract text from PDFs.
The script requires the tkinter library for popup messages.
Dependencies:
To run this script, ensure you have the required libraries installed. You can usually install these with pip:

