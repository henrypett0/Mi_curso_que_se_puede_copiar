# 📚 Plantilla de Curso con Quarto

Crea tu propio sitio web de curso en minutos. Agrega lecciones y el sitio se actualiza solo.

**No necesitas saber programar.** Solo necesitas una cuenta de GitHub.

---

## 🚀 Cómo crear tu curso (3 pasos)

### 1. Copia este repositorio

Click en el botón verde **"Use this template"** → **"Create a new repository"**

- Ponle el nombre que quieras (ej. `mi-curso-de-finanzas`)
- Márcalo como **Public**
- Click en **Create repository**

### 2. Activa GitHub Pages

En tu nuevo repo:

1. Ve a **Settings** → **Pages**
2. En "Source" selecciona **GitHub Actions**

> ⚠️ **Este paso es obligatorio.** Sin esto el sitio no se publica.

### 3. Personaliza el nombre de tu curso

Edita el archivo `_quarto.yml` (puedes hacerlo directo en GitHub):

```yaml
website:
  title: "Nombre de Tu Curso"    ← Cambia esto
```

Haz commit y espera ~2 minutos. Tu sitio estará en:

```
https://TU_USUARIO.github.io/TU_REPO/
```

---

## 📝 Cómo subir una lección, paso a paso

Hay dos caminos. **Elige uno**, hacen lo mismo.

| | Opción A: Terminal | Opción B: GitHub en el navegador |
|---|---|---|
| Necesitas | Tener el repo en tu computadora | Solo el navegador |
| Ventaja | Detecta errores **antes** de subir | No instalas nada |

---

### Opción A: Con el script (desde la Terminal)

**Paso 1.** Abre la Terminal y entra a la carpeta de tu curso:

```bash
cd ruta/a/tu-curso
```

**Paso 2.** Corre el script:

```bash
./nueva-leccion.sh
```

**Paso 3.** Te va a preguntar dos cosas. Escribe y presiona Enter en cada una:

```
📝 Nueva lección #02
========================

Título: Variables en R
Descripción breve: Cómo declarar y usar variables
```

El script elige el número solo (si ya tienes la 01, crea la 02) y pone la fecha de hoy.

**Paso 4.** Revisa el resultado. Si todo está bien verás:

```
✅ Creada: lecciones/leccion-02.qmd

🔍 Validando lecciones...

✅ 2 lección(es) validada(s) correctamente
```

Si en vez de eso ves un ❌, **no subas nada todavía**: ve a
[Guía de errores](#-guía-de-errores-y-cómo-arreglarlos) y arréglalo primero.

**Paso 5.** Escribe tu contenido. Abre `lecciones/leccion-02.qmd` en tu editor y
reemplaza el texto de ejemplo. **No borres el encabezado de arriba** (lo que está
entre `---`).

**Paso 6.** Súbelo:

```bash
git add . && git commit -m "agregar leccion 02" && git push
```

**Paso 7.** Espera ~2 minutos y recarga tu sitio. La lección ya aparece en la
página **Lecciones**.

---

### Opción B: Directo desde GitHub (sin Terminal)

**Paso 1.** Entra a tu repositorio en GitHub y abre la carpeta `lecciones/`.

**Paso 2.** Click en **Add file** → **Create new file**.

**Paso 3.** En el nombre escribe `leccion-02.qmd`.

> Usa el **siguiente número** que te toque, siempre con dos dígitos:
> `leccion-01.qmd`, `leccion-02.qmd`, … `leccion-10.qmd`.
> Y no repitas un número que ya exista.

**Paso 4.** Pega esto en el cuadro de texto y cambia lo que está en mayúsculas:

```markdown
---
title: "Lección 2: NOMBRE DE LA LECCIÓN"
description: "DE QUÉ TRATA EN UNA LÍNEA"
date: "2026-01-15"
---

## Tu contenido aquí

Escribe en Markdown normal.
```

> La fecha va en formato **año-mes-día**: `2026-01-15`. No uses `15/01/2026`.

**Paso 5.** Baja hasta el final y click en **Commit changes** → **Commit changes**.

**Paso 6.** Ve a la pestaña **Actions** de tu repo. Vas a ver tu cambio corriendo:

- 🟡 Círculo amarillo = está trabajando, espera
- ✅ Palomita verde = listo, tu lección ya está publicada
- ❌ Tache rojo = algo está mal en tu lección; el sitio **no** se actualizó

**Paso 7.** Si salió ❌, click en el run rojo → click en el job **Validar lecciones**.
Ahí aparece el mensaje exacto de qué archivo y qué campo falla. Búscalo en
[Guía de errores](#-guía-de-errores-y-cómo-arreglarlos), corrígelo y vuelve a hacer commit.

---

## ✅ Reglas para que funcione

Cada lección necesita **3 cosas** en el encabezado:

| Campo | Ejemplo | Obligatorio |
|-------|---------|:-----------:|
| `title` | `"Lección 1: Intro"` | ✅ |
| `description` | `"Primera lección"` | ✅ |
| `date` | `"2026-01-15"` | ✅ |

El encabezado va entre `---`:

```yaml
---
title: "..."
description: "..."
date: "YYYY-MM-DD"
---
```

Además, el archivo debe llamarse `leccion-NN.qmd` (con dos dígitos: `leccion-01.qmd`,
`leccion-02.qmd`...) y no puede repetir el número de otra lección.

---

## 🔍 Validación automática

Antes de publicar el sitio, GitHub revisa todas tus lecciones. Si algo está mal,
**no publica** y te dice exactamente qué archivo y qué campo falla.

Se revisa que cada lección:

- Tenga `title`, `description` y `date`, y que no estén vacíos
- Tenga el encabezado bien abierto y cerrado con `---`
- Tenga una fecha real en formato `YYYY-MM-DD` (`2026-13-45` falla)
- Se llame `leccion-NN.qmd`, con extensión `.qmd`
- No repita el número de otra lección

Si algo falla, revisa la [Guía de errores](#-guía-de-errores-y-cómo-arreglarlos).

Puedes correr la misma revisión en tu computadora antes de hacer push:

```bash
python3 scripts/validar-lecciones.py
```

`./nueva-leccion.sh` ya la corre solo después de crear el archivo.

> Los archivos que empiezan con `_` (como `_plantilla.qmd`) se ignoran.

---

## 📁 Estructura del proyecto

```
tu-curso/
├── _quarto.yml           ← Nombre del curso (lo único que cambias)
├── index.qmd             ← Página de inicio
├── lecciones.qmd         ← Lista automática de lecciones (no tocar)
├── nueva-leccion.sh      ← Script para crear lecciones rápido
├── scripts/
│   └── validar-lecciones.py  ← Revisa que las lecciones estén bien (no tocar)
├── lecciones/
│   ├── _plantilla.qmd    ← Plantilla de referencia
│   ├── leccion-01.qmd    ← Ejemplo (puedes borrarlo)
│   └── leccion-02.qmd    ← Tus lecciones van aquí...
└── .github/workflows/
    └── deploy.yml         ← Automatización (no tocar)
```

---

## 🔧 Markdown básico

```markdown
## Título
### Subtítulo

Texto con **negrita** y *cursiva*.

- Viñeta
- Otra viñeta

1. Paso uno
2. Paso dos

[Un enlace](https://ejemplo.com)
```

Bloques de código:

````markdown
```python
print("Hola")
```

```r
library(tidyverse)
```
````

---

## 🚑 Guía de errores y cómo arreglarlos

Cuando la validación falla, verás una lista así:

```
❌ Validación fallida: 2 problema(s) encontrado(s)

  • lecciones/leccion-02.qmd: falta el campo obligatorio 'description'
  • lecciones/leccion-04.qmd: el campo 'date' vale "15/03/2026" y debe tener formato YYYY-MM-DD
```

Cada línea te dice **qué archivo** y **qué está mal**. Búscala aquí abajo.

---

### ❌ `falta el campo obligatorio 'description'`

**Qué pasó:** al encabezado le falta una de las 3 líneas obligatorias
(puede decir `title`, `description` o `date`).

**Mal** ❌
```yaml
---
title: "Lección 2: Variables"
date: "2026-01-15"
---
```

**Bien** ✅
```yaml
---
title: "Lección 2: Variables"
description: "Cómo declarar variables"
date: "2026-01-15"
---
```

---

### ❌ `el campo 'description' está vacío`

**Qué pasó:** la línea existe pero no tiene texto después de los dos puntos.

**Mal** ❌ → `description: ""`
**Bien** ✅ → `description: "Cómo declarar variables"`

---

### ❌ `el campo 'date' ... debe tener formato YYYY-MM-DD`

**Qué pasó:** escribiste la fecha en otro orden o con otros separadores.
Siempre es **año-mes-día** separado por guiones.

| Mal ❌ | Bien ✅ |
|--------|---------|
| `"15/03/2026"` | `"2026-03-15"` |
| `"15-03-2026"` | `"2026-03-15"` |
| `"2026/03/15"` | `"2026-03-15"` |
| `"marzo 15, 2026"` | `"2026-03-15"` |
| `"2026-3-5"` | `"2026-03-05"` |

---

### ❌ `el campo 'date' ... no es una fecha real del calendario`

**Qué pasó:** el formato está bien pero la fecha no existe. Pasa con
el mes 13, el día 45, o un 30 de febrero.

**Mal** ❌ → `date: "2026-13-45"`
**Bien** ✅ → `date: "2026-01-15"`

---

### ❌ `no tiene encabezado YAML (debe empezar con --- en la línea 1)`

**Qué pasó:** el archivo no empieza con `---`, casi siempre porque dejaste una
línea en blanco arriba.

**Mal** ❌
```markdown

---
title: "Lección 2"
```

**Bien** ✅ — el primer `---` va **pegado hasta arriba**, sin nada antes:
```markdown
---
title: "Lección 2"
```

---

### ❌ `la primera línea tiene espacios antes o después de los ---`

**Qué pasó:** hay un espacio invisible junto a los guiones (` ---`). Se ve casi
igual, pero rompe el encabezado.

**Solución:** borra la línea completa y escríbela de nuevo: tres guiones, nada más.

---

### ❌ `el encabezado YAML no está cerrado (falta el --- final)`

**Qué pasó:** pusiste el `---` de arriba pero no el de abajo. Van **dos**.

**Mal** ❌
```markdown
---
title: "Lección 2: Variables"
description: "Cómo declarar variables"
date: "2026-01-15"

## Mi contenido
```

**Bien** ✅
```markdown
---
title: "Lección 2: Variables"
description: "Cómo declarar variables"
date: "2026-01-15"
---

## Mi contenido
```

---

### ❌ `el nombre del archivo no sigue el patrón leccion-NN.qmd`

**Qué pasó:** el nombre del archivo no es el esperado. Debe ser la palabra
`leccion`, un guion, dos dígitos, y `.qmd`.

| Mal ❌ | Por qué | Bien ✅ |
|--------|---------|---------|
| `leccion2.qmd` | falta el guion | `leccion-02.qmd` |
| `leccion-2.qmd` | falta el cero | `leccion-02.qmd` |
| `Leccion-02.qmd` | mayúscula | `leccion-02.qmd` |
| `lección-02.qmd` | lleva acento | `leccion-02.qmd` |
| `leccion-02-variables.qmd` | texto de más | `leccion-02.qmd` |

> En GitHub no puedes renombrar con un click: abre el archivo → ícono del lápiz
> ✏️ → cambia el nombre hasta arriba → **Commit changes**.

---

### ❌ `la extensión debe ser .qmd, no .md`

**Qué pasó:** guardaste la lección como `.md` (o `.txt`, `.Rmd`). Quarto solo
publica archivos `.qmd`, así que la lección no aparecería en el sitio.

**Solución:** renombra el archivo a `leccion-NN.qmd`. El contenido no cambia.

---

### ❌ `número de lección duplicado (02)`

**Qué pasó:** dos archivos usan el mismo número. Suele pasar al duplicar una
lección para reusarla, o al crear una desde GitHub sin ver que ya existía.

El mensaje te dice **cuáles dos archivos** son. Renombra uno al siguiente número
libre, o bórralo si era una copia que no querías.

> Ojo: `leccion-02.qmd` y `leccion-002.qmd` cuentan como el mismo número 2.

---

## ❓ Otros problemas

| Problema | Solución |
|----------|----------|
| El sitio no se publica | Settings → Pages → selecciona **GitHub Actions** |
| Salió ❌ en Actions | Abre el run → job **Validar lecciones** → busca el mensaje en la guía de arriba |
| La lección no aparece pero todo salió verde | Revisa que el archivo esté dentro de `lecciones/` y termine en `.qmd` |
| Mi lección no aparece y empieza con `_` | Los archivos con `_` se ignoran a propósito. Quítale el `_` |
| El orden de las lecciones está raro | La lista se ordena por `date`. Revisa las fechas |
| No veo los cambios | Recarga con `Cmd+Shift+R` o espera 2 minutos |
| `./nueva-leccion.sh: Permission denied` | Corre `chmod +x nueva-leccion.sh` una vez |

---

Hecho con [Quarto](https://quarto.org) + [GitHub Pages](https://pages.github.com)
