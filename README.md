# Analise_Image_IA

## Como executar a aplicação

### Métodos:

- [Convencional](#convencional)
- [Utilizando Docker](#utilizando-docker)

### Convencional

#### 1. Clonar o repositório:

```bash

git clone https://github.com/IrisCareSoluctions/AnaliseImageIA.git

```
#### 2. Acessar a pasta do projeto:

```bash

cd AnaliseImageIA

```


#### 3. Criar um ambiente virtual:

```bash

py -m venv .venv

```

#### 4. Ativar o ambiente virtual (para sistemas Windows):

```bash

source .venv/Scripts/activate

```

#### 4.1 Ativar o ambiente virtual (para sistemas Linux):

```bash

source .venv/bin/activate

```

#### 5. Instalar as dependências:

```bash

pip install -r requirements.txt

```


#### 6. Executar a aplicação:

```bash

flask run -h 0.0.0.0 -p 5000

```

Certifique-se de ter o Python e o Flask instalados em seu ambiente antes de seguir os passos acima.

### Utilizando Docker

#### 1. Construa a imagem:

```bash

docker build -t analise-imagem-ia .

```

#### 2. Inicie o container:

```bash

docker run -p 5000:5000 analise-imagem-ia

```

# Observações

A inteligência artificial criada ainda é muito limitada, luzes ou ângulos diferentes podem afetar na precisão do software, além da distância que ainda é bem sensível.
