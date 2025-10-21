------

# 🤖 Bot de Chamados Técnico

Um bot de Telegram desenvolvido em Python para registrar e gerenciar chamados de suporte técnico com integração ao banco de dados MySQL.

------

## 📋 Descrição

Este projeto implementa um bot interativo no Telegram que permite aos usuários registrar chamados de suporte técnico. O bot coleta dados como setor, localização, tipo de equipamento e descrição do problema, armazenando tudo em uma base MySQL. Administradores podem resolver chamados e notificar os usuários sobre as soluções aplicadas.

------

## ✨ Funcionalidades

- Registro de chamados via conversa interativa no Telegram
- Seleção de setor, ala, localidade e tipo de equipamento
- Armazenamento em banco de dados MySQL
- Resolução de chamados com autenticação de administrador
- Notificação automática ao técnico responsável
- Notificação ao usuário após resolução
- Identificação única para cada chamado
- Comandos integrados ao Telegram

------

## 🛠 Tecnologias Utilizadas

- Python 3.11+
- python-telegram-bot
- MySQL
- mysql-connector-python
- python-dotenv
- Docker
- pytz

------

## 🚀 Instalação

### Pré-requisitos

- Python 3.11 ou superior
- MySQL Server
- Conta de bot no Telegram (via @BotFather)

### Passo a Passo

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd bot-de-chamados
   ```

2. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados MySQL:

   - Crie o banco com o nome especificado
   - Verifique as credenciais de acesso

5. Configure as variáveis de ambiente:

   - Crie um arquivo `.env` na raiz do projeto com base no `example.env`
   - Preencha com os dados abaixo:

   ```env
   TELEGRAM_TOKEN=seu_token_do_bot_aqui
   MYSQL_HOST=seu_host_mysql_aqui
   MYSQL_USER=seu_usuario_mysql_aqui
   MYSQL_PASSWORD=sua_senha_mysql_aqui
   MYSQL_DATABASE=nome_do_banco_de_dados_aqui
   ADMIN_PASSWORD=senha_para_acesso_administrativo
   TECNICO_RESPONSAVEL_ID=id_do_usuario_telegram_do_tecnico
   ID_TECNICO_REDE=id_tecnico_rede_aqui
   ID_TECNICO_HARDWARE=id_tecnico_hardware_aqui
   ID_TECNICO_SOFTWARE=id_tecnico_software_aqui
   ID_TECNICO_IMPRESSORA=id_tecnico_impressora_aqui
   ```

6. Certifique-se de que `.env` está listado no `.gitignore`.

------

## 📌 Uso

### Execução Local

```bash
python ChamadosMysql.py
```

### Docker

1. Construa a imagem:

   ```bash
   docker build -t bot-chamados .
   ```

2. Execute o container:

   ```bash
   docker run -d bot-chamados
   ```

------

## 🤖 Comandos Disponíveis

- `/start` – Mensagem de boas-vindas
- `/chamado` – Inicia registro de chamado
- `/solucao` – Permite resolver chamado (requer senha)
- `/cancelar` – Cancela operação atual

------

## 📊 Fluxo de Registro de Chamado

1. Setor (teclado inline)
2. Ala (teclado inline)
3. Localidade (teclado inline)
4. Patrimônio (texto)
5. Tipo de equipamento (teclado inline)
6. Descrição do problema (texto)

------

## 🔐 Resolução de Chamados

1. Autenticação com senha de administrador
2. Informar ID do chamado
3. Verificar existência
4. Informar solução
5. Atualizar status para "Fechado" e notificar usuário

------

## 🗄️ Estrutura do Banco de Dados

Tabela `chamados` com os campos:

- `id`
- `data_hora`
- `nome`
- `user_id`
- `setor`
- `ala`
- `localidade`
- `patrimonio`
- `tipo`
- `descricao`
- `status`
- `solucao`

------

## 🚨 Segurança

- Use senhas fortes
- Não compartilhe o token do bot
- Configure permissões do banco corretamente
- Use variáveis de ambiente para credenciais
- Mantenha `.env` fora do controle de versão

------

## 🤝 Contribuindo

1. Faça um fork
2. Crie uma branch: `git checkout -b minha-feature`
3. Commit: `git commit -m 'Adiciona nova feature'`
4. Push: `git push origin minha-feature`
5. Abra um Pull Request

------

## 📄 Licença

Licenciado sob a Licença MIT – veja [LICENSE](LICENSE) para detalhes.

------

## 🐛 Reportar Bugs

Abra uma [issue](https://github.com/seu-usuario/nome-do-repositorio/issues) descrevendo o problema.

------

## 💡 Melhorias Futuras

- Upload de imagens nos chamados
- Categorização automática
- Relatórios estatísticos
- Teclados customizados
- Múltiplos níveis de permissão
- Histórico de chamados por usuário

------

