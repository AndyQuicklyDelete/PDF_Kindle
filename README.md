# PDF_Kindle
Create PDFs of Kindle Desktop App eBooks with Python and Autoit3 (Software takes Screenshots and Compiles them to PDF)

**Preparation**

1) Download Desktop Screenshot Capture Software like Greenshot (https://getgreenshot.org/) or Bumpshot (https://www.andyquickdelete.info/portfolio/static/Desktop/Bumpshot-1.0.6-win64.msi) and configure it to save screenshots to your Desktop and in a folder called **ScreenShots** the command to capture active window screenshots should be **shift+printscreen**

2) Make sure Python > 3.8 is installed and add the following libraries: **pip install Pillow fpdf pyautogui**

3) Open Kindle and the book you wish to capture (make sure you are on page 1) locate the Kindle arrow: https://images.suck-o.com/static/images/image_uploads.file_upload.b1a197437223c13d.S2luZGxlLUFycm93LmpwZw==.jpg in the open document and find your mouse coordinates position on top of this arrow using **find_mouse_coordinates.py**. You should also get the top left, top right, bottom left, and bottom right positions of the document, these coordinates are for cropping the screenshots before turning them into a pdf. You will need to adjust these for your screen size inside the python script.

4) Open PDF_Kindle.au3 and change the **$window_title = "Desktop-PC - Kindle - Srimad Bhagavatam"** variable to that of your open book. Change the **MouseClick("Left", 1250, 555, 1, 0)** function values 1250, and 555 to match the arrow position found using **mouse_coordicnates.py** the MouseClick function is found in two places and both will be needed to change. You also need to change the **$num_pages = 440** variable to match your document.

5) Open **cropping_for_kindle.py** and change the variables located on lines 16, 17, 18, 19 to match your document using the coordinates you found in step 3.

6) Close your Kindle Desktop app and run the **PDF_Kindle.au3** file. It will open the Kindle Desktop app and the last open document (which should be the book you want to copy). Make sure your screenshot capture software is running in the background, be sure to disable your screensaver temporarily. You can check your various screenshots to make sure no mistakes are made during the process. If a mistake is made you can hit the **ESC** on your keyboard to halt the script and manually adjust everything again.

7) Finally when that is all done, you can run the python script **cropping_for_kindle.py**. Once completed a pdf will be saved to the same directory as the python script in a folder called output. 
