How to run this locally:

1. Install Necessary Tools:
Python (if not already installed): Install Python from the official website.
Node.js (if using Arduino or server-side scripting): Install Node.js from the official website.

2. Set Up the Web Application:
Create a project folder and place your index.html, styles.css, and script.js files in it.
3. Running the HTML/JavaScript Project:
Using a Live Server Extension (Recommended for Ease):

Right-click on index.html and select "Open with Live Server". This will open your project in a browser and automatically reload the page when you make changes.
Running with a Simple HTTP Server (Python):

Open a terminal (or command prompt) in your project folder.
Run the following command:
For Python 3:
bash
Copy code
python -m http.server 8000
Open a browser and go to http://localhost:8000 to view your project.

4. Setting Up OpenCV for Air Canvas:
Install OpenCV for Python:
Open a terminal and run:
bash
Copy code
pip install opencv-python
Run the Air Canvas Script:
Create a Python script (e.g., air_canvas.py) with your OpenCV code for gesture recognition and drawing.
Run the script from the terminal:
bash
Copy code
python air_canvas.py


5. Arduino Integration (Optional):
Install Arduino IDE: If you're using Arduino, download and install the Arduino IDE.
Set Up Serial Communication:
Write your Arduino code and upload it to the Arduino board.
Make sure your Arduino is connected to the correct serial port.
Connect Arduino with Node.js (If Needed):
Use serialport library in Node.js for serial communication. Install it using:
bash
Copy code
npm install serialport
Run your Node.js server that handles serial communication.


6. Testing Speech-to-Text and Text-to-Speech Features:
Ensure your browser supports the Web Speech API (Chrome is recommended).
Allow microphone access when prompted to use the Speech-to-Text feature.

7. Final Check:
Open index.html in your browser and test all the functionalities: TTS, STT, customization options, air canvas, and Arduino integration (if applicable).
Summary:
Use a simple server (like Live Server or Python's HTTP server) to run the web app.
Install and run OpenCV for the air canvas functionality.
Set up Arduino and Node.js for optional physical feedback.








## Team Details

*Team Name:* BYTE MECHANICS

*Team Leader:* [@ravvii23](https://github.com/ravvii23)

*Team Members:*

- *MEMBER_1* - 2023UIC3589 - [@ravvii23](https://github.com/ravvii23)
- *MEMBER_2* - 2023UIC3560 - [@Aditya-eng](https://github.com/Aditya-eng)
- *MEMBER_3* - 2023UIC3555 - [@ashandg4](https://github.com/ashandg4)
- *MEMBER_4* - 2023UIC3501 - [@Hrydya](https://github.com/Hrydya)
- *MEMBER_5* - 2023UIC3584 - [@Adityamohan01](https://github.com/Adityamohan01)
- *MEMBER_6* - 2023UIC3570 - [@riddhisrivastava1516](https://github.com/riddhisrivastava1516)
