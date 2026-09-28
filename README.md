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

### 1. Plataforma institucional de alojamiento de proyectos académicos (favorita)

> **Título propuesto:** *"Diseño y evaluación de factibilidad de una plataforma institucional de alojamiento y despliegue continuo (PaaS) para proyectos académicos universitarios"*

- **Problema diagnosticado:** estudiantes y profesores necesitan alojar proyectos de distintas materias y niveles de complejidad, y hoy dependen de servicios externos (Render, Vercel, Heroku, etc.) que implican costos, dependencia externa y falta de control institucional sobre los datos académicos.
- **Objetivo general:** diseñar y evaluar la factibilidad técnica y económica de una plataforma tipo Render alojada en la infraestructura de la universidad, que permita a estudiantes y docentes desplegar proyectos de curso mediante un flujo simple (ej. git push).
- **Objetivos específicos (Diagnosticar / Diseñar / Evaluar):**
  1. Diagnosticar las necesidades de alojamiento de proyectos académicos en la comunidad universitaria (encuestas a estudiantes/profesores).
  2. Diseñar la arquitectura de la plataforma: stacks soportados, aislamiento por contenedores, límites de recursos, flujo de despliegue.
  3. Evaluar la viabilidad mediante un piloto con 2–3 materias, midiendo adopción, ahorro frente a servicios externos e incidentes de seguridad.
- **Alcance recomendado (para que sea viable en el tiempo del curso):** acotar a un set fijo de stacks (Node, Python, sitios estáticos), sin intentar replicar la totalidad de funcionalidades de un PaaS comercial. El mayor riesgo técnico es la ejecución de código de terceros (sandboxing, aislamiento, cuotas), que debe tratarse como el núcleo del capítulo de diseño.
- **Base técnica de partida:** ninguna existente; sería desarrollo nuevo, apoyado en la experiencia de despliegue/orquestación de servidores ya adquirida.

### 2. Software base de gestión administrativa para instituciones educativas

> **Título propuesto:** *"Diseño y evaluación de un sistema base de gestión administrativa, académica y financiera para instituciones de educación básica y media"*

- **Problema diagnosticado:** las instituciones educativas privadas de pequeña/mediana escala suelen gestionar inscripciones, facturación y nómina con herramientas manuales (hojas de cálculo) o sistemas genéricos no adaptados a su operación, generando errores de imputación y falta de trazabilidad.
- **Objetivo general:** diseñar y evaluar un sistema base (no atado a una institución específica) que resuelva de forma genérica y configurable los procesos de inscripción, facturación por consumo y nómina de una institución educativa tipo.
- **Objetivos específicos:**
  1. Diagnosticar los procesos administrativos comunes a instituciones educativas de escala similar (inscripciones, facturación, nómina).
  2. Diseñar un modelo de datos y una arquitectura genérica y configurable (multi-institución), separando lo específico de un caso particular de lo reutilizable.
  3. Evaluar el sistema mediante un caso de estudio simulado o anonimizado, midiendo reducción de errores de imputación y tiempo administrativo.
- **Nota importante de alcance:** este candidato se apoya en la base ya construida y probada en producción (APP-FANA), pero **se presenta ante la universidad como un software base genérico**, sin exponer datos, nombre ni detalles operativos de la institución real que lo usa hoy (es una fuente de ingreso activa, no un proyecto académico). El trabajo de grado documentaría el diseño generalizado del sistema, no el caso de uso específico.
- **Base técnica de partida:** la más madura de las tres — sistema en producción con módulos de inscripciones, facturación "por consumo", nómina y auditoría ya resueltos y validados con datos reales.

### 3. Sistema de gestión y evaluación financiera de carteras de préstamos y fondos de inversión

> **Título propuesto:** *"Diseño y evaluación de un sistema de gestión y evaluación de rentabilidad para carteras de préstamos y fondos de inversión de pequeña escala"*

- **Problema diagnosticado:** la gestión de préstamos y fondos de inversión de pequeña escala requiere trazabilidad contable, cálculo confiable de rentabilidad y controles de acceso por rol, algo que hojas de cálculo o sistemas genéricos no garantizan con integridad transaccional.
- **Objetivo general:** diseñar y evaluar un sistema que permita administrar carteras de préstamos y fondos de inversión con integridad transaccional, trazabilidad de auditoría y proyecciones de rentabilidad.
- **Objetivos específicos:**
  1. Diagnosticar los riesgos operativos y contables de la gestión manual de préstamos y fondos (sobreconteos, duplicados, reconstrucciones erróneas).
  2. Diseñar un modelo transaccional con controles de acceso por rol y bitácora de auditoría para las operaciones críticas.
  3. Evaluar el sistema mediante indicadores de rentabilidad mensual/acumulada y un simulador de proyecciones para inversionistas.
- **Ventaja particular:** es el candidato más alineado temáticamente con la bibliografía del curso (Sapag Chain trata directamente evaluación financiera de proyectos: flujo de caja, rentabilidad, factibilidad económica), lo que facilita conectar la teoría del libro con el caso práctico.
- **Nota de confidencialidad (igual que el candidato 2):** es un negocio secundario real (gestión de fondos/inversionistas propios), por lo que se presenta ante la universidad de la misma forma — como software base genérico, sin exponer cifras, identidad de fondos ni clientes reales. El trabajo de grado documenta el diseño del sistema, no el caso de uso específico.
- **Base técnica de partida:** plataforma en producción (Next.js + Supabase) con módulos de préstamos, fondos, rentabilidad, auditoría e inteligencia de negocio ya funcionando.

---

## Recomendación

Orden de preferencia sugerido, sujeto a tu decisión:

1. **Plataforma de alojamiento (PaaS institucional)** — la más original y con mayor "peso" de diseño desde cero, pero también la de mayor riesgo de alcance. Requiere acotar bien el MVP desde el primer corte.
2. **Software base de gestión administrativa** — la de menor riesgo de ejecución (ya funciona en producción), buen encaje con el marco Diagnosticar/Diseñar/Evaluar si se generaliza correctamente y se cuida la confidencialidad del caso real.
3. **Sistema financiero de préstamos/fondos** — la más alineada con la bibliografía del curso, buena opción de respaldo si la plataforma PaaS resulta demasiado ambiciosa para el cronograma.

## Pendientes

- [ ] Leer Capítulo 1 de Sapag Chain antes de la próxima clase.
- [ ] Definir con la profesora si se permite basar un proyecto en software ya existente en producción (candidatos 2 y 3), o si se exige desarrollo nuevo.
- [ ] Decidir el orden final de presentación de los tres candidatos.
- [ ] Si se elige el candidato 1, iniciar el diagnóstico (encuesta a estudiantes/profesores sobre necesidades de alojamiento).
