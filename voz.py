import re
import pyttsx3


class Voz:
    def __init__(self):
        self.ativa = True

    def _limpar(self, texto):
        # tira símbolos do markdown (como ** e #) para não serem lidos em voz alta
        return re.sub(r"[*_`#>]", "", texto)

    def falar(self, texto):
        if not self.ativa:
            return
        try:
            motor = pyttsx3.init()
            motor.setProperty("rate", 175)
            for v in motor.getProperty("voices"):
                info = f"{v.name} {v.id}".lower()
                if "maria" in info or "pt-br" in info or "brazil" in info or "portugu" in info:
                    motor.setProperty("voice", v.id)
                    break
            motor.say(self._limpar(texto))
            motor.runAndWait()
        except Exception as e:
            print(f"(Não consegui falar: {e})")