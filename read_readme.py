import base64

with open("readme.md", "rb") as readme_file:
    encoded_string = base64.b64encode(readme_file.read())
