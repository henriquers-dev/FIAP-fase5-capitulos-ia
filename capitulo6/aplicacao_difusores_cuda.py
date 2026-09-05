from diffusers import StableDiffusionPipeline
import torch

# Carrega a pipeline pré-treinada (latent diffusion + decoding)
model_id = "runwayml/stable-diffusion-v1-5"  # ou outro checkpoint
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")  # mover para GPU

prompt = "uma pintura digital de um filhote de gato sentado em uma floresta encantada, luz suave, estilo arte conceitual, alta resolução"
image = pipe(prompt, guidance_scale=7.5, num_inference_steps=50)["images"][0]

# Salvar a imagem gerada
image.save("gato_floresta.png")
