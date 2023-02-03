import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the model from the file
multiNB = joblib.load('multiNB.pkl')
onehot_enc = joblib.load('onehot_encoder.pkl')


@st.cache
# Define a função principal de predição que recebe valores e faz a previsão
def pred_maturidade(Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10): 
    
    if Q1 == 'Sim': 
        Ix = 'S'
    if Q1 == 'Não':
        Ix = 'N'
    
    if Q2 == 'Sim':
        I2 = 'S'
    if Q2 == 'Não':
        I2 = 'N'
    
    if Q3 == 'Sim':
        I3 = 'S'
    if Q3 == 'Não':
        I3 = 'N'
    
    if Q4 == 'Sim':
        I4 = 'S'
    if Q4 == 'Não':
        I4 = 'N'
    
    if Q5 == 'Sim':
        I5 = 'S'
    if Q5 == 'Não':
        I5 = 'N'
    
    if Q6 == 'Sim':
        I6 = 'S'
    if Q6 == 'Não':
        I6 = 'N'
    
    if Q7 == 'Sim':
        I7 = 'S'
    if Q7 == 'Não':
        I7 = 'N'
    
    if Q8 == 'Sim':
        I8 = 'S'
    if Q8 == 'Não':
        I8 = 'N'
    
    if Q9 == 'Sim':
        I9 = 'S'
    if Q9 == 'Não':
        I9 = 'N'
    
    if Q10 == 'Sim':
        I10 = 'S'
    if Q10 == 'Não':
        I10 = 'N'
    
    # prep dados de input como df
    x_user = [[Ix, I2, I3, I4, I5, I6, I7, I8, I9, I10]]
    colunas = ['i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9', 'i10']
    df_x_user = pd.DataFrame(x_user, columns = colunas)
    
    # é necessario encodar os dados passados pelos usuários, o modelos foi treinado com dados encodados
    # usar o enconde já criado anteriormente e importado
    df_x_user_enc = onehot_enc.transform(df_x_user)
    # realiza a previsão com o modelo importado
    maturidade = multiNB.predict(df_x_user_enc)
 
    if maturidade == 0: # MMCTI <= 33
        conceito ='MATURIDADE DE MELHORIA CONTÍNUA BAIXA. Processo sem elementos condicionantes em sua totalidade, distante da comprovação da realização da melhoria contínua, possui deficiencias na garantia de controle operacional. A existência de elementos garantidores sem a presença dos condicionantes demonstra que os elementos garantidores não são efetivos em sua totalidade.'

    if maturidade == 1: # MMCTI >= 34 and MMCTI <= 73:
        conceito= 'MATURIDADE DE MELHORIA CONTÍNUA MÉDIA. Processo com elementos condicionantes presentes, base para a implantação de práticas de melhoria contínua, existe controle operacional, mas ainda carece de controles de variabilidade com foco na perenidade.'

    if maturidade == 2: # MMCTI>= 74 and MMCTI <= 100:
        conceito = 'MATURIDADE DE MELHORIA CONTÍNUA ALTA. Processo com elementos condicionantes e elementos de garantidores da melhoria contínua.'
  
    return maturidade, conceito

# criação da landing page do app
st.title('METIMUR')

# Adicionar um header
st.header("Avaliação da maturidade da melhoria contínua em um processo de TI")

# Adicionar um subheader
st.subheader('Informe as caracteristicas do processo de TI que deseja avaliar a maturidade:')

# criação user inputs

# Perguntas para o usuário
# Adicionar um radio button

st.write("  ")
st.write("  ")

Q1 = st.selectbox("1 - Processo documentado e o padrão é seguido pelo time?", ("Sim", "Não"))

Q2 = st.selectbox("2 - O processo possui um indicador de resultado medido e armazenado?", ("Sim", "Não"))

Q3 = st.selectbox("3 - Existe um método de Controle do indicador do processo estabelecido e seguidos?", ("Sim", "Não"))

Q4 = st.selectbox("4 - Existe método para avaliar ou retomar a condição de estabilidade do processo (variação do desvio padrão, amplitude, tendências)?", ("Sim", "Não"))

Q5 = st.selectbox("5 - Projetos de melhoria realizados no período no processo?", ("Sim", "Não"))

Q6 = st.selectbox("6 - Análise de causa raiz de problemas feita de forma quantitativa, tendo o KPI como variavel dependente?", ("Sim", "Não"))

Q7 = st.selectbox("7 - Aumento da capacidade comprovada no processo?", ("Sim", "Não"))

Q8 = st.selectbox("8 - O CEP é utilizado para acompanhar a estabilidade dos resultados dos processos fora do projeto de melhoria?", ("Sim", "Não"))

Q9 = st.selectbox("9 - São utilizados métodos para manter a perenidade do que foi alcançado no projeto de melhoria (Plano de Controle, OCAP, FMEA)?", ("Sim", "Não"))

Q10 = st.selectbox("10 - A responsabilidade de monitorar os pontos críticos é passada formalmente para o dono do processo ao fim do projeto de melhoria?", ("Sim", "Não"))


# botão que chama a função de predição
if st.button('Predição da maturidade'):
    maturidade, conceito = pred_maturidade(Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10)
    st.success("Avaliação do processo:")  
    st.write(conceito)
    if maturidade == 0:
        st.write("detalhes maturidade baixa" )
    if maturidade == 1:
        st.write("detalhes maturidade media" )
    if maturidade == 2:
        st.write("detalhes maturidade alta" )
    

    st.write("  ")

st.write("  ")
st.write("  ")
st.write("  ")
st.write("  ")
st.write("Metimur é um produto protegido por direitos autorais. Qualquer uso não autorizado é proibido.")   