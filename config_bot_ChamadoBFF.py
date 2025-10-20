import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Token do bot do Telegram (obtido com @BotFather)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Configurações do MySQL
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

# Senha do administrador para resolver chamados
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

# ID do usuário do Telegram do técnico responsável
TECNICO_RESPONSAVEL_ID = int(os.getenv("TECNICO_RESPONSAVEL_ID", 0))

# IDs específicos para roteamento por categoria (opcional)
ID_TECNICO_REDE = os.getenv("ID_TECNICO_REDE")
ID_TECNICO_HARDWARE = os.getenv("ID_TECNICO_HARDWARE")
ID_TECNICO_SOFTWARE = os.getenv("ID_TECNICO_SOFTWARE")
ID_TECNICO_IMPRESSORA = os.getenv("ID_TECNICO_IMPRESSORA")