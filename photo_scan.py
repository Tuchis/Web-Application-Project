"""
MODULE DOCSTRING
"""
import os
import pytesseract

print(os.listdir('dat'))
for elem in os.listdir('dat'):
    text = pytesseract.image_to_string(f'dat/{elem}', lang="ukr+eng")
    with open(f"dat/{elem[:-5]}.txt", "w", encoding="utf-8") as file:
        file.write(text)
