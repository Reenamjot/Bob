import os
import requests
import openai  # Correcting the import from `OpenAI` to `openai`

openai.api_key = 'my-api-key'

def download_image(filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
    else:
        print("Error downloading image from URL:", url)

def filename_from_input(prompt):
    # Remove all non-alphanumeric characters from the prompt except spaces.
    alphanum = ""
    for character in prompt:
        if character.isalnum() or character == " ":
            alphanum += character
    # Split the alphanumeric prompt into words.
    alphanum_split = alphanum.split()
    if len(alphanum_split) > 3:
        alphanum_split = alphanum_split[:3]
    # Join the words with underscores and return the result.
    return "images/" + "_".join(alphanum_split)

def get_image(prompt, model="dall-e-2"):
    n = 2  # Number of images to generate

    # Generate images
    image_response = openai.Image.create(
        prompt=prompt,
        n=n,
        size="1024x1024"
    )

    # Ensure images directory exists
    os.makedirs("images", exist_ok=True)

    # Save images and return response
    for i in range(n):
        filename = filename_from_input(prompt) + "_" + str(i + 1) + ".png"
        download_image(filename, image_response['data'][i]['url'])

    return image_response

prompt = input("Enter a prompt: ")
response = get_image(prompt)
print(response)

print("----------------------------------------------")
print("Images saved to", filename_from_input(prompt) + "_*.png!")

from IPython.display import Image, display
display(Image(filename_from_input(prompt) + '_1.png'))
display(Image(filename_from_input(prompt) + '_2.png'))