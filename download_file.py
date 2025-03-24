import requests

file_id = "1ewoR-VB362vE4r0DQ3cO9QPzhxwoytiA"  # Replace with your actual file ID
url = f"https://drive.google.com/uc?export=download&id={file_id}"

response = requests.get(url, stream=True)

with open("my_model.tflite", "wb") as file:
    for chunk in response.iter_content(1024):
        file.write(chunk)

print("Download complete!")
