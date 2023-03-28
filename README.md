# Live Streaming IP Camera Video over the Internet using FastAPI
This script allows you to live stream your IP camera video over the internet using FastAPI. It also provides the option to use the ipWebcam application to access your mobile camera feed in case you don't have an IP camera.


# Prerequisites
Before you can use this script, you will need to have the following:

1. An IP camera or the ipWebcam application installed on your mobile device.
2. Python 3.x installed on your computer.
3. FastAPI and uvicorn installed on your computer. You can install them using pip by running pip install fastapi uvicorn.

# Usage
1. Clone this repository to your local machine using the following command:
     git clone https://github.com/NiharikaSarma001/Live-Webstreaming

2. Navigate to the directory where the repository was cloned using the following command:
    cd <name of the directory>

3. Open the main.py file and modify the CAMERA_URL variable to point to your IP camera URL or the ipWebcam application URL.

4. Run the following command to start the server:
    uvicorn main:app --reload

5. Open your web browser and navigate to http://localhost:8000/ to view the live stream.

6. To view the live stream over the internet, you will need to use tunneling. One option for tunneling is to use ngrok. To use ngrok, download and install it from https://ngrok.com/download. Then, run the following command to start the tunnel:
    
     ngrok http 8000

7. Once the tunnel is running, ngrok will provide a public URL that you can use to access the live stream from anywhere.
