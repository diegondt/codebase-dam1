from huggingface_hub import InferenceClient
from create_env import TOKEN
import PIL

client = InferenceClient("black-forest-labs/FLUX.1-dev", token=TOKEN)

# output is a PIL.Image object
image = client.text_to_image("Astronaut riding a horse")

image.save("a.png", "png")