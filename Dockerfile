# Use a última versão do Python disponível
FROM python:3.12-slim

# Adicionar um usuário 'python'
RUN useradd -m python

# Instalar dependências
RUN apt-get update && apt-get install -y \
    zsh \
    git \
    curl \
    fontconfig \
    && apt-get install -y --no-install-recommends \
    fonts-dejavu \
    && rm -rf /var/lib/apt/lists/*

# Instalar Oh My Zsh
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Instalar o tema Spaceship e fontes Powerline
RUN git clone https://github.com/denysdovhan/spaceship-prompt.git /root/.oh-my-zsh/themes/spaceship-prompt \
    && ln -s /root/.oh-my-zsh/themes/spaceship-prompt/spaceship.zsh-theme /root/.oh-my-zsh/themes/spaceship.zsh-theme \
    && git clone https://github.com/powerline/fonts.git --depth=1 \
    && cd fonts \
    && ./install.sh \
    && cd .. \
    && rm -rf fonts

# Definir o diretório de trabalho
WORKDIR /app

# Instalar o pytest
RUN pip install --no-cache-dir pytest

# Copiar o código da aplicação para o diretório de trabalho
COPY . .

# Define o comando padrão para manter o contêiner em execução
CMD ["tail", "-f", "/dev/null"]
