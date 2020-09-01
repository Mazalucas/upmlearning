import pandas as pd


# Load data
table_clients = pd.read_csv("../⁨Documents⁩/⁨GitHub⁩/⁨upmlearning⁩/⁨datasets⁩/CLIENTES.csv")
table_creditos = pd.read_csv("../⁨Documents⁩/⁨GitHub⁩/⁨upmlearning⁩/⁨datasets⁩/CREDITOS.csv")

df1 = pd.DataFrame("../⁨Documents⁩/⁨GitHub⁩/⁨upmlearning⁩/⁨datasets⁩/CLIENTES.csv", columns = ['ID_CLIENTE', 'TDOC', 'NROC', 'SEXO', 'FALTA', 'FNAC', 'INGRESO_NETO', 'FECHA_ALTA_LABORAL', 'SUCURSAL', 'PROVINCIA_PER', 'COD_POSTAL_PER', 'TIPOLABORAL', 'METAL'])
df2 = pd.DataFrame("../⁨Documents⁩/⁨GitHub⁩/⁨upmlearning⁩/⁨datasets⁩/CREDITOS.csv", columns = ['ID_CLIENTE', 'TDOC', 'NDOC', 'FECHAINFORME', 'FLIQUIDACION', 'CODIGO', 'ID_CREDITO', 'MONTO', 'SUCURSAL', 'NOMBRE', 'RECIBO', 'CLASE_PLAN'])

# Display data
# .shape displays how large the resulting DataFrame is:
table_clients.shape

# .head displays first 5 columns
print(table_clients.head())


# merge
df_merge_col = pd.merge(df1, df2, on='ID_CLIENTE')

df_merge_col

#df_outer = pd.merge(df1, df2, on='id', how='outer')

#df_outer

