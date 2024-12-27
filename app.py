import fitz  # PyMuPDF

def extract_lines_with_ans(pdf_path):
    ans_lines = []

    # Open the PDF
    doc = fitz.open(pdf_path)

    # Iterate through each page
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # Extract text from the page
        text = page.get_text()
        
        # Split the text into lines and filter lines starting with "Ans."
        lines = text.splitlines()
        ans_lines.extend(line.strip() for line in lines if line.strip().startswith("Ans."))
    
    return ans_lines


# Example usage
pdf_path = "example.pdf"  # Replace with your PDF file path
ans_lines = extract_lines_with_ans(pdf_path)

print("Lines starting with 'Ans.':")
for line in ans_lines:
    print(line)




# import fitz  # PyMuPDF
# import re    # For regex matching

# def extract_numbers_after_ans(pdf_path):
#     ans_numbers = []

#     # Open the PDF
#     doc = fitz.open(pdf_path)

#     # Iterate through each page
#     for page_num in range(len(doc)):
#         page = doc[page_num]
        
#         # Extract text from the page
#         text = page.get_text()
        
#         # Split the text into lines
#         lines = text.splitlines()
        
#         # Process each line
#         for line in lines:
#             line = line.strip()
#             if line.startswith("Ans."):
#                 # Extract the number immediately after "Ans."
#                 match = re.match(r"Ans\.\s*(\d+)", line)
#                 if match:
#                     ans_numbers.append(int(match.group(1)))  # Convert to integer and add to array
    
#     return ans_numbers


# # Example usage
# pdf_path = "example.pdf"  # Replace with your PDF file path
# numbers = extract_numbers_after_ans(pdf_path)




# import fitz  # PyMuPDF
# import re    # For regex matching
# from prettytable import PrettyTable  # For creating a table

# def extract_numbers_after_ans_with_table(pdf_path):
#     ans_numbers = []

#     # Open the PDF
#     doc = fitz.open(pdf_path)

#     # Iterate through each page
#     for page_num in range(len(doc)):
#         page = doc[page_num]
        
#         # Extract text from the page
#         text = page.get_text()
        
#         # Split the text into lines
#         lines = text.splitlines()
        
#         # Process each line
#         for line in lines:
#             line = line.strip()
#             if line.startswith("Ans."):
#                 # Extract the number immediately after "Ans."
#                 match = re.match(r"Ans\.\s*(\d+)", line)
#                 if match:
#                     ans_numbers.append(int(match.group(1)))  # Convert to integer and add to array

#     # Create a table
#     table = PrettyTable(["S.No", "Number"])
#     for idx, number in enumerate(ans_numbers, start=1):
#         table.add_row([idx, number])

#     return table


# # Example usage
# pdf_path = "example.pdf"  # Replace with your PDF file path
# table = extract_numbers_after_ans_with_table(pdf_path)

# print("Extracted Numbers Table:")
# print(table)




# import fitz  # PyMuPDF
# import re    # For regex matching
# import openpyxl  # For Excel file creation
# from openpyxl.styles import Font  # For styling the Excel cells

# def extract_numbers_after_ans(pdf_path):
#     ans_numbers = []

#     # Open the PDF
#     doc = fitz.open(pdf_path)

#     # Iterate through each page
#     for page_num in range(len(doc)):
#         page = doc[page_num]
        
#         # Extract text from the page
#         text = page.get_text()
        
#         # Split the text into lines
#         lines = text.splitlines()
        
#         # Process each line
#         for line in lines:
#             line = line.strip()
#             if line.startswith("Ans."):
#                 # Extract the number immediately after "Ans."
#                 match = re.match(r"Ans\.\s*(\d+)", line)
#                 if match:
#                     ans_numbers.append(int(match.group(1)))  # Convert to integer and add to array
    
#     return ans_numbers

# def save_to_excel(data, output_file):
#     # Create a new workbook
#     workbook = openpyxl.Workbook()
#     sheet = workbook.active
#     sheet.title = "Extracted Numbers"

#     # Add headers
#     sheet["A1"] = "S.No"
#     sheet["B1"] = "Number"

#     # Bold the "S.No" header
#     bold_font = Font(bold=True)
#     sheet["A1"].font = bold_font
#     sheet["B1"].font = bold_font

#     # Add data to Excel
#     for idx, number in enumerate(data, start=1):
#         sheet.append([idx, number])

#     # Save the workbook
#     workbook.save(output_file)
#     print(f"Data saved to {output_file}")

# # Example usage
# pdf_path = "example.pdf"  # Replace with your PDF file path
# numbers = extract_numbers_after_ans(pdf_path)

# # Save to Excel
# output_file = "extracted_numbers.xlsx"
# save_to_excel(numbers, output_file)



# import fitz  # PyMuPDF
# import re    # For regex matching
# import openpyxl  # For Excel file creation
# from openpyxl.styles import Font  # For styling the Excel cells

# def extract_numbers_after_ans(pdf_path):
#     ans_numbers = []

#     # Open the PDF
#     doc = fitz.open(pdf_path)

#     # Iterate through each page
#     for page_num in range(len(doc)):
#         page = doc[page_num]
        
#         # Extract text from the page
#         text = page.get_text()
        
#         # Split the text into lines
#         lines = text.splitlines()
        
#         # Process each line
#         for line in lines:
#             line = line.strip()
#             if line.startswith("Ans."):
#                 # Extract the number immediately after "Ans."
#                 match = re.match(r"Ans\.\s*(\d+)", line)
#                 if match:
#                     ans_numbers.append(int(match.group(1)))  # Convert to integer and add to array
    
#     return ans_numbers

# def save_to_excel(data, output_file):
#     # Create a new workbook
#     workbook = openpyxl.Workbook()
#     sheet = workbook.active
#     sheet.title = "Extracted Numbers"

#     # Add headers
#     sheet["A1"] = "S.No"
#     sheet["B1"] = "Number"

#     # Bold the headers
#     bold_font = Font(bold=True)
#     sheet["A1"].font = bold_font
#     sheet["B1"].font = bold_font

#     # Add data to Excel and bold the numbers in the "Number" column
#     for idx, number in enumerate(data, start=1):
#         # Insert data
#         sheet.append([idx, number])
#         # Bold the "Number" column (column B)
#         sheet[f"B{idx + 1}"].font = bold_font

#     # Save the workbook
#     workbook.save(output_file)
#     print(f"Data saved to {output_file}")

# # Example usage
# pdf_path = "example.pdf"  # Replace with your PDF file path
# numbers = extract_numbers_after_ans(pdf_path)

# # Save to Excel
# output_file = "extracted_numbers.xlsx"
# save_to_excel(numbers, output_file)




# import fitz  # PyMuPDF
# import re
# import openpyxl
# from openpyxl.styles import Font
# import streamlit as st
# from io import BytesIO

# def extract_numbers_after_ans(pdf_path):
#     ans_numbers = []

#     # Open the PDF
#     doc = fitz.open(pdf_path)

#     # Iterate through each page
#     for page_num in range(len(doc)):
#         page = doc[page_num]
        
#         # Extract text from the page
#         text = page.get_text()
        
#         # Split the text into lines
#         lines = text.splitlines()
        
#         # Process each line
#         for line in lines:
#             line = line.strip()
#             if line.startswith("Ans."):
#                 # Extract the number immediately after "Ans."
#                 match = re.match(r"Ans\.\s*(\d+)", line)
#                 if match:
#                     ans_numbers.append(int(match.group(1)))  # Convert to integer and add to array
    
#     return ans_numbers

# def create_excel(data):
#     # Create a new workbook
#     workbook = openpyxl.Workbook()
#     sheet = workbook.active
#     sheet.title = "Extracted Numbers"

#     # Add headers
#     sheet["A1"] = "S.No"
#     sheet["B1"] = "Number"

#     # Bold the headers
#     bold_font = Font(bold=True)
#     sheet["A1"].font = bold_font
#     sheet["B1"].font = bold_font

#     # Add data to Excel and bold the numbers in the "Number" column
#     for idx, number in enumerate(data, start=1):
#         # Insert data
#         sheet.append([idx, number])
#         # Bold the "Number" column (column B)
#         sheet[f"B{idx + 1}"].font = bold_font

#     # Save the workbook to a BytesIO object
#     output = BytesIO()
#     workbook.save(output)
#     output.seek(0)  # Reset the stream position
#     return output

# # Streamlit App
# st.title("PDF Number Extractor")
# st.write("Upload a PDF, and this app will extract numbers after 'Ans.' and generate an Excel file for download.")

# # File uploader (users can upload a PDF from any source on their local machine)
# uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

# if uploaded_file:
#     # Process the uploaded PDF (using the uploaded file object directly)
#     with st.spinner("Processing..."):
#         numbers = extract_numbers_after_ans(uploaded_file)

#     if numbers:
#         st.success("Numbers extracted successfully!")
#         st.write("Extracted Numbers:")
#         st.write(numbers)

#         # Create Excel file
#         excel_data = create_excel(numbers)

#         # Provide a download button for the Excel file
#         st.download_button(
#             label="Download Excel File",
#             data=excel_data,
#             file_name="extracted_numbers.xlsx",
#             mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#         )
#     else:
#         st.warning("No numbers found after 'Ans.' in the uploaded PDF.")




# import fitz  # PyMuPDF
# import re
# import openpyxl
# from openpyxl.styles import Font
# import streamlit as st
# from io import BytesIO

# def extract_numbers_after_ans(uploaded_file):
#     ans_numbers = []

#     # Open the uploaded file as a file-like object
#     doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

#     # Iterate through each page
#     for page_num in range(len(doc)):
#         page = doc[page_num]
        
#         # Extract text from the page
#         text = page.get_text()
        
#         # Split the text into lines
#         lines = text.splitlines()
        
#         # Process each line
#         for line in lines:
#             line = line.strip()
#             if line.startswith("Ans."):
#                 # Extract the number immediately after "Ans."
#                 match = re.match(r"Ans\.\s*(\d+)", line)
#                 if match:
#                     ans_numbers.append(int(match.group(1)))  # Convert to integer and add to array
    
#     return ans_numbers

# def create_excel(data):
#     # Create a new workbook
#     workbook = openpyxl.Workbook()
#     sheet = workbook.active
#     sheet.title = "Extracted Numbers"

#     # Add headers
#     sheet["A1"] = "S.No"
#     sheet["B1"] = "Number"

#     # Bold the headers
#     bold_font = Font(bold=True)
#     sheet["A1"].font = bold_font
#     sheet["B1"].font = bold_font

#     # Add data to Excel and bold the numbers in the "Number" column
#     for idx, number in enumerate(data, start=1):
#         # Insert data
#         sheet.append([idx, number])
#         # Bold the "Number" column (column B)
#         sheet[f"B{idx + 1}"].font = bold_font

#     # Save the workbook to a BytesIO object
#     output = BytesIO()
#     workbook.save(output)
#     output.seek(0)  # Reset the stream position
#     return output

# # Streamlit App
# st.title("PDF Number Extractor")
# st.write("Upload a PDF, and this app will extract numbers after 'Ans.' and generate an Excel file for download.")

# # File uploader (users can upload a PDF from any source on their local machine)
# uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

# if uploaded_file:
#     # Process the uploaded PDF (using the uploaded file object directly)
#     with st.spinner("Processing..."):
#         numbers = extract_numbers_after_ans(uploaded_file)

#     if numbers:
#         st.success("Numbers extracted successfully!")
#         st.write("Extracted Numbers:")
#         st.write(numbers)

#         # Create Excel file
#         excel_data = create_excel(numbers)

#         # Provide a download button for the Excel file
#         st.download_button(
#             label="Download Excel File",
#             data=excel_data,
#             file_name="extracted_numbers.xlsx",
#             mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#         )
#     else:
#         st.warning("No numbers found after 'Ans.' in the uploaded PDF.")
