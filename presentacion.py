
import datetime
from negocio import registrar_atencion, obtener_paciente, obtener_diagnostico, obtener_tipos_tratamiento,registrar_nuevo_paciente,obtener_historial_atencion


def registrar_nuevos_pacientes(nombre_paciente):
    direccion_paciente = input("Ingrese la dirección del nuevo paciente: ")
    telefono_paciente = input("Ingrese el teléfono del nuevo paciente: ")

    return registrar_nuevo_paciente(nombre_paciente, direccion_paciente, telefono_paciente)


def obtener_datos_atencion():
    # Función para obtener datos de atención del usuario
    nombre_paciente = input("Ingrese el nombre del paciente: ")

    # Obtener lista de pacientes que coinciden con el nombre ingresado
    pacientes = obtener_paciente(nombre_paciente)

    if not pacientes:
        print("No se encontraron pacientes con ese nombre.")
        nuevo_paciente = input("¿Desea registrar un nuevo paciente? (Sí/No): ").lower()
        if nuevo_paciente == 'si':
            registrar_nuevos_pacientes(nombre_paciente) 
            pacientes = obtener_paciente(nombre_paciente)
            
            
        else:

            return None

    # Mostrar lista de pacientes y permitir al usuario seleccionar uno
    print("Lista de pacientes:")
    for paciente in pacientes:
        print(f"{paciente[0]}. {paciente[1]}")

    paciente_id = input("Seleccione el ID del paciente: ")

    # Verificar que el ID ingresado sea válido
    paciente_id = int(paciente_id)
    if paciente_id not in [paciente[0] for paciente in pacientes]:
        print("ID de paciente inválido.")
        return None

    # Obtener lista de diagnósticos
    diagnosticos = obtener_diagnostico()
    if not diagnosticos:
        print("No hay diagnósticos disponibles. Registre diagnósticos antes de continuar.")
        return None

    # Mostrar lista de diagnósticos y permitir al usuario seleccionar uno
    print("Lista de diagnósticos:")
    for diagnostico in diagnosticos:
        
       print(f"{diagnostico[0]}. {diagnostico[1]}")


    diagnostico_id = input("Ingrese el ID del diagnóstico: ")

    # Verificar que el ID ingresado sea válido
    diagnostico_id = int(diagnostico_id)
    if diagnostico_id not in [diag[0] for diag in diagnosticos]:
        print("ID de diagnóstico inválido.")
        return None

    # Obtener lista de tipos de tratamiento
    tipos_tratamientos = obtener_tipos_tratamiento()
    if not tipos_tratamientos:
        print("No hay tipos de tratamiento disponibles. Registre tipos de tratamiento antes de continuar.")
        return None

    # Mostrar lista de tipos de tratamiento y permitir al usuario seleccionar uno
    print("Lista de tipos de tratamiento:")
    for tipo_tratamiento in tipos_tratamientos:
        print(f"{tipo_tratamiento[0]}. {tipo_tratamiento[1]}")

    tipo_tratamiento_id = input("Ingrese el ID del tipo de tratamiento: ")

    # Verificar que el ID ingresado sea válido
    tipo_tratamiento_id = int(tipo_tratamiento_id)
    if tipo_tratamiento_id not in [tipo_trat[0] for tipo_trat in tipos_tratamientos]:
        print("ID de tipo de tratamiento inválido.")
        return None

    servicio_realizado = input("Ingrese el servicio realizado (Especificaciones): ")
    monto = float(input("Ingrese el monto: "))
    
    # Obtener la fecha actual
    fecha_atencion = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        'paciente_id': paciente_id,
        'diagnostico_id': diagnostico_id,
        'tipo_tratamiento_id': tipo_tratamiento_id,
        'servicio_realizado': servicio_realizado,
        'monto': monto,
        'fecha_atencion': fecha_atencion
    }


opcion = input("BIENVENIDO A CLINICA SALUD DENTAL\n"
               "¿Desea ver el historial de todas las atenciones registradas? (Sí/No): ").lower()
if opcion == 'si':
    historial_todas_atenciones = obtener_historial_atencion()

    if not historial_todas_atenciones:
        print("No hay historial de atenciones registrado.")
    else:
        print("Historial de Todas las Atenciones:")
        for atencion in historial_todas_atenciones:
            print(f"Fecha: {atencion[0]}, Paciente: {atencion[1]}, Diagnóstico: {atencion[2]}, "
                  f"Tratamiento: {atencion[3]}, Servicio: {atencion[4]}, Monto: {atencion[5]}")

# Main
if __name__ == "__main__":
    # Obtener datos de atención del usuario
    datos_atencion = obtener_datos_atencion()

    if datos_atencion:
        # Registrar la atención
        resultado = registrar_atencion(datos_atencion)
        print(resultado)
