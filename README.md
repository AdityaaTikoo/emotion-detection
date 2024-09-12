# Getting Started

## Requirements 
- Download these using your package manager.
1. python3
2. pip3

## Setting up virtual environment 
- Setting up a virtual environment is very important otherwise your program will not work properly.

```bash
# Creating a virtual environment called env

python3 -m venv env

# Activating that environment 

source env/bin/activate
```

## Requirements 
```bash
pip install opencv-python fer numpy tensorflow
```

## Program Options 
1. If your using the `live_face_detection.py` program then it will access your camera, no parameters required.
2. If your using the `picture_recognition.py` program then it will require an `image path` parameter.

## How to run ?

```bash
# Run the live_face_detection.py program
python3 live_face_detection.py

# Run the picture_recognition.py
python3 picture_detection.py
```

### Additional 
Choose any picture from the `images` folder and update the `image_path` manually.

---