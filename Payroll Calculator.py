class Empleado:
    def __init__(self, nombre, salario_base, horas_trabajadas, tasa_horas_extra=1.5):
        self.nombre = nombre
        self.salario_base = salario_base
        self.horas_trabajadas = horas_trabajadas
        self.tasa_horas_extra = tasa_horas_extra

    def calcular_salario_bruto(self):
        horas_normales = 40
        if self.horas_trabajadas <= horas_normales:
            return self.salario_base
        else:
            horas_extra = self.horas_trabajadas - horas_normales
            salario_extra = horas_extra * (self.salario_base / horas_normales) * self.tasa_horas_extra
            return self.salario_base + salario_extra

    def calcular_deducciones(self, porcentaje_impuesto):
        salario_bruto = self.calcular_salario_bruto()
        return salario_bruto * (porcentaje_impuesto / 100)

    def calcular_salario_neto(self, porcentaje_impuesto):
        salario_bruto = self.calcular_salario_bruto()
        deducciones = self.calcular_deducciones(porcentaje_impuesto)
        return salario_bruto - deducciones

def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    return False

# Función para ingresar los datos
def ingresar_datos():
    nombre = input("Ingrese el nombre del empleado: ")
    salario_base = float(input("Ingrese el salario base: "))
    horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
    porcentaje_impuesto = float(input("Ingrese el porcentaje de impuesto: "))
    anio = int(input("Ingrese el año: "))

    return nombre, salario_base, horas_trabajadas, porcentaje_impuesto, anio

# Función principal para ejecutar el cálculo
def main():
    nombre, salario_base, horas_trabajadas, porcentaje_impuesto, anio = ingresar_datos()
    empleado = Empleado(nombre, salario_base, horas_trabajadas)

    if es_bisiesto(anio):
        print(f"El año {anio} es un año bisiesto.")
    else:
        print(f"El año {anio} no es un año bisiesto.")

    salario_bruto = empleado.calcular_salario_bruto()
    deducciones = empleado.calcular_deducciones(porcentaje_impuesto)
    salario_neto = empleado.calcular_salario_neto(porcentaje_impuesto)

    print(f"\n--- Resultado de la nómina ---")
    print(f"Empleado: {empleado.nombre}")
    print(f"Salario bruto: ${salario_bruto:.2f}")
    print(f"Deducciones: ${deducciones:.2f}")
    print(f"Salario neto: ${salario_neto:.2f}")

# Ejecutar el programa
if __name__ == "__main__":
    main()
