from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from fastapi.templating import Jinja2Templates

# Resolve template directory relative to this file
template_dir = Path(__file__).parent / "templates"

# Create Jinja2 environment with caching disabled
env = Environment(loader=FileSystemLoader(str(template_dir)), cache_size=0)
templates = Jinja2Templates(env=env)
