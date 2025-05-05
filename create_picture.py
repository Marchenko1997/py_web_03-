import os
from pathlib import Path


base = Path("picture")


structure = {
    "icons": ["e-learning_icon.jpg", "mongodb.jpg"],
    "Logo": ["IBM+Logo.png", "ibm.svg", "logo-tm.png"],
    "Other/Icons": ["1600.png"],
    "Other": ["golang.png", "hqdefault.jpg", "nodejslogo.png"],
    "wallpaper": ["js.png", "node-wallpaper.jpg"],
    "": ["bot-icon.png", "javascript_encapsulation.jpg"],
}


for folder, files in structure.items():
    folder_path = base / folder
    folder_path.mkdir(parents=True, exist_ok=True) 
    for file_name in files:
        file_path = folder_path / file_name
        file_path.touch()  
        print(f"Створен файл: {file_path}")

print("\n✅ Структуру папки 'picture' створено!")
