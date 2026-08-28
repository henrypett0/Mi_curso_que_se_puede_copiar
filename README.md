# 📚 Plantilla de Curso con Quarto

Crea tu propio sitio web de curso en minutos. Agrega lecciones y el sitio se actualiza solo.

**No necesitas saber programar.** Solo necesitas una cuenta de GitHub.

> 🏗️ ¿Quieres entender cómo está hecho todo esto y construirlo tú desde cero?
> Lee la [Guía desde cero](GUIA-DESDE-CERO.md). Este README es para el uso diario.

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

## 🔴 Publicación manual: el botón de encendido

**Este sitio no se publica solo.** Guardar un cambio no lo pone en internet:
se publica cuando tú pulsas el botón.

1. Pestaña **Actions**
2. Columna izquierda → **Deploy Quarto Site** ← no sirve "All workflows"
3. Botón **Run workflow** → **Run workflow**

Tarda ~1 minuto y medio.

### Qué pasa en cada caso

| Lo que haces | Valida | Publica |
|---|:---:|:---:|
| Guardas un cambio (push) | ✅ | ❌ |
| Abres un Pull Request | ✅ | ❌ |
| Pulsas **Run workflow** | ✅ | ✅ |

Así, al guardar te enteras enseguida si una lección está mal formada, pero
decides tú cuándo sale al público. Puedes escribir cinco lecciones y publicarlas
todas de una vez.

> ⚠️ **El descuido típico:** subes una lección, la ves en verde y das por hecho
> que ya está publicada. El verde solo dice que está *bien escrita*. Para que se
> vea en el sitio, hay que pulsar el botón.

**¿Prefieres que se publique solo?** En `.github/workflows/deploy.yml`, cambia
la línea `if: github.event_name == 'workflow_dispatch'` por
`if: github.event_name != 'pull_request'`.

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
├── imagenes/             ← Opcional: imágenes de tus lecciones
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

## 📊 Código de R que se ejecuta

Hay **dos formas** de poner código en una lección, y la diferencia son las llaves:

````markdown
```r          ← SIN llaves: solo muestra el código, no lo corre
x <- 2 + 2
```

```{r}        ← CON llaves: lo ejecuta y muestra el resultado
x <- 2 + 2
x
```
````

Con llaves obtienes la tabla calculada, la gráfica dibujada, el número real.
Sin llaves solo se ve el código bonito con colores.

### Si usas un paquete, decláralo

Este es el paso que se olvida. Tu computadora tiene tus paquetes instalados;
**el servidor de GitHub arranca vacío cada vez**. Si tu lección usa `ggplot2`
y no lo declaras, el deploy falla con:

```
there is no package called 'ggplot2'
```

Para arreglarlo, abre `.github/workflows/deploy.yml`, busca el paso
**Instalar paquetes de R** y agrega el paquete a la lista:

```r
install.packages(c(
  "knitr",
  "rmarkdown"
  , "ggplot2"      ← agrégalo así, con la coma al principio
))
```

`knitr` y `rmarkdown` ya vienen puestos: son los que hacen funcionar el
mecanismo, no los borres.

> Cada paquete extra suma tiempo al deploy. Pon solo los que de verdad uses.

### Ocultar el código y dejar solo el resultado

````markdown
```{r}
#| echo: false
plot(1:10)
```
````

| Opción | Qué hace |
|--------|----------|
| `#| echo: false` | Oculta el código, muestra el resultado |
| `#| eval: false` | Muestra el código pero no lo corre |
| `#| warning: false` | Esconde los avisos amarillos de R |
| `#| message: false` | Esconde los mensajes de carga de paquetes |

### Si no usas R para nada

Puedes borrar los pasos **Setup R** e **Instalar paquetes de R** de
`.github/workflows/deploy.yml`. El deploy será un par de minutos más rápido.

---

## 🧪 Código de R que el alumno ejecuta (WebR)

Hay una diferencia grande entre las dos cosas:

| | ```` ```{r} ```` | ```` ```{webr-r} ```` |
|---|---|---|
| Dónde corre R | En el servidor, al publicar | En el navegador del alumno |
| Qué ve el visitante | El resultado congelado | Un editor que puede cambiar y correr |

Para lecciones interactivas, mira [`lecciones/leccion-05.qmd`](lecciones/leccion-05.qmd)
como ejemplo. El encabezado necesita **tres líneas**:

```yaml
---
title: "Lección 5: Mi lección interactiva"
description: "..."
date: "2026-01-20"
engine: markdown      # ← obligatorio, ver abajo
filters:
  - webr
---
```

Y los bloques se escriben con `webr-r` en lugar de `r`.

> ⚠️ **No olvides `engine: markdown`.** Sin esa línea, el deploy falla con un error
> confuso sobre Jupyter (`No module named 'yaml'`). Quarto ve el lenguaje `webr-r`,
> no lo reconoce, e intenta arrancar un kernel de Python para ejecutarlo. Esa línea
> le dice que el documento no se ejecuta al construir — que es justo el caso, porque
> corre en el navegador del visitante.

**Lo que debes saber antes de usarlo:**

- La primera celda que alguien corra tarda ~1 minuto: el navegador descarga R. Las
  siguientes son instantáneas
- Solo funcionan los paquetes compilados para WebR, no todo CRAN
- La extensión vive en `_extensions/coatless/webr/` y **debe subirse al repo**
- `knitr::kable()` no está disponible; usa `data.frame` a secas para mostrar tablas

---

## 📷 Cómo poner una imagen en una lección

La línea es esta:

```markdown
![Texto que describe la imagen](diagrama.png)
```

El texto entre corchetes sale como **pie de foto** debajo de la imagen, y es lo que
leen los lectores de pantalla de personas ciegas. Si lo dejas vacío —
`![](diagrama.png)` — la imagen sale sin pie.

### Paso 1: decide dónde guardar la imagen

**Opción A — junto a la lección.** La más simple si la imagen es de una sola lección:

```
lecciones/
├── leccion-02.qmd
└── diagrama.png
```

```markdown
![Mi diagrama](diagrama.png)
```

**Opción B — en una carpeta `imagenes/`.** Mejor si vas a reusar imágenes en varias
lecciones:

```
tu-curso/
├── imagenes/
│   └── diagrama.png
└── lecciones/
    └── leccion-02.qmd
```

```markdown
![Mi diagrama](../imagenes/diagrama.png)
```

> ⚠️ Fíjate en los `../` del inicio. Significan *"sube una carpeta"*, y hacen falta
> porque tu lección vive dentro de `lecciones/`. Olvidarlos es el error #1 con
> imágenes: no falla el deploy, simplemente sale la imagen rota.

### Paso 2: sube la imagen

**Desde GitHub (sin Terminal):** entra a la carpeta → **Add file** → **Upload files**
→ arrastra la imagen → **Commit changes**.

**Desde la Terminal:** copia la imagen a la carpeta y súbela con tu lección:

```bash
git add . && git commit -m "agregar imagen" && git push
```

### Paso 3: cambia el tamaño si hace falta

```markdown
![Mi diagrama](diagrama.png){width=400}     ← 400 píxeles de ancho
![Mi diagrama](diagrama.png){width=50%}     ← la mitad del ancho de la página
```

### Reglas para que no falle

| Regla | Bien ✅ | Mal ❌ |
|-------|---------|--------|
| Sin espacios en el nombre | `diagrama-flujo.png` | `diagrama flujo.png` |
| Sin acentos ni ñ | `graficas.png` | `gráficas.png` |
| Todo en minúsculas | `foto.png` | `Foto.PNG` |
| Imágenes ligeras | ~200 KB | 5 MB de la cámara del celular |

> Las mayúsculas importan: si el archivo es `Diagrama.png` y escribes
> `![](diagrama.png)`, en tu Mac se ve bien pero **en el sitio publicado sale rota**.

Formatos que puedes usar: `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`, `.webp`.
También puedes dejar `.pdf`, `.csv`, `.xlsx` y `.json` en `lecciones/` sin que la
validación se queje.

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

### ❌ `no es una lección válida`

**Qué pasó:** hay un archivo suelto dentro de `lecciones/` que no se llama
`leccion-NN.qmd`. Quarto no lo publica, así que no serviría de nada ahí.

Pasa al subir notas, borradores o archivos de prueba a esa carpeta.

**Tienes tres salidas:**

1. Si **sí** era una lección → renómbrala a `leccion-NN.qmd`
2. Si **no** era una lección → bórrala, o muévela fuera de `lecciones/`
3. Si quieres conservarla ahí sin publicarla → ponle `_` al principio
   (`_borrador.qmd`). Los archivos con `_` se ignoran

> Las imágenes y datos que acompañan a tus lecciones (`.png`, `.jpg`, `.pdf`,
> `.csv`…) sí puedes dejarlos en la carpeta, no dan error.

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
| `No module named 'yaml'` / error de Jupyter | Tu lección usa ```` ```{webr-r} ```` y le falta `engine: markdown`. Ver [WebR](#-código-de-r-que-el-alumno-ejecuta-webr) |
| `Unable to locate an installed version of R` | Usaste ```` ```{r} ```` con llaves. Necesitas los pasos de R en el workflow. Ver [Código de R](#-código-de-r-que-se-ejecuta) |
| `there is no package called '...'` | Falta declarar ese paquete en **Instalar paquetes de R**. Ver [Código de R](#-código-de-r-que-se-ejecuta) |
| Sale una imagen rota 🖼️ | Revisa los `../` de la ruta y que mayúsculas y acentos del nombre coincidan exactamente. Ver [Cómo poner una imagen](#-cómo-poner-una-imagen-en-una-lección) |
| No veo los cambios | Recarga con `Cmd+Shift+R` o espera 2 minutos |
| `./nueva-leccion.sh: Permission denied` | Corre `chmod +x nueva-leccion.sh` una vez |

---

Hecho con [Quarto](https://quarto.org) + [GitHub Pages](https://pages.github.com)
