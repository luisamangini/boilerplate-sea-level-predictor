import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Primeiro eu leio os dados do arquivo CSV
    df = pd.read_csv("epa-sea-level.csv")

    # Faço o gráfico de dispersão com os pontos reais do nível do mar
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Crio a primeira linha de tendência usando todos os dados (de 1880 até 2050)
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    anos_todos = pd.Series(range(1880, 2051))
    previsao_todos = intercept + slope * anos_todos
    plt.plot(anos_todos, previsao_todos, color="red")

    # Agora faço outra linha de tendência, mas só com dados a partir do ano 2000
    df_2000 = df[df["Year"] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    anos_2000 = pd.Series(range(2000, 2051))
    previsao_2000 = intercept2 + slope2 * anos_2000
    plt.plot(anos_2000, previsao_2000, color="green")

    # Coloco os rótulos nos eixos e um título no gráfico
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Salvo o gráfico como imagem e retorno o objeto do gráfico
    plt.savefig('sea_level_plot.png')
    return plt.gca()
