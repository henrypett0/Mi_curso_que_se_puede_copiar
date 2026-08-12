#!/bin/bash

# ============================================
# nueva-leccion.sh — Crea una nueva lección
# Uso: ./nueva-leccion.sh
# ============================================

# Encontrar el siguiente número de lección
ultimo=$(ls lecciones/leccion-*.qmd 2>/dev/null | sort -V | tail -1 | grep -o '[0-9]\+')
if [ -z "$ultimo" ]; then
  siguiente=1
else
  siguiente=$((10#$ultimo + 1))
fi
numero=$(printf "%02d" $siguiente)

# Pedir datos
echo ""
echo "📝 Nueva lección #$numero"
echo "========================"
echo ""
read -p "Título: " titulo
read -p "Descripción breve: " descripcion

fecha=$(date +%Y-%m-%d)
archivo="lecciones/leccion-${numero}.qmd"

# Crear archivo
cat > "$archivo" << EOF
---
title: "Lección ${numero}: ${titulo}"
description: "${descripcion}"
date: "${fecha}"
---

## ${titulo}

Escribe tu contenido aquí.
EOF

echo ""
echo "✅ Creada: $archivo"
echo ""

# Validar (la misma validación que corre en GitHub antes de publicar)
echo "🔍 Validando lecciones..."
echo ""
if ! python3 scripts/validar-lecciones.py; then
  echo ""
  echo "⚠️  Corrige los problemas de arriba antes de hacer push,"
  echo "    o GitHub rechazará la publicación del sitio."
  exit 1
fi

echo ""
echo "Siguiente paso:"
echo "  1. Edita $archivo con tu contenido"
echo "  2. git add . && git commit -m \"agregar leccion $numero\" && git push"
echo ""
