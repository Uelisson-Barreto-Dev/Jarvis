import time
from google import genai
from google.genai import types
import config
import memoria


class Cerebro:
    def __init__(self):
        memoria.iniciar()
        self.client = genai.Client(
            api_key=config.GEMINI_API_KEY,
            http_options=types.HttpOptions(timeout=60000),
        )
        self.chat = self.client.chats.create(
            model=config.MODELO,
            config=types.GenerateContentConfig(
                system_instruction=self._montar_sistema(),
            ),
        )

    def _montar_sistema(self):
        fatos = memoria.listar()
        if not fatos:
            return config.SISTEMA
        lista = "\n".join(f"- {texto}" for _, texto in fatos)
        return (
            config.SISTEMA
            + "\n\nCoisas que você já sabe sobre o Uelisson "
            "(use só quando forem relevantes para a conversa):\n"
            + lista
        )

    def responder(self, pergunta: str) -> str:
        esperas = [3, 8, 15]

        for tentativa in range(len(esperas) + 1):
            try:
                resposta = self.chat.send_message(pergunta)
                return resposta.text
            except Exception as e:
                erro = str(e)
                temporario = any(
                    c in erro
                    for c in ("503", "504", "429", "UNAVAILABLE", "DEADLINE_EXCEEDED")
                )
                if temporario and tentativa < len(esperas):
                    print(f"(Servidor ocupado, tentando de novo em {esperas[tentativa]}s...)")
                    time.sleep(esperas[tentativa])
                else:
                    return f"Tive um problema ao pensar nisso: {e}"