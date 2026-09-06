import torch
from diffusers import DiffusionPipeline
from diffusers.utils import export_to_video

pipeline = DiffusionPipeline.from_pretrained("damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16")
pipeline.enable_model_cpu_offload()
pipeline.enable_vae_slicing()

prompt = "Confident teddy bear surfer rides the wave in the tropics"
video_frames = pipeline(prompt).frames[0]
export_to_video(video_frames, "modelscopet2v.mp4", fps=10)
