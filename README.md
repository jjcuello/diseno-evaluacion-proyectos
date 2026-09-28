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
- **Estructura de objetivos:** 5 objetivos/pasos para dar solución al problema, entre los que destacan **Diagnosticar, Diseñar y Evaluar**.

---

## Las tres propuestas de proyecto

Se requiere presentar tres candidatos a Proyecto de Grado. Cada título fue formulado para quedar ligado a un Objetivo General claro, siguiendo el criterio de Sapag Chain de que todo proyecto debe demostrar factibilidad (técnica) y viabilidad (beneficio real para un tercero).

### 1. Plataforma institucional de alojamiento de proyectos académicos

> **Título propuesto:** *"Diseño y evaluación de factibilidad de una plataforma institucional de alojamiento y despliegue continuo (PaaS) para proyectos académicos universitarios"*

- **Problema diagnosticado:** estudiantes y profesores necesitan alojar proyectos de distintas materias y niveles de complejidad, y hoy dependen de servicios externos (Render, Vercel, Heroku, etc.) que implican costos, dependencia externa y falta de control institucional sobre los datos académicos.
- **Pregunta de investigación:** ¿en qué medida es factible, técnica y económicamente, diseñar una plataforma de alojamiento institucional que permita a estudiantes y profesores desplegar proyectos académicos sin depender de servicios externos de pago?
- **Objetivo general:** diseñar y evaluar la factibilidad técnica y económica de una plataforma tipo Render alojada en la infraestructura de la universidad, que permita a estudiantes y docentes desplegar proyectos de curso mediante un flujo simple (ej. git push).
- **Objetivos específicos (Diagnosticar / Diseñar / Evaluar):**
    1. Diagnosticar las necesidades de alojamiento de proyectos académicos en la comunidad universitaria (encuestas a estudiantes/profesores).
    2. Diseñar la arquitectura de la plataforma: stacks soportados, aislamiento por contenedores, límites de recursos, flujo de despliegue.
    3. Evaluar la viabilidad mediante un piloto con 2–3 materias, midiendo adopción, ahorro frente a servicios externos e incidentes de seguridad.
- **Alcance:** soporte a un set fijo de stacks (Node, Python, sitios estáticos), despliegue vía git push, aislamiento por contenedor, límites de recursos básicos, piloto con 2–3 materias durante un período académico.
- **Fuera de alcance:** bases de datos gestionadas complejas, facturación multiusuario, alta disponibilidad/escalado multiservidor, integraciones con CI/CD externas, soporte a stacks fuera del set definido.
- **Indicadores de evaluación:** % de reducción de costo frente a servicios externos, tiempo promedio de despliegue vs. proceso manual, número de proyectos alojados durante el piloto, incidentes de seguridad registrados, satisfacción de usuarios (encuesta post-piloto).
- **Alcance recomendado (para que sea viable en el tiempo del curso):** sin intentar replicar la totalidad de funcionalidades de un PaaS comercial. El mayor riesgo técnico es la ejecución de código de terceros (sandboxing, aislamiento, cuotas), que debe tratarse como el núcleo del capítulo de diseño.
- **Métrica de viabilidad (costo-beneficio):** no se mide en ventas, sino comparando el costo de mantener la infraestructura en la universidad frente al costo de que alumnos/profesores paguen servicios externos, más el tiempo perdido en configuraciones manuales de despliegue.
- **Base técnica de partida:** ninguna existente; sería desarrollo nuevo, apoyado en la experiencia de despliegue/orquestación de servidores ya adquirida.

### 2. Software base de gestión administrativa para instituciones educativas

> **Título propuesto:** *"Diseño y evaluación de un sistema base de gestión administrativa, académica y financiera para instituciones de educación básica y media"*

- **Problema diagnosticado:** las instituciones educativas privadas de pequeña/mediana escala suelen gestionar inscripciones, facturación y nómina con herramientas manuales (hojas de cálculo) o sistemas genéricos no adaptados a su operación, generando errores de imputación y falta de trazabilidad.
- **Pregunta de investigación:** ¿es posible diseñar un modelo de software base, genérico y configurable, que resuelva los procesos de inscripción, facturación y nómina comunes a instituciones educativas privadas de pequeña/mediana escala, y evaluar su eficiencia frente a la gestión manual?
- **Objetivo general:** diseñar y evaluar un sistema base (no atado a una institución específica) que resuelva de forma genérica y configurable los procesos de inscripción, facturación por consumo y nómina de una institución educativa tipo.
- **Objetivos específicos:**
    1. Diagnosticar los procesos administrativos comunes a instituciones educativas de escala similar (inscripciones, facturación, nómina).
    2. Diseñar un modelo de datos y una arquitectura genérica y configurable (multi-institución), separando lo específico de un caso particular de lo reutilizable.
    3. Evaluar el sistema mediante un caso de estudio simulado o anonimizado, midiendo reducción de errores de imputación y tiempo administrativo.
- **Alcance:** modelo de datos multi-institución; módulos de inscripción, facturación por consumo, nómina y auditoría; validación con caso de estudio simulado o anonimizado.
- **Fuera de alcance:** integración con sistemas contables externos de terceros, módulos académicos (notas, asistencia) si no existen ya en la base, soporte multi-idioma, despliegue como SaaS público para múltiples clientes reales.
- **Indicadores de evaluación:** horas-hombre ahorradas, % de reducción de errores de imputación, tiempo de cierre administrativo mensual, cobertura de auditoría (eventos registrados vs. eventos críticos totales).
- **Nota importante de alcance:** este candidato se apoya en la base ya construida y probada en producción (APP-FANA), pero **se presenta ante la universidad como un software base genérico**, sin exponer datos, nombre ni detalles operativos de la institución real que lo usa hoy (es una fuente de ingreso activa, no un proyecto académico). El trabajo de grado documentaría el diseño generalizado del sistema, no el caso de uso específico.
- **Métrica de viabilidad (eficiencia operativa):** horas-hombre ahorradas y reducción de costos por errores contables/de imputación, comparando el proceso manual (o con hojas de cálculo) contra el sistema.
- **Base técnica de partida:** la más madura de las tres — sistema en producción con módulos de inscripciones, facturación "por consumo", nómina y auditoría ya resueltos y validados con datos reales. Esto reduce el riesgo técnico casi a cero y permite concentrar el esfuerzo del curso en la parte metodológica y documental (formato del Politécnico Santiago Mariño).

### 3. Sistema de gestión y evaluación financiera de carteras de préstamos y fondos de inversión

> **Título propuesto:** *"Diseño y evaluación de un sistema de gestión y evaluación de rentabilidad para carteras de préstamos y fondos de inversión de pequeña escala"*

- **Problema diagnosticado:** la gestión de préstamos y fondos de inversión de pequeña escala requiere trazabilidad contable, cálculo confiable de rentabilidad y controles de acceso por rol, algo que hojas de cálculo o sistemas genéricos no garantizan con integridad transaccional.
- **Pregunta de investigación:** ¿cómo diseñar un sistema transaccional con controles de auditoría que garantice trazabilidad e integridad en la gestión de carteras de préstamos y fondos de inversión de pequeña escala, y cómo evaluar su aporte a la rentabilidad y a la reducción del riesgo operativo?
- **Objetivo general:** diseñar y evaluar un sistema que permita administrar carteras de préstamos y fondos de inversión con integridad transaccional, trazabilidad de auditoría y proyecciones de rentabilidad.
- **Objetivos específicos:**
    1. Diagnosticar los riesgos operativos y contables de la gestión manual de préstamos y fondos (sobreconteos, duplicados, reconstrucciones erróneas).
    2. Diseñar un modelo transaccional con controles de acceso por rol y bitácora de auditoría para las operaciones críticas.
    3. Evaluar el sistema mediante indicadores de rentabilidad mensual/acumulada y un simulador de proyecciones para inversionistas.
- **Alcance:** modelo transaccional (alta, cobro, avances, amortización, cierre), control de acceso por rol, bitácora de auditoría, indicadores de rentabilidad mensual/acumulada, simulador de proyecciones.
- **Fuera de alcance:** integración con banca real o pasarelas de pago, cumplimiento regulatorio formal ante entes de supervisión financiera, gestión de múltiples monedas/inflación, aplicación móvil completa.
- **Indicadores de evaluación:** % de reducción de errores de reconstrucción histórica, tiempo de cierre mensual, cobertura de auditoría, precisión de las proyecciones del simulador frente a resultados reales.
- **Ventaja particular:** es el candidato más alineado temáticamente con la bibliografía del curso (Sapag Chain trata directamente evaluación financiera de proyectos: flujo de caja, rentabilidad, VAN, TIR, factibilidad económica). El software mismo es una herramienta de evaluación financiera, así que la tesis "habla el mismo idioma" que la materia durante todo el semestre — es la más fácil de justificar económicamente.
- **Nota de confidencialidad (igual que el candidato 2):** es un negocio secundario real (gestión de fondos/inversionistas propios), por lo que se presenta ante la universidad de la misma forma — como software base genérico, sin exponer cifras, identidad de fondos ni clientes reales. Los objetivos deben enfocarse en el diseño del sistema transaccional y la seguridad de la auditoría, no en los datos del negocio que lo respalda.
- **Base técnica de partida:** plataforma en producción (Next.js + Supabase) con módulos de préstamos, fondos, rentabilidad, auditoría e inteligencia de negocio ya funcionando.

---

## Matriz comparativa

| Criterio | 1. PaaS institucional | 2. Gestión administrativa | 3. Financiero (préstamos/fondos) |
|---|---|---|---|
| Originalidad | Alta | Media | Media-alta |
| Riesgo técnico | Alto (sandboxing, aislamiento) | Bajo | Bajo-medio |
| Alineación con la materia (Sapag Chain) | Media | Media | Alta |
| Evidencia disponible (base ya construida) | Ninguna — desarrollo nuevo | Alta (en producción) | Alta (en producción) |
| Ajuste al cronograma (18 semanas del curso) | Exigente, depende de disciplina de alcance | Cómodo | Cómodo |
| Facilidad de evaluación de resultados | Media (requiere piloto real) | Alta | Alta |
| Dependencia de datos sensibles a anonimizar | Ninguna | Alta | Alta |

## Recomendación

No hay un orden único correcto todavía: la mejor opción depende de si la profesora acepta partir de sistemas ya operativos (candidatos 2 y 3) o exige desarrollo enteramente nuevo, y de qué se quiere priorizar — originalidad técnica vs. defendibilidad metodológica. Con eso claro:

- **Si buscas la propuesta más defendible, con menor riesgo de ejecución** → **Opción 2**. Riesgo técnico casi nulo; el trabajo real está en la abstracción del dominio y la narrativa (debe leerse como diseño y evaluación, no como "mostrar el software que ya hice").
- **Si buscas la propuesta más potente y original, con más margen para lucirte** → **Opción 1**, pero acotada con disciplina desde el primer corte (2–3 stacks, aislamiento simple, piloto corto). Sin ese recorte puede consumir el trabajo de grado entero solo en infraestructura.
- **Si buscas la mejor alineación con la teoría del curso** → **Opción 3**. Facilita los estudios de rentabilidad (VAN, TIR, flujo de caja) durante todo el semestre, con el mismo riesgo de narrativa que la opción 2 (cuidar la confidencialidad del negocio real).

**Recomendación concreta:** no dar la opción 1 por favorita de entrada solo por ser la más original — en un jurado universitario suele pesar tanto o más la defendibilidad metodológica y la facilidad de mostrar resultados medibles. Antes de comprometerte, confirma con la profesora si aceptan proyectos basados en sistemas ya operativos; si la respuesta es sí, la opción 2 es objetivamente la de menor riesgo.

## Pendientes

- [ ] Leer Capítulo 1 de Sapag Chain antes de la próxima clase.
- [ ] **Definir con la profesora si se permite basar un proyecto en software ya existente en producción (candidatos 2 y 3), o si se exige desarrollo nuevo** — esto condiciona directamente cuál de las tres conviene más.
- [ ] Decidir el criterio de selección final entre las tres alternativas (usar la matriz comparativa como base).
- [ ] Si se elige el candidato 1, iniciar el diagnóstico (encuesta a estudiantes/profesores sobre necesidades de alojamiento).
- [ ] Si se elige el candidato 2 o 3, trabajar la narrativa de generalización/anonimización antes de la exposición.
- [ ] Evaluar si conviene preparar una versión formal del documento para entregar a la profesora (estructura de anteproyecto según el manual del Politécnico Santiago Mariño).
