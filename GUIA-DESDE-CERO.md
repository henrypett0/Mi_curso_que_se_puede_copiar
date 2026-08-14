# 🏗️ Guía: construir este sistema desde cero

Esta guía es para quien quiere **entender y armar** este proyecto pieza por pieza,
empezando desde una cuenta de GitHub recién creada y nada más.

> ¿Solo quieres publicar tu curso rápido? No leas esto. Copia la plantilla y sigue
> el [README](README.md) — te toma 10 minutos. Esta guía es para entender **cómo
> está hecho** y poder construirlo tú mismo.

---

## 🎯 Qué vas a construir

Un sitio web de curso que se publica solo. Escribes una lección en un archivo de
texto, la subes, y en 2 minutos está en internet.

```
Escribes leccion-05.qmd
        ↓
   git push
        ↓
GitHub revisa que la lección esté bien formada   ← el "validador"
        ↓
   ¿está bien?
    ↙        ↘
   NO         SÍ
    ↓          ↓
 Se detiene   Quarto convierte los .qmd en HTML
 El sitio          ↓
 anterior     Se publica en GitHub Pages
 sigue intacto     ↓
              Tu curso en internet
```

La pieza que casi nadie pone —y es la que salva— es el **validador**. Sin él, una
fecha mal escrita se publica silenciosamente rota. Con él, el sitio bueno se queda
como está y tú recibes un mensaje diciéndote exactamente qué archivo arreglar.

### Las herramientas y por qué cada una

| Herramienta | Para qué sirve | ¿Cuesta? |
|-------------|----------------|----------|
| **GitHub** | Guarda tus archivos y su historial | Gratis |
| **Quarto** | Convierte tus archivos de texto en un sitio web bonito | Gratis |
| **GitHub Pages** | Hospeda el sitio en internet | Gratis |
| **GitHub Actions** | El robot que hace todo el proceso solo | Gratis |
| **Python** | Corre el validador (ya viene en Mac y en el servidor) | Gratis |

Todo el sistema cuesta **$0** mientras tu repo sea público.

---

## 📋 Parte 0: lo que necesitas antes de empezar

1. **Una cuenta de GitHub.** Si no la tienes: [github.com/signup](https://github.com/signup).
2. **Una computadora** con Mac, Windows o Linux.
3. **Nada de experiencia programando.** En serio. Vas a copiar y pegar archivos de
   texto.

Lo que **no** necesitas: saber HTML, pagar hosting, ni entender qué es un servidor.

---

## 🥇 Parte 1: crear el repositorio

Un "repositorio" (o *repo*) es la carpeta de tu proyecto, guardada en GitHub.

1. Entra a [github.com/new](https://github.com/new)
2. **Repository name:** el nombre de tu curso, sin espacios (ej. `mi-curso-finanzas`)
3. **Public** ← obligatorio, si es privado GitHub Pages te cobra
4. Marca **Add a README file**
5. Click en **Create repository**

Ya tienes tu repo. La barra de direcciones dice algo como
`github.com/tu-usuario/mi-curso-finanzas`.

> **Concepto clave:** todo lo que pongas en la rama `main` de este repo es lo que se
> publica. `main` es la línea principal de tu proyecto.

---

## 🥈 Parte 2: instalar Quarto y bajar el repo

### Instala Quarto

Descárgalo de [quarto.org/docs/get-started](https://quarto.org/docs/get-started/) e
instálalo como cualquier programa. Para comprobar que quedó, abre la Terminal
(en Mac: `Cmd+Espacio` → escribe "Terminal") y corre:

```bash
quarto --version
```

Si responde con un número (ej. `1.8.27`), listo.

### Baja el repo a tu computadora

En la página de tu repo: botón verde **Code** → copia la URL. Luego en la Terminal:

```bash
cd Documents
git clone https://github.com/TU-USUARIO/TU-REPO.git
cd TU-REPO
```

Ahora tienes una carpeta local conectada a GitHub. Los cambios que hagas aquí se
suben con `git push`.

---

## 🥉 Parte 3: el esqueleto del sitio

Vas a crear 4 archivos. Explico qué hace cada uno **antes** de que lo copies, para
que no sea magia.

### 3.1 `_quarto.yml` — la configuración

Este archivo le dice a Quarto qué tipo de sitio quieres y cómo se ve el menú.

```yaml
project:
  type: website
  output-dir: _site

website:
  title: "Nombre de Tu Curso"
  navbar:
    left:
      - text: "Inicio"
        href: index.qmd
      - text: "Lecciones"
        href: lecciones.qmd

format:
  html:
    theme: cosmo
    toc: true
    lang: es
```

Línea por línea:

| Línea | Qué hace |
|-------|----------|
| `type: website` | "Esto es un sitio de varias páginas", no un documento suelto |
| `output-dir: _site` | El sitio construido se guarda en la carpeta `_site` |
| `title:` | El nombre que sale arriba a la izquierda |
| `navbar:` | Los botones del menú superior |
| `theme: cosmo` | El diseño. Hay ~25 gratis en [quarto.org/docs/output-formats/html-themes](https://quarto.org/docs/output-formats/html-themes.html) |
| `toc: true` | Muestra el índice lateral "En esta página" |
| `lang: es` | Pone en español los textos automáticos (fechas, "Índice", etc.) |

> El `_` inicial del nombre no es decorativo: Quarto trata los archivos que empiezan
> con `_` como archivos de configuración y **no los publica** como páginas. Este
> detalle vuelve a aparecer más adelante.

### 3.2 `index.qmd` — la página de inicio

`index` es un nombre especial: es la página que se abre por defecto.

```markdown
---
title: "Bienvenido"
---

Este es el sitio web del curso. Navega a **Lecciones** para ver el contenido.
```

Todo archivo `.qmd` tiene dos partes:

1. **El encabezado**, entre `---` y `---`. Son datos *sobre* la página.
2. **El contenido**, debajo. Es Markdown normal.

### 3.3 `lecciones.qmd` — el índice automático

Aquí está el primer truco que ahorra trabajo de verdad. Esta página **no** tiene una
lista escrita a mano: Quarto la arma sola leyendo tus lecciones.

```yaml
---
title: "Lecciones"
listing:
  contents: lecciones/*.qmd
  sort: "date asc"
  type: table
  fields: [date, title, description]
  field-display-names:
    date: "Fecha"
    title: "Lección"
    description: "Descripción"
---
```

`listing` significa "haz una lista automática":

- `contents: lecciones/*.qmd` → mira todos los `.qmd` de esa carpeta
- `sort: "date asc"` → ordénalos por fecha, del más viejo al más nuevo
- `fields:` → muestra estas tres columnas

**Aquí nace la regla más importante del proyecto.** Para que esta tabla funcione,
cada lección *tiene* que traer `title`, `description` y `date` en su encabezado.
Si a una le falta la fecha, aparece con la casilla vacía o se ordena mal. Ese es
exactamente el problema que el validador va a resolver más adelante.

### 3.4 `.gitignore` — lo que no se sube

Cuando Quarto construye el sitio genera carpetas temporales que no tiene sentido
guardar en GitHub. Este archivo las excluye:

```
_site/
.quarto/
.DS_Store
```

- `_site/` → el sitio construido; se genera solo en cada deploy
- `.quarto/` → caché interno de Quarto
- `.DS_Store` → basura que macOS deja en cada carpeta

---

## 📖 Parte 4: las lecciones

### 4.1 La convención de nombres

Cada lección se llama `leccion-NN.qmd`, con **dos dígitos**:

```
lecciones/
├── leccion-01.qmd
├── leccion-02.qmd
└── leccion-03.qmd
```

¿Por qué dos dígitos y no `leccion-1.qmd`? Porque las computadoras ordenan texto
alfabéticamente, y así `leccion-10` quedaría **antes** que `leccion-2`. Con el cero
adelante, el orden alfabético coincide con el numérico.

### 4.2 `lecciones/_plantilla.qmd`

Un archivo de referencia para copiar y pegar:

```markdown
---
title: "Lección X: TITULO"
description: "DESCRIPCION BREVE"
date: "YYYY-MM-DD"
---

## Sección 1

Escribe tu contenido aquí.
```

Fíjate en el `_` del inicio: gracias a él Quarto lo ignora y no aparece publicado
como una lección vacía. Recuerda este detalle — **causa un problema real más
adelante en esta guía**.

### 4.3 Tu primera lección

`lecciones/leccion-01.qmd`:

```markdown
---
title: "Lección 1: Introducción"
description: "Primera lección del curso"
date: "2026-01-01"
---

## Bienvenida

Este es un ejemplo de lección.
```

La fecha va en formato **año-mes-día**. Es el estándar internacional (ISO 8601) y
existe por una razón práctica: es el único formato que se ordena solo. Además evita
la ambigüedad de `03/04/2026`, que en México es 3 de abril y en Estados Unidos es 4
de marzo.

---

## 👀 Parte 5: verlo antes de publicar

En la Terminal, dentro de tu carpeta:

```bash
quarto preview
```

Se abre tu navegador con el sitio funcionando en tu computadora. Mientras esté
corriendo, cada vez que guardes un archivo la página se actualiza sola.

Para detenerlo: `Ctrl+C` en la Terminal.

> Esto es **local**: solo tú lo ves. Nadie más tiene acceso todavía.

---

## 🚀 Parte 6: publicarlo en internet

Aquí se conectan dos cosas: **GitHub Pages** (el hospedaje) y **GitHub Actions**
(el robot que construye el sitio).

### 6.1 Activa GitHub Pages

En tu repo: **Settings** → **Pages** → en "Source" selecciona **GitHub Actions**.

> ⚠️ Sin este paso nada funciona, y el error no es obvio: el robot corre en verde
> pero el sitio nunca aparece.

### 6.2 El workflow

Crea el archivo `.github/workflows/deploy.yml`. Ese nombre de carpeta no es
negociable: es donde GitHub busca las automatizaciones.

```yaml
name: Deploy Quarto Site

on:
  push:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Checkout
        uses: actions/checkout@v5

      - name: Setup Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Render
        uses: quarto-dev/quarto-actions/render@v2

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: _site

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

Traducido a español:

| Bloque | Qué significa |
|--------|---------------|
| `on: push: branches: [main]` | "Haz esto cada vez que suba algo a main" |
| `permissions:` | Los permisos que el robot necesita para publicar |
| `runs-on: ubuntu-latest` | GitHub te presta una computadora Linux nueva |
| `steps:` | La receta, en orden |
| `Checkout` | Baja tus archivos a esa computadora prestada |
| `Setup Quarto` | Instala Quarto ahí |
| `Render` | Convierte tus `.qmd` en HTML |
| `Upload artifact` | Empaqueta la carpeta `_site` |
| `Deploy to GitHub Pages` | La publica |

**El concepto que hay que entender:** esa computadora prestada **nace vacía y se
destruye al terminar**. No tiene tus programas ni tus archivos. Todo lo que necesite
—Quarto, R, paquetes— hay que instalarlo en cada corrida. Esto explica la mitad de
los errores que vas a ver en tu vida con Actions.

### 6.3 Súbelo

```bash
git add .
git commit -m "sitio inicial"
git push
```

Ve a la pestaña **Actions** de tu repo y verás al robot trabajando. Al terminar, tu
sitio está en:

```
https://TU-USUARIO.github.io/TU-REPO/
```

**Hasta aquí ya tienes un sitio de curso que se publica solo.** Lo que sigue es lo
que lo vuelve confiable.

---

## 🛡️ Parte 7: el validador

### El problema que resuelve

Escribes una lección con la fecha así: `date: "15/03/2026"`. Subes. El robot corre
en **verde**, todo parece bien... y tu lección aparece en el sitio con la fecha vacía
y ordenada en el lugar equivocado. Nadie te avisó.

Peor: si el error rompe el render, el deploy falla y **el sitio se queda a medias**.

La solución es revisar las lecciones **antes** de construir nada.

### Qué revisa

1. Que estén los 3 campos: `title`, `description`, `date` — y que no estén vacíos
2. Que la fecha sea real y en formato `YYYY-MM-DD` (`2026-13-45` no existe)
3. Que el archivo se llame `leccion-NN.qmd`
4. Que no haya dos lecciones con el mismo número
5. Que no haya archivos sueltos que Quarto no vaya a publicar

### El código

Está completo en [`scripts/validar-lecciones.py`](scripts/validar-lecciones.py) —
cópialo tal cual a tu proyecto. Aquí explico las decisiones que importan.

**Se escribió en Python y sin librerías externas** a propósito. Python ya viene
instalado en Mac, en Linux y en el servidor de GitHub, así que el validador corre
en todos lados sin instalar nada. Si usara una librería de YAML habría que
instalarla en cada corrida.

**Lee el encabezado a mano**, línea por línea, en vez de usar un parser de YAML:

```python
if not lineas or lineas[0].strip() != "---":
    return {}, "no tiene encabezado YAML (debe empezar con --- en la línea 1)"
```

**Valida la fecha en dos pasos**, y esto es más sutil de lo que parece:

```python
if not PATRON_FECHA.match(fecha):
    # el formato está mal: "15/03/2026"
else:
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        # el formato está bien pero la fecha no existe: "2026-13-45"
```

Un solo patrón no basta: `2026-13-45` **cumple** el formato `YYYY-MM-DD` y aun así
no es una fecha. Por eso se intenta convertir de verdad.

**Junta todos los errores antes de rendirse.** Podría detenerse en el primero, pero
entonces arreglas uno, vuelves a subir, esperas 2 minutos y descubres el siguiente.
Reportando todos de golpe arreglas una vez.

**Ignora los archivos que empiezan con `_`:**

```python
rutas = {p for p in CARPETA.glob("*.qmd") if not p.name.startswith("_")}
```

Sin esta línea el proyecto **no funcionaría nunca**: `_plantilla.qmd` tiene la fecha
literal `YYYY-MM-DD`, así que fallaría en cada corrida, para siempre.

### Pruébalo

```bash
python3 scripts/validar-lecciones.py
```

Con todo bien:

```
✅ 4 lección(es) validada(s) correctamente
```

Rompe una lección a propósito y vuelve a correrlo. Debe decirte el archivo y el
campo exactos. **Prueba que falla antes de confiar en que funciona** — un validador
que nunca viste fallar puede estar aprobando todo.

---

## 🔗 Parte 8: conectar el validador al deploy

Que el validador exista no sirve de nada si el deploy no lo obedece. Hay que
convertirlo en un **portero**.

Se parte el workflow en dos trabajos, y el segundo depende del primero:

```yaml
jobs:
  validar:
    name: Validar lecciones
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v5

      - name: Validar encabezados y nombres de las lecciones
        run: python3 scripts/validar-lecciones.py

  build-deploy:
    name: Construir y publicar
    needs: validar          # ← la línea clave
    if: github.event_name == 'push'
    runs-on: ubuntu-latest
    steps:
      # ... todo lo de la Parte 6
```

Dos líneas hacen el trabajo:

- **`needs: validar`** → "no empieces a construir hasta que la validación pase".
  Si el validador falla, el deploy **ni siquiera arranca** y el sitio publicado se
  queda intacto.
- **`if: github.event_name == 'push'`** → solo publica en pushes de verdad.

Y se agrega el disparador de pull requests:

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
```

Así, si alguien propone un cambio, se valida sin publicar nada.

> **Cómo saber que el portero funciona:** crea un archivo `lecciones/prueba.txt`,
> súbelo y confirma que el run sale ❌ y que tu sitio **no** cambió. Luego bórralo.
> Este proyecto se probó exactamente así.

---

## ⚡ Parte 9: el script para crear lecciones

Crear lecciones a mano es repetitivo y propenso a errores: hay que recordar el
número siguiente, el formato de fecha, los tres campos.

[`nueva-leccion.sh`](nueva-leccion.sh) lo hace por ti. Copia el archivo del repo; lo
importante son dos ideas.

**Calcula el número solo:**

```bash
ultimo=$(ls lecciones/leccion-*.qmd 2>/dev/null | sort -V | tail -1 | grep -o '[0-9]\+')
siguiente=$((10#$ultimo + 1))
numero=$(printf "%02d" $siguiente)
```

El `10#` de ahí es un detalle que muerde: sin él, bash interpreta `08` como número
**octal** y truena, porque en octal no existe el 8.

**Corre la misma validación al terminar:**

```bash
if ! python3 scripts/validar-lecciones.py; then
  echo "⚠️  Corrige los problemas antes de hacer push"
  exit 1
fi
```

Esta es la decisión de diseño más importante del proyecto: **una sola fuente de
verdad**. El script local y el servidor corren *el mismo archivo*. Si fueran dos
copias de la misma lógica, tarde o temprano una cambiaría y tendrías un validador
local que aprueba lo que el servidor rechaza — el peor de los mundos.

Dale permiso de ejecución una vez:

```bash
chmod +x nueva-leccion.sh
```

---

## 📊 Parte 10 (opcional): código de R que se ejecuta

Si tu curso enseña R y quieres que las lecciones muestren **resultados calculados**
—tablas, gráficas— y no solo el código, necesitas dos pasos más en el workflow:

```yaml
      - name: Setup R
        uses: r-lib/actions/setup-r@v2
        with:
          use-public-rspm: true

      - name: Instalar paquetes de R
        shell: Rscript {0}
        run: |
          install.packages(c("knitr", "rmarkdown"))
```

Recuerda el concepto de la Parte 6: **la computadora prestada nace vacía**. Tu Mac
tiene R y tus paquetes; el servidor no. Todo lo que uses hay que declararlo ahí.

Detalles en la sección de R del [README](README.md).

---

## 🩹 Parte 11: los errores que de verdad salieron

Esta parte no es teórica. Son los tropiezos reales al construir este proyecto, con
sus mensajes tal como aparecieron. Te vas a encontrar los mismos.

### `Unable to locate an installed version of R`

**Qué pasó:** una lección usaba bloques ` ```{r} ` (con llaves = "ejecuta esto"). En
la Mac funcionaba porque tenía R instalado. En el servidor no.

**La lección de fondo:** *"en mi computadora sí funciona"* casi siempre significa que
instalaste algo hace meses y se te olvidó. El servidor no olvida porque nunca supo.

**Arreglo:** los pasos de la Parte 10. Y ojo, no basta `knitr`: también hace falta
`rmarkdown`.

### Un archivo `.md` desaparecía sin avisar

**Qué pasó:** el validador solo miraba archivos `.qmd`. Una lección guardada como
`.md` no la revisaba **nadie**: no daba error, y tampoco se publicaba. Simplemente
no existía.

**La lección de fondo:** un validador que solo revisa lo que espera encontrar tiene
un punto ciego. Lo peligroso no es lo que falla ruidosamente, es lo que se ignora en
silencio.

**Arreglo:** revisar **todo** lo que hay en `lecciones/`, y marcar como error
cualquier cosa que no sea una lección válida ni un adjunto reconocido (imágenes,
PDF, CSV).

### Un archivo sin extensión pasaba en verde

**Qué pasó:** al probar el portero con un archivo llamado `hola-va-a-fallar`... no
falló. No tenía extensión, así que se escapaba de todas las revisiones.

**La lección de fondo:** **prueba tus validaciones con casos que deban fallar.** Si
solo pruebas que lo bueno pasa, nunca descubres lo que se cuela.

### Un espacio invisible rompía el encabezado

**Qué pasó:** un espacio antes de los guiones (` ---` en vez de `---`) rompe el
encabezado en Quarto, pero el validador lo aceptaba porque limpiaba los espacios
antes de comparar.

**Arreglo:** exigir que la primera línea sea exactamente `---`.

### `Node.js 20 is deprecated`

**Qué pasó:** un aviso amarillo en cada corrida. **No es un error** — el deploy
funcionaba igual.

**La lección de fondo:** aprende a distinguir un aviso (amarillo, informativo) de un
error (rojo, detiene todo). Perseguir avisos que no rompen nada es una forma común
de perder la tarde.

**Arreglo:** subir `actions/checkout` de `v4` a `v5`.

---

## ✅ Checklist final

Cuando termines, deberías tener:

- [ ] Repo público en GitHub
- [ ] **Settings → Pages → Source: GitHub Actions** activado
- [ ] `_quarto.yml` con el nombre de tu curso
- [ ] `index.qmd` y `lecciones.qmd`
- [ ] `lecciones/` con `_plantilla.qmd` y al menos una lección
- [ ] `.gitignore`
- [ ] `scripts/validar-lecciones.py`
- [ ] `.github/workflows/deploy.yml` con los dos jobs y el `needs: validar`
- [ ] `nueva-leccion.sh` con permiso de ejecución
- [ ] Probado que el validador **falla** con una lección rota
- [ ] Tu sitio abriendo en `https://TU-USUARIO.github.io/TU-REPO/`

---

## 🗺️ Mapa de archivos

```
tu-curso/
├── _quarto.yml                    ← configuración del sitio (Parte 3.1)
├── index.qmd                      ← página de inicio (Parte 3.2)
├── lecciones.qmd                  ← índice automático (Parte 3.3)
├── .gitignore                     ← lo que no se sube (Parte 3.4)
├── nueva-leccion.sh               ← crea lecciones (Parte 9)
├── README.md                      ← guía de uso diario
├── GUIA-DESDE-CERO.md             ← este archivo
├── scripts/
│   └── validar-lecciones.py       ← el validador (Parte 7)
├── lecciones/
│   ├── _plantilla.qmd             ← plantilla, ignorada por el `_`
│   └── leccion-01.qmd             ← tus lecciones
└── .github/workflows/
    └── deploy.yml                 ← la automatización (Partes 6 y 8)
```

---

## 📚 Para seguir

- [Documentación de Quarto](https://quarto.org/docs/websites/) — sitios web
- [Temas visuales](https://quarto.org/docs/output-formats/html-themes.html) — cambiar el `theme:`
- [GitHub Actions](https://docs.github.com/es/actions) — automatizaciones
- [README de este repo](README.md) — el uso del día a día

---

Hecho con [Quarto](https://quarto.org) + [GitHub Pages](https://pages.github.com)
