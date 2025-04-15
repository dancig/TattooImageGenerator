import torch
from diffusers import DiffusionPipeline


class ImageGenerator:

    def __init__(self):
        self.sd_pipeline = DiffusionPipeline.from_pretrained("./stable-diffusion-v1-5", torch_dtype=torch.bfloat16,
                                                             use_safetensors=True, safety_checker=None).to("cuda")

    def generate_image(self, prompt):
        return self.sd_pipeline(prompt, num_inference_steps=30).images[0]
