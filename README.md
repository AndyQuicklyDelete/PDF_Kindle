# PDF_Kindle
Create PDFs of Kindle Desktop App eBooks with Python and Autoit3 (Software takes Screenshots and Compiles them in to PDF)

**Preparation**

1) Download Desktop Screenshot Capture Software like Greenshot (https://getgreenshot.org/) or Bumpshot (https://www.andyquickdelete.info/portfolio/static/Desktop/Bumpshot-1.0.7-win64.msi) and configure it to save screenshots to your Desktop and in a folder called **ScreenShots**. The command to capture active window screenshots should be **shift+printscreen**

2) Make sure Python > 3.8 is installed and add the following libraries: **pip install Pillow fpdf pyautogui**

3) Open Kindle and the document you wish to capture (make sure you are on page 1) locate the Kindle navigation arrow in the open document and find the mouse coordinates position on top of this arrow using **find_mouse_coordinates.py**. You should also get the **top left, top right, bottom left, and bottom right** readable area of the document, these coordinates are for cropping the screenshots before turning them into a pdf.

4) Open PDF_Kindle.au3 and change the **$window_title = "Desktop-PC - Kindle - Srimad Bhagavatam"** variable to that of your open document. Change the **MouseClick("Left", 1250, 555, 1, 0)** function values of 1250, and 555 to match the Kindle arrow position found using **mouse_coordinates.py**. The MouseClick function is found in two locations inside the script. You also need to change the **$num_pages = 440** variable to match your open document.

5) Open **cropping_for_kindle.py** and change the variables located on lines 16, 17, 18, 19 to match your document using the coordinates you found in step 3.

6) Close your Kindle Desktop app and run the **PDF_Kindle.au3** file. It will open the Kindle Desktop app and the last open document (which should be the book you want to copy). Make sure your screenshot capture software is running in the background, be sure to disable your screensaver and Desktop sleep temporarily. If a mistake is made you can hit the **ESC** key on your keyboard to halt the script and manually adjust everything again, I suggest doing this once or twice just to check everything is working properly.

7) Finally when all that is done, you can run the python script **cropping_for_kindle.py**. Once completed a pdf will be saved to the same directory as the python script in a folder called output. Enjoy :-) 
