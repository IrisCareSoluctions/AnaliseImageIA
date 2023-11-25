# Analise_Image_IA

# IrisCare Soluctions

    O IrisCare é um aplicativo móvel desenvolvido para a prevenção e controle do Retinoblastoma, uma forma de câncer ocular, 
    por meio da análise de imagem, controle periódico e encaminhamento para a Secretaria Municipal e GRAACC.


<img align="center" src="https://github.com/IrisCareSoluctions/HybridMobile/blob/main/assets/evidencia4.png" />

----
# <span style="color: #63C71F;">Pitch</span>

[Assista ao video Pitch](https://youtu.be/0_QOPCaIbMc)

----

# <span style="color: #63C71F;">Demonstração WebApp da Azure </span>

[Assista ao video do back-end integrado rodando](https://www.youtube.com/watch?v=kX0do_P3T9E)

---

# Desenvolvedores:

    -> RM: 93915 -  JAELSON DOS SANTOS

    -> RM: 94311 - MARCOS BILOBRAM

    -> RM: 96320 - NATHÁLIA MAIA

    -> RM: 94972 - RAFAELA DA SILVA

    -> RM: 93613 - VINICIUS DE OLIVEIRA



<div align="center"> 
    <a href="https://github.com/JaelsonJonas">
        <img align="center" height="100" width="100" style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/101295166?v=4" />
    </a>
    <a href="https://github.com/marcosbilobram">
        <img align="center" height="100" width="100" style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/92834827?v=4" />
    </a>
    <a href="https://github.com/natmaia">
        <img align="center" height="100" width="100" style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/105464103?s=96&v=4" />
    </a>
    <a href="https://github.com/gsrafaela">
        <img align="center" height="100" width="100" style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/99452621?v=4" />
    </a>
    <a href="https://github.com/ViniOlr">
        <img align="center" height="100" width="100" style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/81593244?v=4" />
    </a>
</div>


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
