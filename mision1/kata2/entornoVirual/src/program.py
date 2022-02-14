# Usando un paquete instalado 
# En un entorno virtual env

from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print(now)

now = now + relativedelta(months=1, weeks=1, hour=10)

print(now)

print('\n Haciendo uso de un entorno virtual en Python')