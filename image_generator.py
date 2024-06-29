import click
import os
import torch
from diffusers import StableDiffusionPipeline


@click.command()
@click.option('--desc', prompt='Enter a Image Description')
@click.option('--num_images', default=1, help='Number of times to process the image.')
def generate_image(desc, num_images):
    # Check if CUDA is available
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Using device: {device}')

    # Load the model and move it to the appropriate device
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5").to(device)

    # Generate images on the selected device
    images = pipe(desc, num_images=num_images, height=512, width=512).images

    # Define output directory
    output_dir = os.getcwd()

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the generated images
    for i, img in enumerate(images):
        img.save(os.path.join(output_dir, f"image_{i + 1}.png"))
        print(f"Image {i + 1} saved at {os.path.join(output_dir, f'image_{i + 1}.png')}")


if __name__ == '__main__':
    generate_image()
