def obtener_horario(inicio, horas):
    # Convertir el inicio a hora y minuto
    h, m = map(int, inicio.split(":"))
    # Calcular la hora de finalización
    h_fin = h + horas
    if h_fin >= 24:  # En caso de que el horario pase de las 24 horas
        h_fin -= 24
    # Devolver horario en formato HH:MM
    return f"{h:02d}:{m:02d} - {h_fin:02d}:{m:02d}"

def main():
    num_empleados = int(input("Ingrese la cantidad de empleados: "))
    horas_por_dia = int(input("Ingrese las horas de trabajo por día: "))

    inicio_jornada = "11:00"  # Supongamos que la jornada comienza a las 8:00 AM

    for i in range(1, num_empleados + 1):
        horario = obtener_horario(inicio_jornada, horas_por_dia)
        print(f"Empleado {i}: {horario}")

        # Actualizar el inicio de la jornada para el próximo empleado
        h, m = map(int, inicio_jornada.split(":"))
        h += horas_por_dia
        if h >= 24:  # En caso de que el horario pase de las 24 horas
            h -= 24
        inicio_jornada = f"{h:02d}:{m:02d}"

if __name__ == "__main__":
    main()
