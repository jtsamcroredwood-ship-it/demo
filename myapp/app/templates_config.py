from pathlib import Path
from fastapi.templating import Jinja2Templates

# Resolve template directory relative to this file
template_dir = Path(__file__).parent / "templates"
templates = Jinja2Templates(directory=str(template_dir))
