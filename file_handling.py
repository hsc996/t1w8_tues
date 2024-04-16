readme_file = open("readme.txt", "w") # "w" for .write mode, "a" for .append mode
# Can use r+ to read+write

# print(readme_file.read())

readme_file.write("Hello Everyone")

readme_file.close()
