from cerebro import Cerebro
from voz import Voz
import memoria

cerebro = Cerebro()
voz = Voz()

print("Jarvis online. Digite 'sair' para encerrar.")
print("Comandos: /lembrar texto | /memoria | /esquecer número | /voz\n")

while True:
    pergunta = input("Você: ").strip()

    if pergunta.lower() in ("sair", "exit"):
        print("Jarvis: Até mais!")
        voz.falar("Até mais!")
        break
    if not pergunta:
        continue

    if pergunta == "/voz":
        voz.ativa = not voz.ativa
        print(f"\nJarvis: Voz {'ligada' if voz.ativa else 'desligada'}.\n")
        continue

    if pergunta.startswith("/lembrar "):
        memoria.salvar(pergunta[len("/lembrar "):].strip())
        print("\nJarvis: Anotado! Vou lembrar disso na próxima vez que eu ligar.\n")
        continue

    if pergunta == "/memoria":
        fatos = memoria.listar()
        if not fatos:
            print("\nJarvis: Ainda não tenho nada anotado.\n")
        else:
            print("\nJarvis: Isto é o que eu tenho anotado:")
            for id_fato, texto in fatos:
                print(f"  {id_fato}. {texto}")
            print()
        continue

    if pergunta.startswith("/esquecer "):
        try:
            if memoria.apagar(int(pergunta.split()[1])):
                print("\nJarvis: Pronto, esqueci isso.\n")
            else:
                print("\nJarvis: Não achei esse número.\n")
        except ValueError:
            print("\nJarvis: Use assim: /esquecer 2\n")
        continue

    print("\nJarvis está pensando...")
    resposta = cerebro.responder(pergunta)
    print(f"\nJarvis: {resposta}\n")
    voz.falar(resposta)