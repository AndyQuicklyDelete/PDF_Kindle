; To begin first open the Kindle for PC Desktop App
; Make sure you are on the page of the book you wish to capture from, before closing the Kindle for PC Desktop App
; Configue the User Settings of the Autoit script to match your Kindle For PC Desktop App and the book in question  
; And finally launching the PDF_Kindle Autoit Script

HotKeySet("{ESC}", "RunQuit")

Func RunQuit()
	WinClose("")
	Exit
EndFunc

PDF_Kindle()

Func PDF_Kindle()

	; User Settings
	$path_to_kindle = "C:\Program Files (x86)\Amazon\Kindle\Kindle.exe"
	$window_title = "Desktop-PC"

	; Number of estimated Pages
	$num_pages = 440

	; Run Kindle and Sleep to Wait for Program Launch
	Run($path_to_kindle)
	Sleep(5000)
	
	; Activate Window
	WinActivate($window_title, "")

	; Starting from the first page continue to capture screenShots
	Local $i = 1
	While $i <= $num_pages
		Sleep(2000) 
		Send("{SHIFTDOWN}{PRINTSCREEN}") ; Captures ScreenShot using Bumpshot Key Binding
		Sleep(2000) 
		Send("{SHIFTUP}") ; Release Screen Capture Key
		MouseClick("Left", 1250, 555, 1, 0)
		$i = $i + 1
		If @HotKeyPressed = "{ESC}" Then ExitLoop
	WEnd
	
	WinClose($window_title)
	
EndFunc
