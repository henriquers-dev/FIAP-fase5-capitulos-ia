from diffusers import AudioLDMPipeline
from IPython.display import Audio
import torch

model_id = "cvssp/audioldm-s-v2"

# Verifica se há GPU disponível; float16 só funciona bem em CUDA
device = "cuda" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if device == "cuda" else torch.float32

pipe = AudioLDMPipeline.from_pretrained(model_id, torch_dtype=torch_dtype)
pipe = pipe.to(device)

generator = torch.Generator(device).manual_seed(0)
