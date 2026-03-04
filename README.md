#  Dashboard de Análise de Salários 

Projeto de **análise de dados** desenvolvido em Python, que transforma uma base pública de salários mensais no Brasil em um **dashboard interativo**, permitindo explorar e visualizar informações de forma clara e dinâmica.

---

##  Objetivo do Projeto

- Analisar dados salariais do Brasil  
- Explorar informações por setor, profissão e faixa salarial  
- Transformar dados brutos em informações visuais e compreensíveis  
- Praticar análise de dados e criação de dashboards

---

##  Funcionalidades

- **Filtros interativos**
  - Seleção de setores econômicos
  - Ajuste de faixa salarial por slider

- **Métricas dinâmicas**
  - Total de registros
  - Salário médio
  - Salário mediano

- **Visualizações gráficas**
  - Média salarial por setor econômico
  - Top 10 profissões com maiores médias salariais

- **Exploração de dados**
  - Tabela interativa com salários base, 13º e ganhos adicionais

- **Otimização**
  - Cache de dados para carregamento mais rápido do arquivo CSV

---

##  Tecnologias Utilizadas

- **Python**
- **Streamlit**
- **Pandas**
- **CSV (base de dados pública)**

---

##  Estrutura do Projeto
- data/
- monthly_salary_brazil.csv
- app.py
- README.md
- requirements.txt

  ---

##  Como Executar o Projeto

1. Certifique-se de ter o **Python** instalado  
2. Instale as dependências:
   ```bash
   pip install streamlit pandas
   streamlit run app.py
