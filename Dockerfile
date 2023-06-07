# Define a imagem base
FROM python:3.10

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos de configuração do projeto para o diretório de trabalho
COPY . /app

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta do aplicativo
EXPOSE 5000

# Define o comando para iniciar o aplicativo
CMD ["python", "app.py"]
