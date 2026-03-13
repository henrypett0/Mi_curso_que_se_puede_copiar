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

## 📝 Cómo agregar una lección

### Opción A: Con el script (desde Terminal)

```bash
./nueva-leccion.sh
```

Te pide título y descripción, crea el archivo automáticamente. Después:

```bash
git add . && git commit -m "nueva leccion" && git push
```

### Opción B: Directo desde GitHub (sin Terminal)

1. Ve a la carpeta `lecciones/` en tu repo
2. Click en **Add file** → **Create new file**
3. Nombre: `leccion-02.qmd` (usa números con cero: 01, 02, 03...)
4. Pega esto y modifica:

```yaml
---
title: "Lección 2: Nombre de la Lección"
description: "De qué trata"
date: "2026-01-15"
---

## Tu contenido aquí

Escribe en Markdown normal.
```

5. Click en **Commit changes**
6. El sitio se actualiza solo en ~2 minutos.

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

---

## 📁 Estructura del proyecto

```
tu-curso/
├── _quarto.yml           ← Nombre del curso (lo único que cambias)
├── index.qmd             ← Página de inicio
├── lecciones.qmd         ← Lista automática de lecciones (no tocar)
├── nueva-leccion.sh      ← Script para crear lecciones rápido
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

## ❓ Problemas comunes

| Problema | Solución |
|----------|----------|
| El sitio no se publica | Settings → Pages → selecciona **GitHub Actions** |
| La lección no aparece | Revisa que tenga `title`, `description` y `date` |
| Error en el deploy | Revisa que `---` estén correctos en tu `.qmd` |
| No veo los cambios | Recarga con `Cmd+Shift+R` o espera 2 minutos |

---

Hecho con [Quarto](https://quarto.org) + [GitHub Pages](https://pages.github.com)
