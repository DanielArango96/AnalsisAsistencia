import pandas as pd

dataFrameUsuarios=pd.read_excel("./data/usuarios_sistema_completo.xlsx")


#print(dataFrameUsuarios['tipo_usuario'].unique())
#print(dataFrameUsuarios['especialidad'].unique())




#1. Solo estudiantes
soloEstudiantes=dataFrameUsuarios.query('tipo_usuario == "estudiante"')
print ("#1 :", soloEstudiantes )

#2. Solo profesores
soloProfesores=dataFrameUsuarios.query('tipo_usuario == "docente"')
print ("#2 :", soloProfesores )

#3. Todos excepto estudiantes
diferenteEstudiantes=dataFrameUsuarios.query('tipo_usuario != "estudiante"')
print ("#3 :", diferenteEstudiantes )

#4. Filtrar por especialidad
filtrarPorEspecialidad=dataFrameUsuarios.query('especialidad == "Ingenieria de Sistemas"')
print ("#4 :", filtrarPorEspecialidad )



#5. Excluir una especialidad
especialidadExcluida=dataFrameUsuarios.query('especialidad != "Ingenieria Civil"')
print ("#5 :", filtrarPorEspecialidad )

#6. Excluir administrativos
diferentesAdministrativos=dataFrameUsuarios.query('tipo_usuario != "administrativo"')
print ("#6 :", diferentesAdministrativos )

#7. Direcciones en medellin
direccionesMedellin=dataFrameUsuarios[dataFrameUsuarios['direccion'].str.contains('medellin', case=False, na=False)]
print ("#7 :", direccionesMedellin )


#8. Direcciones terminadas en sur
direccionesTerminadasSur = dataFrameUsuarios[dataFrameUsuarios['direccion'].str.lower().str.endswith('sur', na=False)]
print("#8 :", direccionesTerminadasSur )

#9. Direcciones que inician con calle
direccionesIniciadasCalle=dataFrameUsuarios[dataFrameUsuarios['direccion'].str.lower().str.startswith('calle', na=False )]
print("#9 :", direccionesIniciadasCalle )

#10.Especialidades que contienen la palabra datos
especialidadesConPalabraDatos=dataFrameUsuarios[dataFrameUsuarios['especialidad'].str.contains('datos', case=False, na=False)]
print("#10 :", especialidadesConPalabraDatos )

#11. instructores en itagui
instructoresDeItagui = dataFrameUsuarios[
    (dataFrameUsuarios['tipo_usuario'] == 'docente') &
    (dataFrameUsuarios['direccion'].str.contains('itagüí', case=False, na=False))
]
print("#11 :", instructoresDeItagui )

#12. nacidos despues de 2000
nacidosEnLos2000=dataFrameUsuarios[pd.to_datetime(dataFrameUsuarios['fecha_nacimiento']) > '2000-01-01']
print("#12 :", nacidosEnLos2000 )

#13. nacidos en los 90

dataFrameUsuarios['fecha_nacimiento'] = pd.to_datetime(dataFrameUsuarios['fecha_nacimiento'], errors='coerce')

nacidosEnLos90 = dataFrameUsuarios[
    (dataFrameUsuarios['fecha_nacimiento'] >= '1990-01-01') &
    (dataFrameUsuarios['fecha_nacimiento'] <= '1999-12-31')
]

print("#13 :", nacidosEnLos90 )

#14. direcciones en envigado
direccionesEnvigado=dataFrameUsuarios[dataFrameUsuarios['direccion'].str.contains('Envigado', case=False, na=False)]
print ("#14 :", direccionesEnvigado )

#15. especialdiades que empizan por I
especialidadesInicianI=dataFrameUsuarios[dataFrameUsuarios['especialidad'].str.startswith('I', na=False)]
print ("#15 :", especialidadesInicianI )

#16. usuarios sin direccion
usuariosSinDireccion=dataFrameUsuarios[dataFrameUsuarios['direccion'].isna() | (dataFrameUsuarios['direccion'].str.strip() == '')]
print ("#16 :", usuariosSinDireccion )

#17. usuarios sin especialidad
usuariosSinEspecialidad=dataFrameUsuarios[dataFrameUsuarios['especialidad'].isna() | (dataFrameUsuarios['especialidad'].str.strip() == '')]
print ("#17 :", usuariosSinEspecialidad )


#18. profesores que viven en sabaneta
direccionesSabaneta=dataFrameUsuarios[dataFrameUsuarios['direccion'].str.contains('Envigado', case=False, na=False)]
print ("#18 :", direccionesEnvigado )

#19. aprendices que viven en bello
#estudiantesDeBello = dataFrameUsuarios[
    #(dataFrameUsuarios['tipo_usuario'] == 'estudiante') &
    #(dataFrameUsuarios['ciudad'].str.lower() == 'bello')]
#print ("#19 :", estudiantesDeBello )

#20. nacidos en el nuevo milenio
nacidosNuevoMilenio=dataFrameUsuarios[pd.to_datetime(dataFrameUsuarios['fecha_nacimiento']) >= '2000-01-01']
print ("#20 :", nacidosNuevoMilenio )



#1. total por tipo
totalPorTipo=dataFrameUsuarios.groupby('tipo_usuario').size()
print("#01 :",totalPorTipo)

#2. total por especialidad
totalPorEspecialidad=dataFrameUsuarios.groupby('especialidad').size()
print("#02 :",totalPorEspecialidad)

#3. cantidad de especialidades distintas
conteoEspecialidades=dataFrameUsuarios['especialidad'].value_counts()
print("#03 :",conteoEspecialidades)


#4. tipos de usuario por especialidad
tiposUsuariosPorEspecialidad = dataFrameUsuarios.groupby(['especialidad', 'tipo_usuario']).size().unstack(fill_value=0)
print("#04 :",tiposUsuariosPorEspecialidad)

#5. usuario mas antiguo por tipo
usuarioMasAntiguo=dataFrameUsuarios.loc[pd.to_datetime(dataFrameUsuarios['fecha_nacimiento']).groupby(dataFrameUsuarios['tipo_usuario']).idxmin()]
print("#05 :",tiposUsuariosPorEspecialidad)


#6. usuario mas joven por tipo
usuarioMasJoven=dataFrameUsuarios.loc[pd.to_datetime(dataFrameUsuarios['fecha_nacimiento']).groupby(dataFrameUsuarios['tipo_usuario']).idxmax()]
print("#06 :",tiposUsuariosPorEspecialidad)

#7. primer registro por tipo
primerRegistroPorTipo=dataFrameUsuarios.loc[pd.to_datetime(dataFrameUsuarios['fecha_registro']).groupby(dataFrameUsuarios['tipo_usuario']).idxmin()]
print("#07 :",primerRegistroPorTipo)


#8. ultimo registro por tipo

#9. combinacion tipo por especialidad
#10. el mas viejo por especialidad
#11. cuantos de cada especialidad por tipo
#12. edad promedio por tipo
#13. años de nacimeinto mas frecuente por especialidad
#14. mes de nacimiento ams frecuente por tipo
#15. UNA CONSULTA O FILTRO QUE UD PROPONGA
