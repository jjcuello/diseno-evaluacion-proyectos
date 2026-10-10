# Diseño y Evaluación de Proyectos — Trabajo de Grado

## Datos generales de la asignatura

- **Profesora:** Carmen Díaz
- **Horarios:** Lunes 9:15 / Jueves 10:00
- **Bibliografía base:** Sapag Chain, Nassir y Reinaldo — *Preparación y Evaluación de Proyectos* (leer Capítulo 1)
- **Manual de referencia:** Manual de elaboración de Trabajos de Grado (Politécnico Santiago Mariño)

## Plan de evaluación

| Unidad | Contenido | Duración | Ponderación |
|---|---|---|---|
| I | Evaluación de Proyectos | 4 semanas | I Corte: 10–20 |
| II | La Investigación y el Marco Teórico | 6 semanas | II Corte: 10–20 |
| III | Las Estrategias metodológicas y su evaluación | 8 semanas | III Corte: 20–20 |

Estrategias metodológicas: conversatorios, trabajos escritos, exposiciones, cuadros comparativos, análisis.

## Conceptos clave vistos (Unidad I)

- **¿Qué es un proyecto?** Elaboración de una metodología, asignación de recursos y delimitación clara, con el fin de solucionar un problema.
- **Título del proyecto:** debe estar directamente ligado al Objetivo General y a la propuesta de investigación.
- **Factibilidad y viabilidad:** el proyecto debe ser factible; la viabilidad radica en generar un beneficio real.
- **Verbos de los objetivos:** entre los verbos que guían la solución del problema destacan **Diagnosticar, Diseñar y Evaluar**.

## Orientaciones del docente (revisión del borrador)

1. **Título sin verbos.** Si un texto lleva verbo, que sea uno solo; en esta primera entrega el título no lleva ninguno. El título nombra la solución (sustantivo + delimitación), no la acción. Así se evitan las objeciones habituales de los profesores de metodología.
2. **Un objetivo general y tres objetivos específicos.** El **objetivo general es el título redactado en infinitivo**: se antepone un único verbo al título y no se le agrega nada más. Cada objetivo específico lleva también un solo verbo.
3. **Del problema al título.** El proyecto da solución a un problema. Al estudiar ese problema en tres niveles, **macro** (mundial), **meso** (Latinoamérica) y **micro** (Venezuela, hasta llegar al Politécnico), se llega al **título**, que a su vez resuelve la problemática. *Escala precisada por la tutora de metodología.*
4. **Pocos títulos en el capítulo I.** Solo van los del Manual (cap. III, figuras 1 y 2): Contextualización del Problema, Objetivos de la Investigación (con Objetivo General y Objetivos Específicos) y Justificación de la Investigación. Los niveles, las causas, las consecuencias, el pronóstico, la delimitación y la formulación se redactan como prosa, pasando de una idea a la siguiente con conectores. Solo hay salto de página al cambiar de capítulo.
5. **Contextualización: unos cinco párrafos por nivel, de 10 a 13 líneas cada uno.** Referencia de la clase grupal, no exigida al leer el borrador.
6. **Guía de redacción de la clase grupal** (Departamento de Investigación y Postgrado): el problema se redacta en presente, de lo general a lo particular, contrastando la situación real con la deseada, con causas y consecuencias, y termina en las interrogantes. Se recomienda ilustrarlo con citas textuales, cuadros o valores y fotos reales. La justificación no repite las razones de la contextualización y dice a quién beneficia el trabajo. Los objetivos específicos omiten el *dónde*.
7. **Portada e índice** según los anexos C-1 y C-2 del Manual (fotos de la clase). Los márgenes (4 cm a la izquierda y 3 cm en los demás lados) se revisan con rigor: si no se cumplen, no se permite imprimir. Hay que imprimir en papel carta, al tamaño real (100 %), sin «ajustar a la página». En el índice, lo que aún no se ha redactado lleva «x» en lugar del número de página.
8. **Instrumento de evaluación:** [FOR-INVP-009](referencias/FOR-INVP-009.docx) registra los logros en cuatro momentos evaluativos: el problema, el marco referencial, el marco metodológico y los aspectos administrativos. Se usa como lista de control antes de cada entrega.

**Secuencia de trabajo:**

1. Problemática
2. Estudio del problema: macro → meso → micro
3. Título (la solución, sin verbos)
4. Objetivo general (el título en infinitivo, un solo verbo)
5. Tres objetivos específicos (Diagnosticar / Diseñar / Evaluar)

---

## Proyecto de grado

> **Título:** *"Plataforma web institucional de alojamiento y despliegue continuo (PaaS) para el Politécnico Santiago Mariño"*

El trabajo cuenta con dos tutores, y por eso se desarrolla en dos documentos:

| Documento | Tutor | Contenido |
|---|---|---|
| [Documento técnico](Documento-Tecnico.md) ([PDF](Documento-Tecnico.pdf)) | Tutor técnico | Planteamiento, arquitectura, cronograma, alcance e indicadores |
| [Documento metodológico](Documento-Metodologico.md) ([PDF](Documento-Metodologico.pdf), [Word](Documento-Metodologico.docx)) | Tutor metodológico | Portada, índice y capítulos según el Manual; hoy, el capítulo I |
| [Propuesta corta](Propuesta-Corta.md) ([PDF](Propuesta-Corta.pdf)) | Tutor metodológico | Línea de investigación, modalidad y estructura; nombre provisional, probablemente el Protocolo de Investigación |

Por ahora el trabajo se centra en el **capítulo I**. Los capítulos II y III se redactarán cuando se apruebe el I, y el documento técnico se ajustará cuando lo lea el profesor.

Las normas del Manual (5ª ed.) y del Reglamento de Trabajo de Grado (2025) están resumidas como *skills* para agentes en [.claude/skills/](.claude/skills/); el punto de entrada es [AGENTS.md](AGENTS.md).

## Generar los documentos

```
python generar_documentos.py
```

Produce:

- `Documento-Metodologico.pdf` y `.docx`: **la única versión del documento metodológico**, con el formato del Manual: portada según el anexo C-1 (con el logo), índice general según el anexo C-2, carta, márgenes de 4 y 3 cm, Arial 12, interlineado 1,5, preliminares en romanos y cuerpo desde la página 1. Se arma desde el capítulo I de `Documento-Metodologico.md`. Los capítulos pendientes no se imprimen, pero aparecen en el índice con «x». Los marcadores `[PENDIENTE…]` salen resaltados en amarillo. En el Word, los números del índice son campos: al abrirlo, Word pide actualizarlos.
- `Documento-Tecnico.pdf` y `Propuesta-Corta.pdf`: copias de trabajo, sin el formato del Manual.

Los datos de la portada (autor, tutor, docente, fecha), sus posiciones y las entradas fijas del índice están al comienzo de `generar_documentos.py`. El logo está en `plantillas/logo-iupsm-azul.jpg`.

**Convenciones de los borradores.** Los marcadores entre corchetes indican información que falta y que **no debe inventarse**:

- `[DIAGNÓSTICO: …]`: dato del Politécnico que se obtendrá en la fase de diagnóstico o que debe aportar el autor.
- `[PENDIENTE: …]`: dato administrativo por definir.
- `[FUENTE PENDIENTE: …]`: afirmación que necesita respaldo bibliográfico.

Todas las fuentes citadas están verificadas en `investigacion/fuentes.md`.

**Requisitos (Windows):** `pip install markdown weasyprint python-docx`, [Pandoc](https://pandoc.org) y Pango de MSYS2 (`winget install MSYS2.MSYS2` y luego `pacman -S mingw-w64-x86_64-pango` en la consola de MSYS2). El script encuentra Pango por su cuenta en `C:\msys64\mingw64\bin`. La plantilla de Word se regenera con `python plantillas/crear_referencia_docx.py`.

## Pendientes

- [ ] Confirmar con la profesora qué es la «propuesta corta» (todo indica que es el Protocolo de Investigación) y pedir su formato único.
- [ ] Preguntar qué va en el renglón «Xxxxxxxxx» del capítulo II en la guía del índice (anexo C-2); por ahora no se incluye.
- [ ] Confirmar las páginas preliminares de esta entrega. En la guía, el índice cae en la página iv porque antes van la portada y las constancias de aprobación del docente y del tutor (anexos A-2 y A-3), que el Manual exige en la versión para el jurado. Hoy el índice es la página ii.
- [ ] Si hay fotos reales del Politécnico (laboratorios, equipos), evaluar si ilustran la contextualización.
- [ ] Relevancia ambiental en la justificación (la guía de clase la menciona): solo si se encuentra una fuente verificada.
- [ ] Leer Capítulo 1 de Sapag Chain antes de la próxima clase.
- [x] Línea de investigación elegida: Sistemas de Comunicación → Transmisión de Datos → Virtualización (falta el aval formal del coordinador de línea al presentar el protocolo).
- [ ] Confirmar la modalidad (propuesta: Proyecto Factible; alternativa: Investigación Tecnológica) con el tutor metodológico.
- [ ] Añadir la fase de **alternativas de solución** (exigida en Proyecto Factible): comparar PaaS comerciales, PaaS de código abierto autoalojados (Coolify, Dokku, CapRover) y la solución propia sobre k3s.
- [x] Nivel macro: 4 fuentes verificadas en [investigacion/fuentes.md](investigacion/fuentes.md) (caso OPE/NERC de Boston University, Mass Open Cloud, Heroku).
- [x] Nivel meso: Nube UNAM y pagos PSE verificados (con correcciones a Gemini).
- [x] Antecedentes: 3 válidos y 1 complementario (Ecuador, 2022–2024) en [investigacion/fuentes.md](investigacion/fuentes.md).
- [x] Nivel micro: conectividad y electricidad (Freedom House 2024), universidades (ODHULA 2023) y límites de pago (Bancamiga 2024) verificados. Se descartó lo de la OFAC y el SWIFT que trajo Gemini.
- [ ] ⚠️ Las 5 "tesis venezolanas" que trajo Gemini no existen en la web: no citarlas (ver V6 en investigacion/fuentes.md).
- [ ] Antecedentes venezolanos de 2023 en adelante: consultar la Coordinación de Trabajo de Grado y la biblioteca del I.U.P.S.M., y los repositorios de la UCAB, la USB, la UCV, la UNET, la URBE, la ULA y la UNEXPO.
- [ ] Documento técnico: tratar el **racionamiento eléctrico** como riesgo explícito del clúster (autonomía del UPS, apagado ordenado, arranque automático, disponibilidad medida en el piloto).
- [ ] Buscar una fuente que demuestre la barrera de pago internacional en la región (pista: Global Findex del Banco Mundial).
- [ ] Reunir bases teóricas de 2016 en adelante.
- [ ] Identificar las bases legales aplicables (ciencia y tecnología, infogobierno, delitos informáticos, propiedad intelectual).
- [ ] Solicitar el aval escrito del Politécnico para realizar la investigación en sus instalaciones (Reglamento, art. 45).
- [ ] Al inscribir Proyecto de Investigación, ajustar el cronograma de 18 semanas al calendario del Reglamento (por ahora el trabajo se adelanta sin la materia inscrita).
- [ ] Incorporar al repositorio (carpeta `referencias/`) los PDF del Manual, el Reglamento y el esquema por naturaleza.
- [x] Verbo del objetivo general: **Diseñar** (decisión del autor; falta el visto bueno de la tutora).
- [x] Objetivos ajustados: OE2 «Definir la arquitectura…» y OE3 «Evaluar la factibilidad técnica, operativa y económica…», sin piloto (el piloto pasa a recomendaciones).
- [ ] Realinear el cronograma, el alcance y los indicadores del documento técnico al nuevo alcance (sin piloto; con prueba de concepto en laboratorio).
- [ ] Respaldar con fuentes citables los contextos macro, meso y micro (estadísticas, normativas, datos del Politécnico).
- [ ] Reescribir el estudio del problema de [Documento-Tecnico.md](Documento-Tecnico.md) con la nueva escala (macro mundial, meso Latinoamérica, micro Venezuela y el Politécnico).
- [ ] Solicitar al departamento de tecnología del Politécnico: espacio físico para los 3 equipos, segmento de red, IP pública (o permiso para Cloudflare Tunnel), delegación del subdominio `paas.psm.edu.ve` y proveedor de identidad (Google Workspace, Microsoft 365 o correo institucional).
- [ ] Confirmar el dominio institucional real (`psm.edu.ve` viene de la hoja de ruta y no está verificado).
- [ ] Definir si los 3 equipos HP los aporta el autor o el Politécnico (cambia el estudio económico) y relevar sus especificaciones (CPU, RAM, disco) para calcular la capacidad del piloto.
- [x] Sistema operativo de los nodos: AlmaLinux 9 o Rocky Linux 9 (familia Red Hat), sujeto a lo que administre el departamento de tecnología (pregunta incluida en la entrevista).
- [ ] Verificar el estado de las herramientas antes de implementar (Kaniko archivado, versiones de Traefik incluidas en k3s, Paketo, BuildKit rootless).
- [ ] Redactar el borrador del reglamento de uso aceptable para aprobación del Politécnico.
- [ ] Iniciar el diagnóstico (encuesta a estudiantes y docentes sobre necesidades de alojamiento).
