import time
from google import genai
from google.genai import types
import config


class Cerebro:
    def __init__(self):
        self.client = genai.Client(
            api_key=config.GEMINI_API_KEY,
            http_options=types.HttpOptions(timeout=60000),  # 60 segundos
        )
        self.chat = self.client.chats.create(
            model=config.MODELO,
            config=types.GenerateContentConfig(
                system_instruction=config.SISTEMA,
            ),
        )

    def responder(self, pergunta: str) -> str:
        esperas = [3, 8, 15]  # segundos de espera entre as tentativas

        for tentativa in range(len(esperas) + 1):
            try:
                resposta = self.chat.send_message(pergunta)
                return resposta.text
            except Exception as e:
                erro = str(e)
                temporario = any(c in erro for c in ("503", "504", "429", "UNAVAILABLE", "DEADLINE_EXCEEDED"))

                if temporario and tentativa < len(esperas):
                    print(f"(Servidor ocupado, tentando de novo em {esperas[tentativa]}s...)")
                    time.sleep(esperas[tentativa])
                else:
                    return f"Tive um problema ao pensar nisso: {e}"