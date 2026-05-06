# LLM service
import ollama
from ollama import ResponseError

MODELO = "qwen2.5:7b"

def consultar_modelo(mensaje: str) -> dict:
    try:
        respuesta = ollama.chat(
            model=MODELO,
            messages=[
                {"role": "system", "content": "Eres un agente útil que responde de forma clara y concisa. Si no sabes la respuesta, di que no lo sabes y no inventes nada. trabajas en el centro de investigacion"
                "en ingenieria y ciencias aplicadas (ciicap) ubicado en cuernavaca morelos, mexico y tu función es responder preguntas relacionadas con el centro de investigación, sus proyectos, investigadores, publicaciones y cualquier otra información relevante. Si la pregunta no está relacionada con el centro de investigación, responde que no tienes información sobre ese tema."},
                {"role": "user", "content": mensaje}
            ]
        )

        contenido = respuesta["message"]["content"]
        tokens_entrada = respuesta.get("prompt_eval_count", 0)
        tokens_salida = respuesta.get("eval_count", 0)

        return {
            "respuesta": contenido,
            "modelo": MODELO,
            "tokens": {
                "entrada": tokens_entrada,
                "salida": tokens_salida,
                "total": tokens_entrada + tokens_salida
            }
        }

    except ResponseError as e:
        raise Exception(f"Ollama rechazó la solicitud: {e.error} (status: {e.status_code})")
    except ConnectionError:
        raise Exception("No se pudo conectar con Ollama — verifica que esté corriendo en el puerto 11434")
    except Exception as e:
        raise Exception(f"Error en el modelo {MODELO}: {str(e)}")