# Bot de Chamados Técnico

Um bot de Telegram desenvolvido em Python para gerenciar e registrar chamados de suporte técnico com integração a banco de dados MySQL.

## 📋 Descrição

Este projeto implementa um bot de Telegram que permite aos usuários registrar chamados de suporte técnico de forma interativa. O bot coleta informações como setor, localização, tipo de equipamento e descrição do problema, armazenando tudo em uma base de dados MySQL. O sistema também permite que administradores resolvam chamados e notifiquem os usuários sobre as soluções.

## ✨ Funcionalidades

- Registro interativo de chamados através de conversas no Telegram
- Seleção de setor, ala, localidade, tipo de equipamento e descrição do problema
- Armazenamento de chamados em banco de dados MySQL
- Sistema de resolução de chamados com autenticação de administrador
- Notificação automática ao técnico responsável por novos chamados
- Notificação ao usuário quando o chamado é resolvido
- Identificação única para cada chamado
- Integração com o sistema de comandos do Telegram

## 🛠 Tecnologias Utilizadas

- Python 3.11+
- python-telegram-bot
- MySQL
- mysql-connector-python
- python-dotenv
- Docker
- pytz (para manipulação de fuso horário)

## 🚀 Instalação

### Pré-requisitos

- Python 3.11 ou superior
- MySQL Server
- Conta de bot no Telegram (via @BotFather)

### Passo a Passo

1. Clone este repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd bot-de-chamados
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados MySQL:
   - Crie um banco de dados com o nome especificado na configuração
   - Verifique as credenciais de acesso

5. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto com base no arquivo `example.env`
   - Preencha as credenciais conforme explicado na seção abaixo

## ⚙️ Configuração

### Segurança das Credenciais

⚠️ **Importante**: Para segurança do projeto, todas as credenciais sensíveis devem ser armazenadas em variáveis de ambiente ou em um arquivo `.env` local (que não é commitado para o repositório).

### Configuração de Variáveis de Ambiente

1. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

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

2. O arquivo `config_bot_ChamadoBFF.py` carrega automaticamente essas variáveis de ambiente.

3. Certifique-se de que o arquivo `.gitignore` inclui `.env` para manter suas credenciais seguras.

## 📌 Uso

### Local

Para rodar o bot localmente:

```bash
python ChamadosMysql.py
```

### Docker

Para rodar o bot com Docker:

1. Construa a imagem:
   ```bash
   docker build -t bot-chamados .
   ```

2. Execute o container:
   ```bash
   docker run -d bot-chamados
   ```

## 🤖 Comandos Disponíveis

- `/start` - Inicia o bot e exibe mensagem de boas-vindas
- `/chamado` - Inicia o processo de registro de um novo chamado
- `/solucao` - Permite a um administrador resolver um chamado (requer senha)
- `/cancelar` - Cancela a operação atual

## 📊 Estrutura do Fluxo de Chamado

1. Setor (seleção via teclado inline)
2. Ala (seleção via teclado inline)
3. Localidade (seleção via teclado inline)
4. Patrimônio (informação textual)
5. Tipo de equipamento (seleção via teclado inline)
6. Descrição do problema (informação textual)

## 🔐 Sistema de Resolução de Chamados

O sistema de resolução de chamados segue os seguintes passos:

1. Autenticação com senha de administrador
2. Informação do ID do chamado
3. Verificação da existência do chamado
4. Informação da descrição da solução
5. Atualização do status para "Fechado" e envio de notificação ao usuário

## 🗄️ Banco de Dados

O sistema utiliza uma tabela MySQL chamada `chamados` com os seguintes campos:

- `id`: Identificador único do chamado
- `data_hora`: Data e hora do registro
- `nome`: Nome do usuário que registrou
- `user_id`: ID do usuário no Telegram
- `setor`: Setor onde ocorreu o problema
- `ala`: Ala do prédio
- `localidade`: Localização específica
- `patrimonio`: Número do patrimônio do equipamento
- `tipo`: Tipo de equipamento
- `descricao`: Descrição do problema
- `status`: Status do chamado (Aberto/Fechado)
- `solucao`: Descrição da solução aplicada

## 🚨 Segurança

- Use senhas fortes para o acesso administrativo
- Não compartilhe o token do bot
- Configure corretamente as permissões de acesso ao banco de dados
- Use variáveis de ambiente para armazenar credenciais
- Mantenha o arquivo `.env` fora do controle de versão

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature: `git checkout -b minha-feature`
3. Faça commit das suas alterações: `git commit -m 'Adiciona nova feature'`
4. Faça push para a branch: `git push origin minha-feature`
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

[Seu Nome ou Nome da Organização]

## 🐛 Reportar Bugs

Se encontrar algum problema, abra uma [issue](https://github.com/seu-usuario/nome-do-repositorio/issues) no GitHub descrevendo o problema encontrado.

## 💡 Melhorias Futuras

- Adicionar sistema de upload de imagens para os chamados
- Implementar categorização automática de chamados
- Adicionar sistema de relatórios estatísticos
- Melhorar interface com teclados customizados
- Adicionar suporte a múltiplos níveis de permissão
- Implementar histórico de chamados por usuário

## 📋 Descrição

Este projeto implementa um bot de Telegram que permite aos usuários registrar chamados de suporte técnico de forma interativa. O bot coleta informações como setor, localização, tipo de equipamento e descrição do problema, armazenando tudo em uma base de dados MySQL. O sistema também permite que administradores resolvam chamados e notifiquem os usuários sobre as soluções.

## ✨ Funcionalidades

- Registro interativo de chamados através de conversas no Telegram
- Seleção de setor, ala, localidade, tipo de equipamento e descrição do problema
- Armazenamento de chamados em banco de dados MySQL
- Sistema de resolução de chamados com autenticação de administrador
- Notificação automática ao técnico responsável por novos chamados
- Notificação ao usuário quando o chamado é resolvido
- Identificação única para cada chamado
- Integração com o sistema de comandos do Telegram

## 🛠 Tecnologias Utilizadas

- Python 3.11+
- python-telegram-bot
- MySQL
- mysql-connector-python
- Docker
- pytz (para manipulação de fuso horário)

## 🚀 Instalação

### Pré-requisitos

- Python 3.11 ou superior
- MySQL Server
- Conta de bot no Telegram (via @BotFather)

### Passo a Passo

1. Clone este repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd bot-de-chamados
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados MySQL:
   - Crie um banco de dados com o nome especificado na configuração
   - Verifique as credenciais de acesso

5. Configure as variáveis de ambiente:
   - Renomeie `example.env` para `.env` (caso exista) ou crie um novo arquivo `.env`
   - Preencha as credenciais conforme explicado na seção abaixo

## ⚙️ Configuração

### Segurança das Credenciais

⚠️ **Importante**: Para segurança do projeto, todas as credenciais sensíveis devem ser armazenadas em variáveis de ambiente ou em um arquivo `.env` local (que não é commitado para o repositório).

### Configuração de Variáveis de Ambiente

1. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
TELEGRAM_TOKEN=seu_token_do_bot_aqui
MYSQL_HOST=seu_host_mysql_aqui
MYSQL_USER=seu_usuario_mysql_aqui
MYSQL_PASSWORD=sua_senha_mysql_aqui
MYSQL_DATABASE=nome_do_banco_de_dados_aqui
ADMIN_PASSWORD=senha_para_acesso_administrativo
TECNICO_RESPONSAVEL_ID=id_do_usuario_telegram_do_tecnico
```

2. O arquivo `config_bot_ChamadoBFF.py` deve ser configurado para carregar estas variáveis automaticamente. Veja o arquivo `exemplo_config_bot_ChamadoBFF.py` como referência.

3. Certifique-se de que o arquivo `.gitignore` inclui `.env` para manter suas credenciais seguras.

## 📌 Uso

### Local

Para rodar o bot localmente:

```bash
python ChamadosMysql.py
```

### Docker

Para rodar o bot com Docker:

1. Construa a imagem:
   ```bash
   docker build -t bot-chamados .
   ```

2. Execute o container:
   ```bash
   docker run -d bot-chamados
   ```

## 🤖 Comandos Disponíveis

- `/start` - Inicia o bot e exibe mensagem de boas-vindas
- `/chamado` - Inicia o processo de registro de um novo chamado
- `/solucao` - Permite a um administrador resolver um chamado (requer senha)
- `/cancelar` - Cancela a operação atual

## 📊 Estrutura do Fluxo de Chamado

1. Setor (seleção via teclado inline)
2. Ala (seleção via teclado inline)
3. Localidade (seleção via teclado inline)
4. Patrimônio (informação textual)
5. Tipo de equipamento (seleção via teclado inline)
6. Descrição do problema (informação textual)

## 🔐 Sistema de Resolução de Chamados

O sistema de resolução de chamados segue os seguintes passos:

1. Autenticação com senha de administrador
2. Informação do ID do chamado
3. Verificação da existência do chamado
4. Informação da descrição da solução
5. Atualização do status para "Fechado" e envio de notificação ao usuário

## 🗄️ Banco de Dados

O sistema utiliza uma tabela MySQL chamada `chamados` com os seguintes campos:

- `id`: Identificador único do chamado
- `data_hora`: Data e hora do registro
- `nome`: Nome do usuário que registrou
- `user_id`: ID do usuário no Telegram
- `setor`: Setor onde ocorreu o problema
- `ala`: Ala do prédio
- `localidade`: Localização específica
- `patrimonio`: Número do patrimônio do equipamento
- `tipo`: Tipo de equipamento
- `descricao`: Descrição do problema
- `status`: Status do chamado (Aberto/Fechado)
- `solucao`: Descrição da solução aplicada

## 🚨 Segurança

- Use senhas fortes para o acesso administrativo
- Não compartilhe o token do bot
- Configure corretamente as permissões de acesso ao banco de dados
- Use variáveis de ambiente para armazenar credenciais

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature: `git checkout -b minha-feature`
3. Faça commit das suas alterações: `git commit -m 'Adiciona nova feature'`
4. Faça push para a branch: `git push origin minha-feature`
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

[Seu Nome ou Nome da Organização]

## 🐛 Reportar Bugs

Se encontrar algum problema, abra uma [issue](https://github.com/seu-usuario/nome-do-repositorio/issues) no GitHub descrevendo o problema encontrado.

## 💡 Melhorias Futuras

- Adicionar sistema de upload de imagens para os chamados
- Implementar categorização automática de chamados
- Adicionar sistema de relatórios estatísticos
- Melhorar interface com teclados customizados
- Adicionar suporte a múltiplos níveis de permissão
- Implementar histórico de chamados por usuário