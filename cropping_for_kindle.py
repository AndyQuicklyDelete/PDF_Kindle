import os, sys
from os import listdir
from PIL import Image
from fpdf import FPDF

## USER SETTINGS ##

screen_shots_folder = "C:\\Users\\Kalipso\\Desktop\\ScreenShots\\"
temp_dir = os.getcwd() + "\\temp\\"
pdf_dir = os.getcwd() + "\\pdf\\"

# Cropping Dimensions, this will be different for each persons computer
# Adjust to your specification. I used Photoshops info window to find the
# Left/Top and Right/Bottom values

left = 447
top = 101
right = 1056
bottom = 1010

## END BASIC USER SETTINGS ##

isExist = os.path.exists(screen_shots_folder)
if not isExist:
    print("[-] Error: ScreenShot directory does not exist")
    sys.exit(0)

isExist = os.path.exists(temp_dir)
if not isExist:
    os.makedirs(temp_dir)

isExist = os.path.exists(pdf_dir)
if not isExist:
    os.makedirs(pdf_dir)

count = 0
folder_dir = screen_shots_folder
for images in os.listdir(folder_dir):    
    im = Image.open(folder_dir + images)

    im1 = im.crop((left, top, right, bottom))
    im1.save(os.getcwd() + "\\temp\\" + images)

    print("[+] Cropping of file: " + images + " successful")
    count += 1

print("[+] Total number of pages: " + str(count))
print("[+] Generating PDF file from cropped images")

image_list = []
folder_dir = temp_dir

for images in os.listdir(folder_dir):
    image_list.append(folder_dir + images)

pdf = FPDF()
for img in image_list:
    pdf.add_page()
    pdf.image(img, 0, 0, 210, 297)
    
pdf.output(pdf_dir + "\\output.pdf", "F")

print("[+] PDF file has been generated")
