from evaluacionalumnosbachillerato.models import *
grupos = GrupoAlumnos.objects.filter(response_boolean_profesor_autoevaluacion=False)
print("Autoevaluación Desempeño Docente Sección Primaria")
for grupo in grupos:
    print(f"{grupo.profesor.nombre} materia: {grupo.profesor.materia} grupo: {grupo.grupo}")

'''
Autoevaluación Desempeño Docente Sección Primaria

ARMENUI HÉRNANDEZ GERALDINE materia: INGLÉS grupo: 5B
ARMENUI HÉRNANDEZ GERALDINE materia: INGLÉS grupo: 6A
ARMENUI HÉRNANDEZ GERALDINE materia: INGLÉS grupo: 6C
COHEN CATTAN MILLY materia: TORÁ grupo: 3B
COHEN CATTAN MILLY materia: TORÁ grupo: 3C
COHEN CATTAN MILLY materia: TORÁ grupo: 3D
PÉREZ BENITEZ JORGE  materia: ZOOMLANDER grupo: 4°
PÉREZ BENITEZ JORGE  materia: ZOOMLANDER grupo: 6°
PROFETA ESQUENAZI JENNY materia: ESPAÑOL grupo: 1A
HÉRNANDEZ VELASCO PAMELA materia: ESPAÑOL grupo: 1C
GARCÍA CARMONA MA. GUADALUPE materia: ESPAÑOL grupo: 1D
VAZQUÉZ SOSA CARLOS ERNESTO materia: ESPAÑOL grupo: 2A
MIRANDA TERÁN ALEJANDRA materia: ESPAÑOL grupo: 2B
PÉREZ LOZANO LILLIAN YAZMIN materia: ESPAÑOL grupo: 2C
CASCAJARES NICOLI MONTSERRAT materia: ESPAÑOL grupo: 2D
PÉREZ SANTACRUZ ARIADNA GUADALUPE materia: ESPAÑOL grupo: 2E
ANAYA PINEDA JUAN JOSE materia: MENTOR grupo: 1C
ANAYA PINEDA JUAN JOSE materia: MENTOR grupo: 1D
GONZALEZ ROBLES EDWIN materia: MENTOR  grupo: 2B
GONZALEZ ROBLES EDWIN materia: MENTOR  grupo: 2E
GALGANI ARANA KARLA materia: INGLÉS grupo: 1A
GALGANI ARANA KARLA materia: INGLÉS grupo: 1B
GÓMEZ CORTEZ MAGDALENA DEL CARMEN materia: INGLÉS grupo: 1D
GÓMEZ CORTEZ MAGDALENA DEL CARMEN materia: INGLÉS grupo: 2D
ESCOBAR SANDRA materia: INGLÉS grupo: 2A
ESCOBAR SANDRA materia: INGLÉS grupo: 2C
HAZAN COHEN LINDA materia: HEBREO grupo: 1A
HAZAN COHEN LINDA materia: HEBREO grupo: 1B
ABOUTBOUL DARWISH TANIA materia: HEBREO grupo: 2B
ABOUTBOUL DARWISH TANIA materia: HEBREO grupo: 2D
LANIADO MARGIE  materia: JAGUIM grupo: 1C
RUSSEK DAYAN RIVKA materia: JAGUIM grupo: 2A
RUSSEK DAYAN RIVKA materia: JAGUIM grupo: 2C
TUSSIE MIZRAHI SHARON materia: JAGUIM grupo: 2E
'''