from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        total_temp = 0
        total_hum = 0
        total_pres = 0
        total_vel_viento = 0
        direccion_viento = {}

        with open(self.nombre_archivo, "r") as file:
            for line in file:
                if line.startswith("Temperatura:"):
                    total_temp += float(line.split(":")[1].strip())
                elif line.startswith("Humedad:"):
                    total_hum += float(line.split(":")[1].strip())
                elif line.startswith("Presion:"):
                    total_pres += float(line.split(":")[1].strip())
                elif line.startswith("Viento:"):
                    viento_data = line.split(":")[1].strip().split(",")
                    velocidad_viento = float(viento_data[0])
                    direccion = viento_data[1]
                    total_vel_viento += velocidad_viento
                    if direccion in direccion_viento:
                        direccion_viento[direccion] += 1
                    else:
                        direccion_viento[direccion] = 1

        num_registros = len(direccion_viento)
        promedio_temp = total_temp / num_registros
        promedio_hum = total_hum / num_registros
        promedio_pres = total_pres / num_registros
        promedio_vel_viento = total_vel_viento / num_registros

        max_direccion = max(direccion_viento, key=direccion_viento.get)

        return promedio_temp, promedio_hum, promedio_pres, promedio_vel_viento, max_direccion

archivo_ejemplo = "datos_meteorologicos.txt"
datos = DatosMeteorologicos(archivo_ejemplo)
promedio_temp, promedio_hum, promedio_pres, promedio_vel_viento, direccion_predominante = datos.procesar_datos()

print("Temperatura promedio:", promedio_temp)
print("Humedad promedio:", promedio_hum)
print("Presión promedio:", promedio_pres)
print("Velocidad promedio del viento:", promedio_vel_viento)
print("Dirección predominante del viento:", direccion_predominante)
