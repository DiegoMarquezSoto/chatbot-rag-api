# chat routes
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.models import schemas
#
from app.services import llm_service

router = APIRouter(prefix="/chat",
                   tags=["chat"],)


@router.post("/", response_model=schemas.APIResponse, status_code=status.HTTP_200_OK)
def consultar_modelo(request: schemas.OllamaRequest):
    try:
        resultado = llm_service.consultar_modelo(request.mensaje)
        return schemas.APIResponse(
            correcto=True,
            mensaje="Consulta ejecutada correctamente",
            objeto=resultado
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "correcto": False,
                "mensaje": f"Error al consultar el modelo: {str(e)}",
                "objeto": None
            }
        )