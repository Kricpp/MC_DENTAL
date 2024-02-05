
from datos import (
    insertar_atencion,
    obtener_atenciones_paciente,
    obtener_pacientes,
    obtener_diagnosticos,
    obtener_tipos_tratamientos,
    insertar_paciente,
    obtener_historial_atenciones

)

def validar_datos_atencion(datos_atencion):
    # Validación de datos de atención
    if not datos_atencion.get('paciente_id'):
        raise ValueError("Se requiere un ID de paciente para registrar la atención.")
    
    if not datos_atencion.get('diagnostico_id'):
        raise ValueError("Se requiere un diagnóstico para registrar la atención.")
    
    if not datos_atencion.get('tipo_tratamiento_id'):
        raise ValueError("Se requiere un tipo de tratamiento para registrar la atención.")
    

    if not isinstance(datos_atencion.get('monto'), (int, float)) or datos_atencion.get('monto') <= 0:
        raise ValueError("El monto debe ser un número real positivo.")

    if not datos_atencion.get('fecha_atencion'):
        raise ValueError("La fecha de atención es obligatoria.")

    # Validar que no haya registros duplicados para la misma atención
    atenciones_previas = obtener_atenciones_paciente(datos_atencion['paciente_id'])
    for atencion_previa in atenciones_previas:
        if (
            atencion_previa[1] == datos_atencion['paciente_id']
            and atencion_previa[2] == datos_atencion['diagnostico_id']
            and atencion_previa[3] == datos_atencion['tipo_tratamiento_id']
            and atencion_previa[4] == datos_atencion['servicio_realizado']
            and atencion_previa[5] == datos_atencion['monto']
            and atencion_previa[0] == datos_atencion['fecha_atencion'].strftime("%Y-%m-%d")
            


        ):
            raise ValueError("Ya existe un registro para la misma atención.")

def registrar_atencion(datos_atencion):
    try:
        validar_datos_atencion(datos_atencion)
        # Si la validación es exitosa, proceder a registrar la atención
        insertar_atencion(
            datos_atencion['paciente_id'],
            datos_atencion['diagnostico_id'],
            datos_atencion['tipo_tratamiento_id'],
            datos_atencion['servicio_realizado'],
            datos_atencion['monto'],
            datos_atencion['fecha_atencion']
        )
        return "Atención registrada con éxito."
    except ValueError as e:
        # Si hay errores de validación, devolver el mensaje de error
        return str(e)

def obtener_paciente(nombre):
    # Esta función devuelve una lista de pacientes que coinciden con el nombre proporcionado.
    return obtener_pacientes(nombre)

def registrar_nuevo_paciente(nombre, direccion, telefono):
    return insertar_paciente(nombre, direccion, telefono)

def obtener_diagnostico():
    # Esta función devuelve una lista de diagnósticos disponibles.
    return obtener_diagnosticos()

def obtener_tipos_tratamiento():
    # Esta función devuelve una lista de tipos de tratamiento disponibles.
    return obtener_tipos_tratamientos()

def obtener_historial_atencion():
    return obtener_historial_atenciones()