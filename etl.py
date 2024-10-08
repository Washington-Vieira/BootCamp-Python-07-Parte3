import pandas as pd
import os
import glob

# DEFININDO LOG
# ---------------
from utils_log import log_decorator
# ---------------

# Definindo a pasta onde os arquivos JSON estão armazenados
@log_decorator
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    # Listando todos os arquivos JSON na pasta especificada
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    
    # Lendo cada arquivo JSON e armazenando em uma lista de DataFrames
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    
    # Concatenando todos os DataFrames em um único DataFrame
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# Chamando a função e print no DataFrame consolidado
# uma funcao que transforma
@log_decorator
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:

    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

@log_decorator
def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    Parametro que vai ser ou "csv" ou "parquet" ou "os dois"
    """
    
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
        if formato == 'parquet':
            df.to_parquet("dados.parquet", index=False)
            
@log_decorator
def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
    #pasta_argumento: str = 'data'
    data_frame = extrair_dados_e_consolidar(pasta)
    #(pasta=pasta_argumento)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    #formato_de_saida: list = ["csv", "parquet"]
    carregar_dados(data_frame_calculado, formato_de_saida)

#--------------- Testar

# if __name__ == "__main__":
