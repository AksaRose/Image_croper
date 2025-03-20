![Untitled-3](https://github.com/user-attachments/assets/f8416d90-40a6-4cfc-81e4-bca2ccf36202)
**Design Element Maker**
============================

### **🔍 Project Description**

Ever designed in figma? If you have, you would know the difficulty of croping an image/pattern to particular shape and to use it as a design element.First you have to create the shape and use mask to create the pattern/image to a specific shaped design element (thats whole lot of work, who does that). Thats were this project comes to play. For simplicity we could say  **Design element maker** is an image cropping API, powered by FastAPI. It allows users to takes in images and crop them into different shapes (circle, square, triangle, etc.). Wait a min, sounds like a bare minimum image cropper, naaah its not. It will help you crop images in the shape of Y2k illustration/design elements which could be used in your designs.  The backend processes the image and returns the cropped version, which can then be downloaded.
<br>
As there are time constraints and technical difficulties,we could only make it as a web app at the moment, but by further adding a manifest.json file it could be easily converted to figma plugin.
### **🌟 Features**

✅ Takes in images\
✅ Choose from multiple cropping shapes\
✅ Preview the cropped image before downloading\
✅ Download the cropped image in high quality\
✅ FastAPI backend for efficient processing

* * * * *

🎥 **Demo Video**
-----------------

[Add the video link here]

* * * * *

🛠 **Installation**
-------------------

### **🔧 Prerequisites**

Before running the project, ensure you have the following installed:

#### **Backend Requirements**

-   **Python** (3.8+ recommended)
-   **FastAPI** (for handling API requests)
-   **Uvicorn** (to run the FastAPI server)
-   **Pillow (PIL)** (for image processing)

#### **Frontend Requirements**

-   Any modern **web browser** (Chrome, Firefox, Edge, etc.)
-   A local HTTP server (e.g., Python's built-in HTTP server)

* * * * *

🏃‍♂️ **Steps to Run**
----------------------

### **Backend Setup (FastAPI Server)**

1️⃣ **Clone the repository**

bash


`https://github.com/AksaRose/Image_croper.git`
`cd grab-a-pi-hacknight`

2️⃣ **Create a virtual environment & activate it**

bash


`python -m venv .venv`
`source .venv/bin/activate   # For Mac/Linux`
# OR
`.venv\Scripts\activate      # For Windows`

3️⃣ **Install backend dependencies**

bash


`pip install fastapi uvicorn pillow`

4️⃣ **Run the FastAPI backend**

bash

`uvicorn main:app --host 127.0.0.1 --port 8000 --reload`

The API should now be running at **[http://127.0.0.1:8000](http://127.0.0.1:8000/)** 🎯

* * * * *

### **Frontend Setup**

1️⃣ **Navigate to the frontend directory**

2️⃣ **Start a local HTTP server**

bash

`python -m http.server 5500`

3️⃣ **Open the frontend in a browser**\
Go to **http://127.0.0.1:5500/index.html** in your browser.

* * * * *


* * * * *

📡 **API Endpoints**
--------------------

### **1️⃣ Upload & Crop Image**

**Endpoint:**

http://127.0.0.1:8000/crop

`POST /crop`

**Request Body:**

-   `file` (image file)
-   `shape` (string: "circle", "square", "triangle", etc.)

**Response:**

-   Cropped image (returned as a downloadable file)

* * * * *

🔥 **Technologies Used**
------------------------

-   **FastAPI** → High-performance backend framework
-   **Uvicorn** → ASGI server for FastAPI
-   **Pillow (PIL)** → Image processing library
-   **HTML/CSS/JavaScript** → Frontend for user interaction

* * * * *

🎉 **Happy Hacking!** 🚀
