#!/usr/bin/env python3
"""
validar-lecciones.py — Valida los archivos .qmd de la carpeta lecciones/

Comprueba, para cada lección:
  1. El nombre del archivo sigue el patrón leccion-NN.qmd (NN = 2 o más dígitos)
  2. Tiene encabezado YAML con los 3 campos obligatorios: title, description, date
  3. La fecha es una fecha real en formato YYYY-MM-DD
  4. No hay dos lecciones con el mismo número

Los archivos que empiezan con "_" (como _plantilla.qmd) se ignoran, igual
que hace Quarto.

Uso:
  python3 scripts/validar-lecciones.py            # valida toda la carpeta
  python3 scripts/validar-lecciones.py ARCHIVO... # valida además esos archivos

Sale con código 0 si todo está bien, 1 si hay algún error.
"""

import re
import sys
from datetime import datetime
from pathlib import Path

CARPETA = Path("lecciones")
CAMPOS_OBLIGATORIOS = ("title", "description", "date")
PATRON_NOMBRE = re.compile(r"^leccion-(\d{2,})\.qmd$")
PATRON_FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def leer_frontmatter(ruta):
    """Devuelve (campos, error). campos es un dict campo -> valor (string)."""
    try:
        lineas = ruta.read_text(encoding="utf-8").splitlines()
    except OSError as e:
        return {}, f"no se pudo leer el archivo ({e})"

    # El encabezado debe empezar en la primera línea con ---
    if not lineas or lineas[0].strip() != "---":
        return {}, "no tiene encabezado YAML (debe empezar con --- en la línea 1)"

    cierre = None
    for i, linea in enumerate(lineas[1:], start=1):
        if linea.strip() in ("---", "..."):
            cierre = i
            break
    if cierre is None:
        return {}, "el encabezado YAML no está cerrado (falta el --- final)"

    campos = {}
    for linea in lineas[1:cierre]:
        if not linea.strip() or linea.lstrip().startswith("#"):
            continue
        # Solo nos interesan las claves de primer nivel (sin indentación)
        if linea[0].isspace() or linea.lstrip().startswith("-"):
            continue
        if ":" not in linea:
            continue
        clave, _, valor = linea.partition(":")
        campos[clave.strip()] = valor.strip().strip('"').strip("'").strip()

    return campos, None


def validar_archivo(ruta):
    """Devuelve (errores, numero_de_leccion o None)."""
    errores = []
    nombre = ruta.name

    coincidencia = PATRON_NOMBRE.match(nombre)
    numero = None
    if coincidencia:
        numero = int(coincidencia.group(1))
    else:
        errores.append(
            f"{ruta}: el nombre del archivo no sigue el patrón leccion-NN.qmd "
            f"(por ejemplo leccion-01.qmd)"
        )

    campos, error = leer_frontmatter(ruta)
    if error:
        errores.append(f"{ruta}: {error}")
        return errores, numero

    for campo in CAMPOS_OBLIGATORIOS:
        if campo not in campos:
            errores.append(f"{ruta}: falta el campo obligatorio '{campo}'")
        elif not campos[campo]:
            errores.append(f"{ruta}: el campo '{campo}' está vacío")

    fecha = campos.get("date", "")
    if fecha:
        if not PATRON_FECHA.match(fecha):
            errores.append(
                f"{ruta}: el campo 'date' vale \"{fecha}\" y debe tener "
                f"formato YYYY-MM-DD (por ejemplo 2026-03-15)"
            )
        else:
            try:
                datetime.strptime(fecha, "%Y-%m-%d")
            except ValueError:
                errores.append(
                    f"{ruta}: el campo 'date' vale \"{fecha}\" y no es una "
                    f"fecha real del calendario"
                )

    return errores, numero


def main(argv):
    if not CARPETA.is_dir():
        print(f"❌ No existe la carpeta {CARPETA}/ "
              f"(ejecuta el script desde la raíz del repositorio)")
        return 1

    rutas = {p for p in CARPETA.glob("*.qmd") if not p.name.startswith("_")}
    for extra in argv:
        p = Path(extra)
        if p.name.startswith("_"):
            continue
        rutas.add(p)

    if not rutas:
        print("⚠️  No hay lecciones que validar en lecciones/")
        return 0

    errores = []
    numeros = {}
    for ruta in sorted(rutas):
        errores_archivo, numero = validar_archivo(ruta)
        errores.extend(errores_archivo)
        if numero is not None:
            numeros.setdefault(numero, []).append(str(ruta))

    for numero, archivos in sorted(numeros.items()):
        if len(archivos) > 1:
            errores.append(
                f"número de lección duplicado ({numero:02d}): "
                + ", ".join(sorted(archivos))
            )

    if errores:
        print(f"❌ Validación fallida: {len(errores)} problema(s) encontrado(s)\n")
        for e in errores:
            print(f"  • {e}")
        print(
            "\nCada lección debe empezar así:\n"
            '  ---\n'
            '  title: "Lección N: Título"\n'
            '  description: "Descripción breve"\n'
            '  date: "YYYY-MM-DD"\n'
            '  ---'
        )
        return 1

    print(f"✅ {len(rutas)} lección(es) validada(s) correctamente")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
