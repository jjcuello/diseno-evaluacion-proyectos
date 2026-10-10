# Instrucciones para agentes

Este repositorio contiene el Trabajo de Grado de Ingeniería de Sistemas en el Instituto Universitario Politécnico "Santiago Mariño" (I.U.P.S.M.). El título es *"Plataforma web institucional de alojamiento y despliegue continuo (PaaS) para el Politécnico Santiago Mariño"*. Se trabaja todo en **español**.

## Documentos y destinatarios

| Archivo | Destinatario | Contenido |
|---|---|---|
| `Documento-Metodologico.md` | Tutor metodológico | Propuesta según el Manual y el Reglamento: capítulos I a III, cronograma y referencias. Empieza en el capítulo I; la portada y el índice los agrega el script |
| `Propuesta-Corta.md` | Tutor metodológico | Línea de investigación, modalidad y estructura. Nombre provisional: probablemente es el Protocolo de Investigación |
| `Documento-Tecnico.md` | Tutor técnico | Arquitectura, seguridad, cronograma técnico, indicadores y factibilidad |
| `README.md` | Ambos | Datos de la asignatura, orientaciones del docente y pendientes |

Los PDF, el Word y la página HTML se generan con `generar_documentos.py`; no se editan a mano. El documento metodológico tiene una sola versión, `Documento-Metodologico.pdf` y `.docx`, con el formato del Manual.

## Skills: léelos antes de trabajar

Están en `.claude/skills/<nombre>/SKILL.md`. Claude Code los carga automáticamente; **otros agentes deben leer el archivo correspondiente antes de actuar**.

| Skill | Cuándo usarlo |
|---|---|
| `tg-estructura` | Crear o reorganizar capítulos, secciones, el índice, el resumen o las páginas preliminares |
| `tg-redaccion` | Redactar o corregir texto, citas, referencias, cuadros, figuras o el formato |
| `tg-reglamento` | Plazos, entregas, evaluación, tutor, jurado, aval y faltas |
| `tg-revision` | Revisar un borrador como lo haría el tutor metodológico |

## Decisiones vigentes del proyecto

- **Línea de investigación (decidida):** Sistemas de Comunicación → Transmisión de Datos → **Virtualización**. Como área complementaria, Seguridad de Datos. El aval formal del coordinador llega con el protocolo.
- **Calendario:** la materia todavía no está inscrita; el trabajo se adelanta. No ajustar fechas al Reglamento hasta que el usuario lo indique.
- **Referencias:** los PDF originales (Manual, Reglamento, esquema por naturaleza, líneas de investigación) van en `referencias/`. Si existen, consúltalos para verificar lo que resumen los skills.
- **Modalidad (propuesta):** **Proyecto Factible**, apoyado en una investigación de campo y documental. La alternativa es Investigación Tecnológica. Está por confirmar con el tutor metodológico.
- **Objetivos vigentes:** general «Diseñar una plataforma web institucional de alojamiento y despliegue continuo (PaaS) para el Politécnico Santiago Mariño»; específicos: Diagnosticar las necesidades…, Definir la arquitectura…, Evaluar la factibilidad técnica, operativa y económica… El alcance llega hasta la demostración de factibilidad, sin piloto. Sede: Extensión Caracas.
- **Orientaciones del docente:** el título no lleva verbos; el objetivo general es el título en infinitivo con un solo verbo; hay tres objetivos específicos (Diagnosticar, Diseñar, Evaluar); el problema se estudia en los niveles macro, meso y micro. El detalle está en `README.md`.
- **Foco actual:** solo el capítulo I del documento metodológico, hasta que lo evalúen y aprueben. El documento técnico se ajusta cuando lo lea el profesor.
- **Instrumento de evaluación:** `referencias/FOR-INVP-009.docx`, con cuatro momentos evaluativos (problema, marco referencial, marco metodológico y aspectos administrativos). Úsalo como lista de control; el skill `tg-revision` resume sus criterios.
- **Prioridad de normas:** Reglamento 2025, luego el Manual 5ª ed. (2015), luego las orientaciones del docente; ante una contradicción, se le pregunta al usuario.

## Registro de fuentes

`investigacion/fuentes.md` lista las fuentes candidatas con su estado. **Solo se citan las marcadas como ✅ Verificada.** Toda fuente nueva, incluidas las que provengan de Gemini u otra IA, se registra ahí antes de usarla.

## Reglas para cualquier agente

1. **No inventar fuentes, datos ni antecedentes.** Si falta una fuente real, deja `[FUENTE PENDIENTE: …]` y anótalo en los pendientes del README. El Reglamento sanciona el plagio y las citas erróneas como fraude científico.
2. No cambiar el título, los objetivos, la línea ni la modalidad sin que el usuario lo pida; cambiarlos sin solicitarlo es una falta grave (Reglamento, art. 106).
3. Mantener la coherencia entre los dos documentos: si cambia un objetivo o una fase en uno, se actualiza el otro.
4. No hacer commit ni push sin que el usuario lo pida.
