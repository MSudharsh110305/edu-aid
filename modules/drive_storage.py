import os

def save_text_to_drive(text_content, filename="scraped_content.txt"):
    temp_drive_path = '/content/drive/MyDrive/TempLangChainData/'
    os.makedirs(temp_drive_path, exist_ok=True)
    
    file_path = os.path.join(temp_drive_path, filename)
    with open(file_path, 'w') as file:
        file.write(text_content)
    return file_path
