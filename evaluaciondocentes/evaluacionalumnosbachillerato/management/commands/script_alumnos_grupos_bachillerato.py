from evaluacionalumnosbachillerato.models import *
grupos = GrupoAlumnos.objects.filter(response_boolean_survey=False)
print("Evaluación Desempeño Docente Sección Primaria por Alumnos")
for grupo in grupos:
    print(f"{grupo.profesor.nombre} materia: {grupo.profesor.materia} grupo: {grupo.grupo}")

'''
Evaluación Desempeño Docente Sección Primaria por Alumnos

VARGAS MARTINEZ FRANCISCO LUIS materia: TALLER EN MOVIMIENTO  grupo: 5°
HÉRNANDEZ VELASCO PAMELA materia: ESPAÑOL grupo: 1C
GARCÍA CARMONA MA. GUADALUPE materia: ESPAÑOL grupo: 1D
MIRANDA TERÁN ALEJANDRA materia: ESPAÑOL grupo: 2B
PÉREZ LOZANO LILLIAN YAZMIN materia: ESPAÑOL grupo: 2C
PÉREZ SANTACRUZ ARIADNA GUADALUPE materia: ESPAÑOL grupo: 2E
ANAYA PINEDA JUAN JOSE materia: MENTOR grupo: 1C
ANAYA PINEDA JUAN JOSE materia: MENTOR grupo: 1D
GONZALEZ ROBLES EDWIN materia: MENTOR  grupo: 2B
GONZALEZ ROBLES EDWIN materia: MENTOR  grupo: 2E
GALGANI ARANA KARLA materia: INGLÉS grupo: 1A
GÓMEZ CORTEZ MAGDALENA DEL CARMEN materia: INGLÉS grupo: 1D
GÓMEZ CORTEZ MAGDALENA DEL CARMEN materia: INGLÉS grupo: 2D
ESCOBAR SANDRA materia: INGLÉS grupo: 2A
ESCOBAR SANDRA materia: INGLÉS grupo: 2C
HAZAN COHEN LINDA materia: HEBREO grupo: 1A
ABOUTBOUL DARWISH TANIA materia: HEBREO grupo: 2B
ABOUTBOUL DARWISH TANIA materia: HEBREO grupo: 2D
LANIADO MARGIE  materia: JAGUIM grupo: 1C
RUSSEK DAYAN RIVKA materia: JAGUIM grupo: 2A
TUSSIE MIZRAHI SHARON materia: JAGUIM grupo: 2E

'''