import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Salários",
    layout="wide"
)

st.title("Análise de Salários - Brasil")
st.markdown("---")

# Carregamento dos dados
@st.cache_data
def load_data():
    return pd.read_csv(
        "data/monthly_salary_brazil.csv",
        on_bad_lines="skip"
    )

try:
    df = load_data()

    # Filtros (barra lateral)
    st.sidebar.title("Filtros")

    setores = sorted(df["sector"].dropna().unique())
    setor_sel = st.sidebar.multiselect(
        "Setor",
        setores,
        default=setores
    )

    df = df[df["sector"].isin(setor_sel)]

    salario_min = int(df["Month_salary"].min())
    salario_max = int(df["Month_salary"].max())

    faixa_salario = st.sidebar.slider(
        "Faixa salarial",
        salario_min,
        salario_max,
        (salario_min, salario_max)
    )

    df = df[
        (df["Month_salary"] >= faixa_salario[0]) &
        (df["Month_salary"] <= faixa_salario[1])
    ]

    # Métricas principais
    st.subheader("Resumo")

    col1, col2, col3 = st.columns(3)
    col1.metric("Registros", len(df))
    col2.metric("Salário médio", f"R$ {df['Month_salary'].mean():,.2f}")
    col3.metric("Salário mediano", f"R$ {df['Month_salary'].median():,.2f}")

    st.markdown("---")

    # Gráfico por setor
    st.subheader("Salário médio por setor")

    salario_setor = (
        df.groupby("sector")["Month_salary"]
        .mean()
        .sort_values(ascending=False)
    )

    st.bar_chart(salario_setor)

    st.markdown("---")

    # Top profissões
    st.subheader("Top 10 profissões por salário médio")

    top_jobs = (
        df.groupby("job")["Month_salary"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(top_jobs)

    st.markdown("---")

    # Tabela final
    st.subheader("Dados")

    st.dataframe(
        df[
            [
                "job",
                "sector",
                "Month_salary",
                "13_salary",
                "eventual_salary"
            ]
        ],
        use_container_width=True
    )

except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
