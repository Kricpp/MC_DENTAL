import datos 
datos.inicializar_base_datos()
from datos import insertar_diagnostico
from datos import insertar_tipo_tratamiento

# Insertar enfermedades dentales
insertar_diagnostico("Caries dental")
insertar_diagnostico("Gingivitis")
insertar_diagnostico("Periodontitis")
insertar_diagnostico("Maloclusión")
insertar_diagnostico("Bruxismo")



# Insertar tipos de tratamiento
insertar_tipo_tratamiento("Ortodoncia")
insertar_tipo_tratamiento("Profilaxis")
insertar_tipo_tratamiento("Endodoncia")
insertar_tipo_tratamiento("Blanqueamiento dental")
insertar_tipo_tratamiento("Extracción dental")
# Añade más tipos de tratamiento según sea necesario


