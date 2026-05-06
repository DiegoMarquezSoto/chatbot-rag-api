# schemas
from pydantic import BaseModel
from typing import Any, Optional

class APIResponse(BaseModel):
    correcto: bool
    mensaje: str
    objeto: Any = None
    
class OllamaRequest(BaseModel):
    mensaje: str
   