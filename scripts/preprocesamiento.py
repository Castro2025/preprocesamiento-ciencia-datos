import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import os

def limpiar_datos(df):
    df = df.drop_duplicates()
    df = df.fillna(df.mean(numeric_only=True))
    return df

def normalizar_datos(df, columnas):
    scaler = MinMaxScaler()
    df[columnas] = scaler.fit_transform(df[columnas])
    return df

def codificar_categoricas(df, columnas):
    encoder = LabelEncoder()
    for col in columnas:
        df[col] = encoder.fit_transform(df[col])
    return df

if __name__ == "__main__":
    ruta = os.path.join("data", "ejemplo.csv")
    df = pd.read_csv(ruta)

    df = limpiar_datos(df)
    df = normalizar_datos(df, ["edad", "ingresos"])
    df = codificar_categoricas(df, ["genero", "ciudad", "nombre"])

    print(df.head())
    df.to_csv(os.path.join("data", "ejemplo_preprocesado.csv"), index=False)
    print("Archivo guardado correctamente.")
