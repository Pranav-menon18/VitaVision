import gdown

file_id = "1ewoR-VB362vE4r0DQ3cO9QPzhxwoytiA"  # Replace with your actual Google Drive file ID
output = "my_model.tflite"

gdown.download(f"https://drive.google.com/uc?id={file_id}", output, quiet=False)

print("Download complete:", output)



