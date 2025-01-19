import base64

with open("TEAM_P0P0_PRESENTS.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
with open("encoded_image.txt", "w", encoding='utf-8') as text_file:
    text_file.write(encoded_string)