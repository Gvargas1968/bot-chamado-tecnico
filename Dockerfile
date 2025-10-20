FROM python:3.11

# Instalar bibliotecas nativas necessárias
# Instala pacotes de sistema
RUN apt-get update && apt-get install -y \
    libzbar0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala pacotes Python via pip
#RUN pip install \
   # python-telegram-bot==13.15 \    mysql-connector-python \    streamlit \    pandas \    requests





#Diretório de trabalho
WORKDIR /bot

# Copiar e instalar dependências Python
COPY requirements.txt .
RUN pip install -r requirements.txt

#Copiar código do bot
COPY . .

# Comando para rodar o bot

CMD ["python", "ChamadosMysql.py"]



