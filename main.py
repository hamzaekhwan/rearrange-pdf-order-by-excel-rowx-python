import fitz
import pandas as pd
import PyPDF2

def generate_integer_list(starting_integer, count):
    integer_list = []
    for i in range(count):
        integer_list.append(starting_integer + i)
    return integer_list

def pdf_to_dict(pdf_file):
    
    pdfFileObj = open(pdf_file, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    id_count = {}
    prev_id = 0
    first_time = True
    page_count = 0

    for index in range(len(pdfReader.pages)):
        pageObj = pdfReader.pages[index]
        text = pageObj.extract_text()
        visit_split = text.split('Visit')

        if len(visit_split) > 1:  # The page is an indexing page
            if first_time:
                prev_id = visit_split[1].split()[0]
                first_time = False
            else:
                id = visit_split[1].split()[0]
                id_count[int(prev_id)] = page_count + 1
                page_count = 0
                prev_id = id
        else:  # Following page
            page_count += 1

    # Count the pages until the last indexing page
    id_count[int(prev_id)] = page_count

    pdfFileObj.close()

    ### Modify the dictionary
    starting = 1

    for visit, count in id_count.items():
        page_list = generate_integer_list(starting, count)
        starting = starting + count
        id_count[int(visit)] = page_list

        

   
    


    return id_count







def rearrange_dict_as_txt(page_dict):

    new_dict = {}
    with open(input_file, 'r') as file:
            for line in file:
                key = line.strip()
                if int(key) in page_dict:
                    new_dict[key] = page_dict[int(key)]
    return new_dict                

    
    
def rearrange_dict_as_xlsx(page_dict):
        new_dict = {}

    
    

        df = pd.read_excel(input_file,header=None)
        for index, row in df.iterrows():
            key = str(row[0])  # افتراض أن العمود الأول يحتوي على الأرقام
            if int(key) in page_dict:
                    new_dict[key] = page_dict[int(key)]

        return new_dict            



def rearrange_pdf(pdf_file,dict):
# Create a new PDF file
    output_pdf = fitz.open()

    with fitz.open(pdf_file) as pdf:
        # Copy the pages to a new file in the specified order
        for key, value in dict.items():
            for page_number in value:
                if 1 <= page_number <= len(pdf):
                    output_pdf.insert_pdf(pdf, from_page=page_number - 1, to_page=page_number - 1)


    output_file = input("Please enter the name of the output file (including the extension): ")
    output_pdf.save(output_file)
    print('Pages successfully rearranged and saved to the output file: ' + output_file)

   


def write_to_txt(new_dict):
    output_txt=input("Please enter the name of the txt output file(which has pages number) : ")
    with open(output_txt, 'w') as file:
        # استخدام حلقة للوصول إلى قائمة الأرقام وطباعتها في الملف
        for key, value in new_dict.items():
            for number in value:
                if value.index(number) != (len(value)-1):
                    file.write(f'{number}-')

                else :
                    if key != list(new_dict)[-1]:
                        file.write(f'{number},')
                    else:    
                        file.write(f'{number}')


    print ("txt file created sucessfully")        



pdf_file=input("Please enter the name of the pdf file : ")

first_dict=pdf_to_dict(pdf_file)

input_file = input("Please enter the name of the text or Excel file: ")
if input_file.lower().endswith('.txt'):
    new_dict=rearrange_dict_as_txt(first_dict)

elif input_file.lower().endswith('.xlsx'):    
    new_dict=rearrange_dict_as_xlsx(first_dict)

else:
        print("File format is not supported. It should be a text file (.txt) or an Excel file (.xlsx).")
        exit(1)
rearrange_pdf(pdf_file,new_dict)
write_to_txt(new_dict)

