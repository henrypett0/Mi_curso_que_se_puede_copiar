# Plantilla mínima — 3 archivos

Todo lo necesario para publicar un curso, en tres archivos. Cópialos a tu
repositorio con **Add file → Create new file**, respetando estas rutas:

| Archivo de aquí | Dónde va en tu repositorio |
|---|---|
| `_quarto.yml` | `_quarto.yml` (en la raíz) |
| `index.qmd` | `index.qmd` (en la raíz) |
| `deploy.yml` | `.github/workflows/deploy.yml` |

Después crea tus lecciones en `lecciones/leccion-01.qmd`, `leccion-02.qmd`...

## Qué hace cada uno

- **`_quarto.yml`** — el nombre de tu curso y el aspecto del sitio.
- **`index.qmd`** — la portada, que además arma sola la lista de lecciones.
- **`deploy.yml`** — la receta: revisa tus lecciones en cada subida, y publica
  el sitio cuando pulsas **Actions → Run workflow**. Trae dentro el revisor,
  así que no hay ningún archivo extra que copiar.

## Encabezado de una lección

```
---
title: "Lección 1: Introducción"
description: "De qué trata"
date: "2026-01-15"
---
```

Los tres campos son obligatorios, la fecha va en formato AAAA-MM-DD, y el
archivo debe llamarse `leccion-NN.qmd` con dos dígitos.

> Esta carpeta empieza con `_`, así que Quarto la ignora y no se publica.
