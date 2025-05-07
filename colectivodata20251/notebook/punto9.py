import pandas as pd

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")

dataFrameAsistencia['fecha'] = pd.to_datetime(dataFrameAsistencia['fecha'], errors='coerce')


# Mostrar los meses presentes en la columna 'fecha'
print(dataFrameAsistencia['fecha'].dt.month.value_counts().sort_index())
 
estudiantesQueAsistieronJunio=dataFrameAsistencia[dataFrameAsistencia['fecha'].dt.month == 3]
print(estudiantesQueAsistieronJunio)