# # Trabalho: Python + Cloud + GitHub
# Disciplina: Cloud Computing

# 🎯 Objetivos
Consolidar o aprendizado de Python com APIs, JSON e Flask

Compreender a relação entre Python e Cloud Computing

Praticar versionamento com Git e GitHub

Desenvolver autonomia na documentação de projetos

Simular colaboração com Git clone/pull em múltiplos ambientes

# 📂 Estrutura do Projeto

python-cloud-trabalho/
├── README.md
├── github_api.py
├── clima_api.py
├── alunos_json.py
├── flask_api.py
└── alunos.json
 requirements.txt
# 📝 Scripts Desenvolvidos
# 1) github_api.py
Consulta a API do GitHub e retorna informações de repositórios.

# 📌 Exemplo de execução:


python github_api.py
# 💻 Saída:


Nome: requests
Descrição: A simple, yet elegant, HTTP library.
Stars: 52.341

# 2) clima_api.py
Consulta API de clima (Open-Meteo) para Curitiba e Hanoi.

# 📌 Exemplo de execução:

python clima_api.py

# 💻 Saída:

Clima em Curitiba: Temperatura: 18 °C Vento: 3 km/h
Clima em Hanoi: Temperatura: 22 °C Vento: 2 km/h

# 3) alunos_json.py

Manipula arquivo JSON com dados de alunos.

# 📌 Exemplo de execução:

python alunos_json.py

# 💻 Saída:

Alunos cadastrados: 
- João, 20 anos
- Maria, 22 anos

# 4) flask_api.py

API em Flask com múltiplas rotas.

#  📌 Executar o servidor:

python flask_api.py

# 🌐 Endpoints disponíveis:

GET / - Mensagem de boas-vindas

GET /alunos - Lista todos os alunos

GET /saudacao/<nome> - Saudação personalizada

GET /curso/<curso> - Filtra por curso

# ⚙️ Configuração e Instalação
Instalar dependências:

pip install -r requirements.txt
Arquivo requirements.txt:

requests==2.31.0
flask==2.3.3

# 🚀 Como Executar o Projeto
# 1. Clonar o repositório:

git clone https://github.com/zer0tres/python-cloud-trabalho.git
cd python-cloud-trabalho

# 2. Executar scripts individualmente:

# API GitHub
python github_api.py

# API Clima
python clima_api.py

# Manipulação JSON
python alunos_json.py

# API Flask (servidor)
python flask_api.py

# 🔄 Testes de Git Pull/Clone
Simulação de colaboração em outra máquina:

# Clonar repositório
git clone https://github.com/zer0tres/python-cloud-trabalho.git projeto-teste

# Navegar para a pasta
cd projeto-teste

# Executar scripts (provar que funcionam)
python alunos_json.py
python clima_api.py

# Testar atualizações com git pull

git pull

Resultado esperado:

# ✅ Clone bem-sucedido

# ✅ Scripts executando corretamente

# ✅ Atualizações sendo puxadas via git pull

# 📊 Fluxo de Trabalho Git

git add .                          # Adiciona arquivos
git commit -m "mensagem"          # Salva versão
git push origin main              # Envia para GitHub
git pull                         # Atualiza local
git clone <URL>                  # Clona repositório

## 👨‍💻 Autor
# João Vinicius Batista dos Santos

# Curso: Análise e Desenvolvimento de Sistemas (ADS)

# Data: Setembro/2025
