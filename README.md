### Utilizando as Ferramentas do GitHub para Solucionar Algoritmos em Python.


![LuizaLabs](https://github.com/user-attachments/assets/9f93c9af-ae9c-4dd4-b97a-e80191745914)


**Bootcamp Luizalabs - Back-end com Python**

---

**DESCRIÇÃO:**

Nesta prática, iremos utilizar o GitHub Copilot e GitHub Codespaces para criar e solucionar algoritmos em Python.

Veremos o poder da utilização do Copilot para nos auxiliar nos estudos e, claro, aplicá-lo para ajudar na codificação, tratamento de erros durante nossos projetos e até mesmo para ajudar na documentação de projetos.

Para completar, vamos utilizar o Codespaces, um ambiente de desenvolvimento na nuvem oferecido pelo GitHub.



---

•  **Ferramentas do GitHub para Solucionar Algoritmos em Python**

![CI - Testes Automatizados](https://github.com/Santosdevbjj/utilizaFerramentasGitHub/actions/workflows/python-tests.yml)



---

📖 **Descrição do Projeto**
Este projeto demonstra como utilizar GitHub Copilot e GitHub Codespaces para criar e solucionar algoritmos em Python. 

O objetivo é explorar o poder dessas ferramentas para acelerar o desenvolvimento, sugerir códigos eficientes, auxiliar na correção de erros e até mesmo na documentação de projetos.

---

🎯 **Objetivos**
- Utilizar o GitHub Copilot para auxiliar na solução de algoritmos em Python.  
- Explorar como a inteligência artificial pode sugerir códigos eficientes e melhorar a produtividade.  
- Documentar decisões técnicas de forma clara e organizada.  
- Utilizar o GitHub Codespaces como ambiente de desenvolvimento na nuvem.  
- Automatizar testes com GitHub Actions.  

---

📂 **Estrutura de Pastas e Arquivos**

<img width="962" height="1349" alt="Screenshot_20251113-131233" src="https://github.com/user-attachments/assets/34eada99-4984-4c6b-aaa4-bd9a33cb0466" />

    

---



📌 **Explicação dos Arquivos**

**requirements.txt**
Lista de dependências Python necessárias para rodar o projeto:
- pytest → framework de testes automatizados.  
- python-dotenv → manipulação de variáveis de ambiente (se necessário).  

---

**.devcontainer/devcontainer.json**
Configuração para rodar o projeto no GitHub Codespaces:
- Define imagem base com Python 3.11.  
- Instala extensões úteis como ms-python.python, github.copilot.  
- Executa pip install -r requirements.txt automaticamente após criar o ambiente.  

---

**src/ (código-fonte dos algoritmos)**
- **concatenar_dados.py** → Recebe dois dados e concatena em uma única string.  
- **repetir_textos.py** → Repete uma string N vezes.  
- **operacoes_matematicas.py** → Realiza operações básicas (+, -, *, /).  
- **verificarparimpar.py** → Verifica se um número é par ou ímpar.  
- **calcular_media.py** → Calcula a média de três notas.  
- **verificar_palindromo.py** → Verifica se uma palavra ou frase é palíndromo.  

---

**docs/guia_algoritmos.md**
Guia explicativo dos algoritmos, entradas/saídas e boas práticas.  
Serve como documentação complementar para estudo.  

---

**tests/ (testes automatizados)**
- **test_concatenar.py** → Testa concatenação de dados.  
- **test_repetir.py** → Testa repetição de strings.  
- **test_operacoes.py** → Testa operações matemáticas.  
- **testparimpar.py** → Testa verificação de par/ímpar.  
- **test_media.py** → Testa cálculo de média.  
- **test_palindromo.py** → Testa verificação de palíndromos.  

---

**.github/workflows/python-tests.yml**
Workflow de GitHub Actions para rodar testes automaticamente a cada push ou pull request.  


---


⚙️ **Tecnologias Utilizadas**
- Python 3.11 → Linguagem principal.  
- GitHub Copilot → Assistente de IA para sugerir e otimizar código.  
- GitHub Codespaces → Ambiente de desenvolvimento na nuvem.  
- Pytest → Framework de testes automatizados.  
- GitHub Actions → CI/CD para rodar testes automaticamente.  
- Git/GitHub → Versionamento e hospedagem do projeto.  

---

💻 **Requisitos de Hardware e Software**

**Hardware**
- Processador Dual-Core ou superior  
- Memória RAM: mínimo 4 GB (recomendado 8 GB)  
- Espaço em disco: mínimo 500 MB livres  

**Software**
- Python 3.10+ instalado (se não usar Codespaces)  
- Git instalado  
- Navegador atualizado (para acessar GitHub e Codespaces)  
- Conta no GitHub (para utilizar Copilot e Codespaces)  

---

🚀 **Como Executar o Projeto**

🔹 Localmente
1. Clone o repositório:
   `bash
   git clone https://github.com/Santosdevbjj/utilizaFerramentasGitHub.git
   cd utilizaFerramentasGitHub
   `

**2. Crie um ambiente virtual:**
   `bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   `

**3. Instale as dependências:**
   `bash
   pip install -r requirements.txt
   `

**4. Execute qualquer algoritmo:**
   `bash
   python src/concatenar_dados.py
   `

**5. Rode os testes:**
   `bash
   pytest tests/
   `

---

🔹 **No GitHub Codespaces**
1. Acesse o repositório no GitHub.  
2. Clique em Code → Codespaces → Create codespace on main.  
3. O ambiente será criado automaticamente com Python e dependências instaladas.  
4. Para rodar os algoritmos:
   `bash
   python src/concatenar_dados.py
   `
**5. Para rodar os testes:**
   `bash
   pytest tests/
   `

---

📚 **Recursos Úteis**
- Documentação GitHub Copilot  
- Guia GitHub Codespaces  
- Pytest Documentation  

---

**Autor:**
Sergio Santos 

---

**Contato:**

[![Portfólio Sérgio Santos](https://img.shields.io/badge/Portfólio-Sérgio_Santos-111827?style=for-the-badge&logo=githubpages&logoColor=00eaff)](https://santosdevbjj.github.io/portfolio/)
[![LinkedIn Sérgio Santos](https://img.shields.io/badge/LinkedIn-Sérgio_Santos-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santossergioluiz) 

---


