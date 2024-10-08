# Adicionando loguru para utilizar como log da minha aplicação

# Serve para debugar o código também
# Qualquer refatoração trocando um print por um log

# from loguru import logger
# from sys import stderr
# from functools import wraps

# # logger.add(
# #                 sink=stderr,
# #                 format="{time} <r>{level}</r> <g>{message}</g> {file}",
# #                 level="INFO"
# #             )

# # Configuração do logger para arquivo de log
# logger.add(
#                 "meu_arquivo_de_logs.log",
#                 format="{time} {level} {message} {file}",
#                 level="CRITICAL"
#             )
# logger.add(
#                 "meu_arquivo_de_logs.log",
#                 format="{time} {level} {message} {file}",
#                 level="INFO"
#             )

# Importando função de decorador
from utils_log import log_decorator
from time_decorator import time_measure_decorator
import time

@time_measure_decorator
# @log_decorator
def soma(x, y):
    # logger.info(x)
    # logger.info(y)
    # logger.info(x + y)
    time.sleep(2)
    return x + y
    
soma(2,3)
soma(2,3)