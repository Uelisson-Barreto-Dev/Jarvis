from cerebro import Cerebro

cerebro = Cerebro()
print("Jarvis online. Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ").strip()
    if pergunta.lower() in ("sair", "exit"):
        print("Jarvis: Até mais!")
        break
    if not pergunta:
        continue
    print("\nJarvis está pensando...")
    print(f"\nJarvis: {cerebro.responder(pergunta)}\n")