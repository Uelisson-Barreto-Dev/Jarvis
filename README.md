# 🤖 Jarvis

Assistente virtual em Python inspirado no Jarvis do Homem de Ferro. Ele conversa pelo terminal, ajuda com estudos, dúvidas e projetos, lembra de informações entre as sessões e responde falando em voz alta.

O "cérebro" usa a API do Google Gemini e fica isolado em um único módulo, então trocar de modelo (ou de provedor de IA) exige mudar pouca coisa.

## ✨ Funcionalidades

- 💬 **Conversa com IA** usando o Gemini, com o histórico da conversa mantido durante a sessão
- 🧠 **Memória persistente** em SQLite: o Jarvis lembra do que você pediu mesmo depois de fechar o programa
- 🔊 **Voz de saída**: as respostas são lidas em voz alta (pyttsx3, offline)
- 🔁 **Tentativas automáticas** quando o servidor está ocupado (erros 503, 504 e 429)
- 🔐 **Chave de API protegida** em arquivo `.env`, fora do repositório

## 🧰 Tecnologias

- Python 3
- [google-genai](https://pypi.org/project/google-genai/) (API do Gemini)
- python-dotenv
- SQLite (módulo `sqlite3` do Python)
- pyttsx3 (síntese de voz)

## 📁 Estrutura do projeto

```
Jarvis/
├── main.py       # loop principal e comandos
├── cerebro.py    # comunicação com o Gemini e tentativas automáticas
├── memoria.py    # banco de dados SQLite (fatos lembrados)
├── voz.py        # voz de saída
├── config.py     # modelo, personalidade (SISTEMA) e leitura da chave
├── .env          # sua chave de API (não vai para o GitHub)
└── .gitignore
```

## 🚀 Como rodar

### 1. Clone o repositório

```bash
git clone https://github.com/Uelisson-Barreto-Dev/Jarvis.git
cd Jarvis
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

No Linux ou Mac, use `source venv/bin/activate` no lugar do segundo comando.

### 3. Instale as bibliotecas

```bash
pip install google-genai python-dotenv pyttsx3
```

### 4. Configure a chave da API

Crie uma chave gratuita no [Google AI Studio](https://aistudio.google.com) e crie um arquivo chamado `.env` na raiz do projeto, com este conteúdo:

```
GEMINI_API_KEY=sua_chave_aqui
```

Nunca envie esse arquivo para o GitHub. O `.gitignore` do projeto já o ignora.

### 5. Execute

```bash
python main.py
```

## 💻 Comandos

| Comando | O que faz |
|---|---|
| `/lembrar texto` | Salva uma informação na memória do Jarvis |
| `/memoria` | Lista tudo que ele tem anotado |
| `/esquecer número` | Apaga um item da memória pelo número da lista |
| `/voz` | Liga ou desliga a voz |
| `sair` | Encerra o programa |

Os itens salvos com `/lembrar` passam a valer na próxima vez que o Jarvis for ligado.

## ⚙️ Configuração

No arquivo `config.py` você pode ajustar:

- `MODELO`: o nome do modelo do Gemini. Os nomes mudam com o tempo, então se aparecer erro de "modelo não encontrado", confira a lista atual no AI Studio.
- `SISTEMA`: a personalidade e as regras do Jarvis.

## 🗺️ Próximos passos

- [ ] Busca na internet para responder sobre assuntos recentes
- [ ] Entrada por voz (microfone)
- [ ] Palavra de ativação ("Jarvis")
- [ ] Ferramentas: abrir sites, ler arquivos do projeto, criar lembretes
- [ ] Interface gráfica ou web

## 📄 Licença

Distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👤 Autor

**Uelisson Barreto**, estudante de Análise e Desenvolvimento de Sistemas.
GitHub: [@Uelisson-Barreto-Dev](https://github.com/Uelisson-Barreto-Dev)