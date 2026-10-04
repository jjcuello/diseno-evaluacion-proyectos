# Registro de fuentes

Fuentes candidatas para el Trabajo de Grado, con su estado de verificación. **Solo se citan las marcadas como ✅ Verificada**, es decir, contrastadas con la fuente primaria. Las referencias siguen el formato del Manual del IUPSM (ver skill `tg-redaccion`).

Estados:

- ✅ **Verificada:** contrastada con la fuente primaria; los datos se pueden citar.
- 🟡 **Por verificar:** dato plausible, todavía sin fuente primaria consultada.
- ❌ **Descartada:** el dato es erróneo o la fuente no aporta.

Origen: búsqueda inicial con Gemini (nivel macro), revisada y verificada en la web el 2026-10-04.

---

## Nivel macro (mundial)

### M1. Open Education Project (OPE): cursos de Boston University migrados de AWS a la nube universitaria ✅

- **Referencia:** Shi, D. (2024, noviembre). The Open Education Project is ready to scale. *Red Hat Research Quarterly* [Revista en línea]. Disponible: https://research.redhat.com/blog/article/the-open-education-project-is-ready-to-scale/ [Consulta: 2026, octubre 4].
- **Datos verificados:**
  - En el semestre de primavera de 2024, tres asignaturas de Boston University funcionaron sobre la infraestructura del OPE en la New England Research Cloud (NERC): Computer Systems, CS 210 (más de 320 estudiantes); Introduction to Operating Systems, EC 440 (más de 70); y Tools for Data Science, CS 506 (más de 220).
  - En 2022, los cursos que corrían en OpenShift AI sobre AWS costaban "roughly $150 per student"; tras la migración a la NERC, "roughly $18 per student". Es una reducción cercana a 88 por ciento.
  - Motivos de la migración: el costo, contar con un clúster dedicado a las clases (escalabilidad y balanceo de carga) y una gestión y un monitoreo más finos, con apagado de sesiones inactivas y facturación por asignatura.
- **Uso:** capítulo I, contextualización del nivel macro. Es el **caso más cercano a este proyecto**: una universidad lleva la plataforma de sus cursos de sistemas desde una nube comercial a una infraestructura propia y reduce el costo por estudiante. También sirve como referente en la fase de alternativas de solución.
- **Advertencia:** la publicación es una revista divulgativa de Red Hat, que además es socio del proyecto, y no está arbitrada. Conviene complementarla con una fuente independiente.

### M2. New England Research Cloud (NERC) ✅

- **Referencia:** Grzybowski, A. (2023, noviembre 28). *New England Research Cloud's affordable production cloud services now available to general research and education users* [Documento en línea]. Boston University, Hariri Institute for Computing. Disponible: https://www.bu.edu/hic/2023/11/28/the-newly-openednew-england-research-cloud-will-deliver-high-end-cloud-services-at-a-fraction-of-the-cost [Consulta: 2026, octubre 4].
- **Datos verificados:**
  - La NERC es "a production cloud, operated by BU and Harvard Research IT", con máquinas virtuales, contenedores, almacenamiento S3 y una plataforma de IA como servicio.
  - Está abierta a "general research and education users".
  - Sus tarifas son "one-third to one-half the cost of the public cloud".
  - La administra la MOC Alliance, con sede en el Hariri Institute de Boston University, y se apoya en el Massachusetts Green High Performance Computing Center (MGHPCC), un consorcio de Boston University, Harvard, MIT, Northeastern y la Universidad de Massachusetts.
- **Uso:** capítulo I, nivel macro: universidades que operan su propia nube como alternativa a la nube pública, con costos menores.

### M3. Alianza Red Hat y Boston University (Mass Open Cloud) ✅

- **Referencia:** Red Hat. (2021, abril 27). *Red Hat and Boston University announce major partnership to advance open hybrid cloud research and operations at scale* [Documento en línea]. Disponible: https://www.redhat.com/es/about/press-releases/red-hat-and-boston-university-announce-major-partnership-advance-open-hybrid-cloud-research-and-operations-scale [Consulta: 2026, octubre 4].
- **Datos verificados:** Red Hat donó 551,9 millones de dólares en suscripciones de software para proyectos de nube abierta, entre ellos la Mass Open Cloud (MOC). Participan Boston University, Harvard, la Universidad de Massachusetts, el MGHPCC y el Boston Children's Hospital.
- **Uso:** capítulo I, nivel macro, como dato complementario.
- **Corrección a Gemini:** OpenShift **no nació de una investigación académica**. Es un producto de Red Hat que estas universidades **adoptaron** para su nube propia.

### M4. Fin de los planes gratuitos de Heroku ✅

- **Referencia:** Wise, B. (2022, agosto 25). *Heroku's next chapter* [Documento en línea]. Heroku. Disponible: https://www.heroku.com/blog/next-chapter/ [Consulta: 2026, octubre 4].
- **Dato verificado:** "Starting November 28, 2022, we plan to stop offering free product plans and plan to start shutting down free dynos and data services". Afectó a Heroku Dynos, Heroku Postgres y Heroku Data for Redis.
- **Uso:** capítulo I, nivel macro: los proveedores comerciales cambian sus condiciones y dejan sin alojamiento gratuito a estudiantes y docentes.

---

## Nivel meso (Latinoamérica)

Origen: búsqueda con Gemini, revisada y verificada en la web el 2026-10-04.

### L1. Nube UNAM (Universidad Nacional Autónoma de México) ✅ con corrección

- **Referencias:**
  - JLOM (2023, junio 27). *Ofrece la UNAM servicios de nube a su comunidad* [Documento en línea]. Portal TIC UNAM. Disponible: https://www.tic.unam.mx/noticias/ofrece-unam-servicios-nube-comunidad/ [Consulta: 2026, octubre 4].
  - Paz, R. (2023, agosto 14). Nube UNAM, una herramienta democratizante. *Gaceta UNAM* [Periódico en línea]. Disponible: https://www.gaceta.unam.mx/nube-unam-una-herramienta-democratizante/ [Consulta: 2026, octubre 4].
- **Datos verificados:**
  - La Dirección General de Cómputo y de Tecnologías de Información y Comunicación (DGTIC) opera una nube propia con tres servicios: Bóveda Digital, infraestructura como servicio (IaaS) y respaldo como servicio (BaaS).
  - Uno de sus fines declarados es la "reducción de costos por el uso de plataformas de empresas de tecnología".
  - Según la directora de la DGTIC, busca "disminuir la dependencia de servicios y plataformas contratados a las empresas transnacionales" (*Gaceta UNAM*).
- **Corrección a Gemini:** el servicio **no está abierto a estudiantes**. Lo solicitan las "escuelas, facultades, centros e institutos de investigación, y dependencias", a través de su responsable de TIC. Además, es IaaS y no PaaS: el estudiante no puede desplegar su proyecto por sí mismo. Esto **refuerza la brecha** que atiende este proyecto: incluso una universidad grande de la región que tiene nube propia no ofrece despliegue de autoservicio a sus estudiantes.
- **Uso:** capítulo I, nivel meso: las universidades latinoamericanas buscan reducir su dependencia de proveedores transnacionales.
- 🟡 Otra fuente sugiere un dato de uso en 2022: 22 entidades atendidas y 474 instancias IaaS. Proviene de la *Memoria UNAM 2022, DGTIC* (https://www.planeacion.unam.mx/Memoria/2022/PDF/14.3-DGTIC.pdf). No se ha verificado en el documento.

### L2. Volumen de pagos por PSE en Colombia ✅ con corrección, de utilidad limitada

- **Referencia:** Defelipe, S. (2024, agosto 5). En el primer semestre de 2024 se realizaron más de 370 millones de transacciones a través de PSE. *Impacto TIC* [Revista en línea]. Disponible: https://impactotic.co/innovacion/consumo-digital/en-el-primer-semestre-de-2024-se-realizaron-mas-de-370-millones-de-transacciones-a-traves-de-pse/ [Consulta: 2026, octubre 4].
- **Dato verificado:** más de 370 millones de transacciones en el **primer semestre** de 2024, 15 por ciento más que en el mismo período de 2023. El dato proviene de ACH Colombia.
- **Correcciones a Gemini:**
  - El período es un semestre, no un trimestre.
  - La fuente es ACH Colombia, citada por Impacto TIC, no un reporte de Pomelo.
  - La afirmación de que estos pagos "no suelen ser compatibles" con las consolas de los proveedores de nube **no tiene respaldo** en la fuente.
- **Uso:** limitado. Muestra que en la región dominan los pagos locales, pero no prueba la barrera para contratar servicios de nube. Hace falta una fuente que lo demuestre directamente.

### L3. Reporte de Pomelo "Pagos digitales y E-commerce en América Latina" (2024) 🟡

No se localizó en la verificación. No citar hasta encontrar el documento original.

### L4. Lo que Gemini declaró no poder respaldar

Gemini no encontró fuentes para:

- el porcentaje de estudiantes de la región sin acceso a la nube por no tener tarjeta internacional;
- el gasto promedio del estudiante en servidores para sus proyectos.

**Esto es útil para el trabajo:** si no hay datos regionales, el **diagnóstico de campo** del objetivo específico 1 (la encuesta a estudiantes del Politécnico) es lo que generará ese dato. Así se justifica la investigación de campo en el capítulo III.

**Pista para respaldar la barrera de pago:** el Banco Mundial publica la base *Global Findex* (2021), con datos de tenencia de tarjetas de crédito por país. Está pendiente de consultar.

---

## Nivel micro (Venezuela)

Origen: búsqueda con Gemini (barreras de pago) y búsqueda propia, verificadas en la web el 2026-10-04.

### V1. Conectividad y electricidad en Venezuela (Freedom House, 2024) ✅

- **Referencia:** Freedom House (2024). *Freedom on the Net 2024: Venezuela* [Documento en línea]. Disponible: https://freedomhouse.org/country/venezuela/freedom-net/2024 [Consulta: 2026, octubre 4].
- **Datos verificados** (período del 1 de junio de 2023 al 31 de mayo de 2024):
  - La velocidad mediana de banda ancha móvil ocupó el puesto 138 de 147 países, según Ookla: 12,17 Mbps de bajada en móvil y 53,90 Mbps de bajada en conexión fija (mayo de 2024).
  - "22 of Venezuela's 23 states undergo daily electricity rationing due to a lack of generation capacity". En marzo de 2024, los apagones interrumpieron internet en al menos ocho estados.
  - Más de 70 por ciento de los planes de internet relevados cuestan entre 4,44 y 56,22 veces el salario mínimo mensual.
  - Una encuesta de 2023 estimó que solo 48 por ciento de los hogares tenía acceso a internet. Según datos oficiales de 2022, la penetración superaba 70 por ciento solo en el Distrito Capital y Miranda, y era menor de 30 por ciento en siete de 23 estados.
- **Uso:** capítulo I, nivel micro: la conexión es lenta y costosa, lo que dificulta depender de servicios remotos. Una plataforma alojada en el propio Politécnico permite que los despliegues y las revisiones dentro del campus usen la red local.
- **⚠️ Implicación para el diseño (documento técnico):** el racionamiento eléctrico también es un **riesgo para el propio clúster** alojado en el Politécnico. Hay que tratarlo de forma explícita: autonomía del UPS, apagado ordenado, arranque automático de los servicios y disponibilidad medida durante el piloto. Ignorarlo debilitaría el estudio de factibilidad técnica ante el jurado.

### V2. Situación de las universidades venezolanas (ODHULA, 2023) ✅

- **Referencia:** Observatorio de Derechos Humanos de la Universidad de Los Andes, ODHULA (2023, agosto). *Situación de las universidades venezolanas: reporte mensual, agosto 2023* [Documento en línea]. Disponible: https://www.uladdhh.org.ve/wp-content/uploads/2023/09/8.-Reporte-agosto-2023-Situacion-de-las-Universidades-Venezolanas.pdf [Consulta: 2026, octubre 4].
- **Datos verificados:**
  - Documenta la "asfixia presupuestaria" y el deterioro de la infraestructura universitaria por falta de mantenimiento e inversión.
  - Recoge la denuncia de un consejero de la ULA sobre cortes de electricidad de entre tres y diez horas en Mérida, que dificultan las clases virtuales.
  - Señala que en un núcleo de la Universidad de Oriente los estudiantes no cuentan con computadoras para investigar.
- **Uso:** capítulo I, nivel micro: las universidades venezolanas tienen poca capacidad de inversión en tecnología. Esto justifica una solución de bajo costo, con equipos existentes y software libre.
- **Advertencia:** es un reporte de una ONG universitaria que compila denuncias de prensa. Es adecuado para el contexto, pero las cifras deben atribuirse a su fuente original.

### V3. Límites de pago internacional con tarjetas venezolanas ✅ dato parcial

- **Referencia:** Flores, J. (2024, abril 27). Bancamiga aumentó los límites de su tarjeta de débito: estos son los montos. *El Diario* [Periódico en línea]. Disponible: https://eldiario.com/2024/04/27/bancamiga-limites-tarjeta-de-debito/ [Consulta: 2026, octubre 4].
- **Dato verificado:** el límite diario de la tarjeta de débito es de 500 dólares para consumos en el país y de **200 dólares en el extranjero**.
- **Matiz importante:** existen tarjetas prepagadas o en divisas para comprar en el exterior y pagar suscripciones, por ejemplo la tarjeta prepagada internacional del Banco de Venezuela (pendiente de verificar). Por lo tanto, **pagar desde Venezuela no es imposible**: exige tener divisas y un producto bancario específico, y está sujeto a límites.
- **Uso:** capítulo I, nivel micro, con prudencia. Conviene formularlo como un costo y una fricción adicionales para el estudiante, no como una imposibilidad.

### V4. Lo que trajo Gemini sobre la OFAC y el SWIFT ❌ como está formulado

- **Afirmación:** las sanciones de la OFAC y los bancos locales impiden que un estudiante pague servicios como AWS; algunos bancos solo emiten SWIFT para montos mayores de 5.000 dólares.
- **Verificación:**
  - El programa de sanciones de la OFAC sobre Venezuela (31 C.F.R. parte 591) se dirige al **Gobierno de Venezuela, a PDVSA, al Banco Central y a personas designadas** en la lista SDN. **No prohíbe** que un ciudadano común pague servicios en el extranjero. Las dificultades reales vienen del sistema bancario y del exceso de cumplimiento de terceros, que no está documentado en una fuente citable.
  - El dato de los 5.000 dólares viene de foros de usuarios: **no es citable** en un trabajo de grado.
- **Decisión:** no usar. Si se quiere argumentar la barrera de pago, usar V3 junto con un estudio formal sobre la bancarización en Venezuela (pendiente de buscar).

### V5. Antecedentes venezolanos 🟡 sin resultados en línea

La búsqueda en la web no arrojó trabajos de grado venezolanos de 2023 en adelante sobre contenedores o plataformas de despliegue. Muchos repositorios venezolanos no están bien indexados. Opciones:

- Consultar la biblioteca y la Coordinación de Trabajo de Grado del propio I.U.P.S.M. (la Coordinación lleva el registro de los trabajos aprobados, según el art. 17 del Reglamento).
- Buscar directamente en los repositorios de la UCAB, la USB, la UCV (Saber UCV), la UNET, la URBE, la ULA y la UNEXPO.

### V6. Cinco "tesis venezolanas" que trajo Gemini ❌ no verificables: tratarlas como inventadas

Gemini listó cinco trabajos con título, autor y año, pero **ninguno con enlace**, y dio una excusa distinta para cada uno ("requiere sesión", "sin URL estática", etc.). Se buscó cada título exacto, entre comillas, el 2026-10-04, y **ninguno aparece en la web**:

| Título según Gemini | Autor según Gemini | Universidad | Resultado |
|---|---|---|---|
| Diseño e implementación de una infraestructura en la nube para la gestión y despliegue de servicios informáticos educativos | Carlos Eduardo Mendoza (2021) | UCV | Sin coincidencias |
| Plataforma de orquestación de contenedores basada en Docker y Kubernetes para el despliegue automatizado de aplicaciones web | Gabriel Alejandro Rodríguez (2022) | UCAB | Sin coincidencias |
| Propuesta de migración de servidores institucionales a plataformas de virtualización y microservicios… | José Luis Morales Santander (2022) | URBE | Sin coincidencias |
| Automatización del despliegue de infraestructura y aplicaciones web mediante Docker en entornos académicos y de laboratorio | Andrea Valentina Colmenares (2023) | USB | Sin coincidencias |
| Evaluación de desempeño en la virtualización de servidores e implementación de servicios institucionales para estudiantes… | Ricardo José Fernández (2023) | ULA | Sin coincidencias |

Hay señales típicas de referencias inventadas por una IA:

- Los títulos son demasiado ajustados al tema pedido.
- Los nombres de los autores son genéricos.
- No hay ningún enlace verificable.
- La falta de enlace se justifica de forma distinta en cada caso.

**Decisión:** **no citar ninguna**. Citar una tesis inexistente es fraude científico por "citas bibliográficas erróneas" (Reglamento 2025, art. 96). Solo se reconsiderarán si el usuario encuentra el documento en el repositorio de la universidad.

### V7. Hallazgos reales de la verificación

- **Saber UCV:** Medina, F. (2015). *Diseño e implementación de una estrategia basada en las mejores prácticas para la virtualización de servidores de una organización*. Trabajo de pregrado, Universidad Central de Venezuela. Disponible: https://saber.ucv.ve/jspui/handle/10872/9344 [Consulta: 2026, octubre 4].
  - ✅ El trabajo existe, pero es de 2015: **queda fuera del límite de antecedentes**. Como mucho, sirve como referencia histórica de la virtualización en Venezuela.
- **Universidad de las Ciencias Informáticas (Cuba), 2024:** hay un trabajo de diploma sobre la automatización del despliegue con Docker en el repositorio de la UCI (https://repositorio.uci.cu/handle/123456789/10898). 🟡 El repositorio bloqueó la descarga y faltan el título, el autor y el contenido. Si se confirma, serviría como antecedente latinoamericano de 2024.

---

## Bases teóricas (capítulo II)

### T1. Firecracker: virtualización ligera (microVM) ✅

- **Referencia:** Agache, A., Brooker, M., Florescu, A., Iordache, A., Liguori, A., Neugebauer, R., Piwonka, P. y Popa, D. M. (2020). Firecracker: Lightweight virtualization for serverless applications. En *17th USENIX Symposium on Networked Systems Design and Implementation (NSDI 20)*. USENIX Association. Disponible: https://www.usenix.org/conference/nsdi20/presentation/agache [Consulta: 2026, octubre 4].
- **Datos verificados:** es un monitor de máquinas virtuales (VMM) de código abierto, especializado en cargas *serverless* pero útil también para contenedores. Lo usan AWS Lambda y AWS Fargate, con millones de cargas en producción.
- **Corrección a Gemini:** **no es de la Universidad de Washington**. Todos los autores son de Amazon Web Services.
- **Uso:** bases teóricas sobre aislamiento: contenedores frente a microVM. Justifica por qué el proyecto usa contenedores con políticas de seguridad y deja las microVM fuera del alcance. Al ser de 2020, cumple el límite de 10 años para bases teóricas.
- **Pendiente:** confirmar las páginas en las actas para la referencia completa.

---

## Reseña histórica (capítulo II, Proyecto Factible)

Estas fuentes tienen más de 10 años, así que solo sirven para la reseña histórica, no para las bases teóricas.

### H1. Apache Mesos (UC Berkeley) 🟡

- Hindman, B. et al. (2011). *Mesos: A platform for fine-grained resource sharing in the data center*. NSDI 11.
- Corrección a Gemini: el laboratorio es el **AMPLab** de UC Berkeley, no el "AMPData Lab".
- Uso: hito histórico de la orquestación de recursos previo a Kubernetes.
- Falta verificarla con la fuente primaria.

### H2. MirageOS y los unikernels (Universidad de Cambridge) 🟡

- Madhavapeddy, A. et al. (2013). *Unikernels: Library operating systems for the cloud*. ASPLOS 2013.
- Uso: enfoque alternativo de despliegue (unikernels frente a contenedores).
- Falta verificarla con la fuente primaria.

---

## Descartadas

### D1. Ray y Anyscale (UC Berkeley) ❌

Es un *framework* de cómputo distribuido para IA, no una plataforma de despliegue de aplicaciones web. No aporta al problema ni a la solución.

---

## Antecedentes de la investigación (capítulo II)

El Manual exige **al menos tres**, de 2021 en adelante, ordenados del más reciente al más antiguo, y con lo que cada uno aporta. Los siguientes se verificaron leyendo la portada y la introducción del documento original.

> **Ojo con la vigencia:** el límite se cuenta desde la fecha de entrega. Si la propuesta se presenta en 2027, los trabajos de 2022 quedan en el límite. Conviene sumar antecedentes de 2023 en adelante, sobre todo venezolanos (nivel micro).

### A1. PUCE Ibarra (Ecuador, 2024): Kubernetes en la unidad de TI de una universidad ✅

- **Referencia:** Sánchez Villacis, D. A. (2024). *Infraestructura kubernetes para implementación de aplicaciones en contenedores en entorno de pruebas en la Unidad de Tecnologías de la Información de la PUCE-Ibarra*. Trabajo de titulación de pregrado, Pontificia Universidad Católica del Ecuador, Ibarra. Disponible: https://repositorio.puce.edu.ec/handle/123456789/44584 [Consulta: 2026, octubre 4].
- **Resumen:** implementó una infraestructura de Kubernetes en la unidad de TI de la universidad, en cuatro etapas: planificación, desarrollo del entorno, pruebas de validación y traspaso al departamento de TI. Concluye que mejora la gestión de las aplicaciones en contenedores, con beneficio para el personal de TI, los docentes y los estudiantes.
- **Aporte:** confirma la factibilidad técnica de Kubernetes dentro de una universidad latinoamericana y ofrece un modelo de fases de implantación y de traspaso institucional, aplicable al estudio organizacional.
- **Pendiente:** el nombre del tutor, que no aparece en la ficha.

### A2. Universidad Técnica del Norte (Ecuador, 2022): el problema más parecido al de este proyecto ✅

- **Referencia:** Correa Cuvi, W. J. (2022). *Estudio de la plataforma Kubernetes para la administración automática de contenedores Docker en la facultad FICA de la Universidad Técnica del Norte*. Trabajo de grado de Ingeniería en Sistemas Computacionales, Universidad Técnica del Norte, Ibarra. Tutor: MSc. Xavier Mauricio Rea Peñafiel. Disponible: https://repositorio.utn.edu.ec/bitstream/123456789/12301/2/04%20ISC%20613%20TRABAJO%20GRADO.pdf [Consulta: 2026, octubre 4].
- **Problema que plantea (casi idéntico al de este proyecto):** las carreras de Sistemas y de Software llevan a producción los proyectos web de sus materias, pero el servidor de virtualización de la facultad está saturado y "los estudiantes actualmente presentan restricciones al momento de acceder a la plataforma de virtualización debido a la creciente demanda".
- **Objetivos específicos:** (a) definir una base teórica sobre Docker y Kubernetes; (b) implementar Kubernetes con minikube para prácticas en entornos locales; (c) validar los resultados midiendo la satisfacción del usuario con el cuestionario CSUQ.
- **Aporte:** respalda el problema desde otra universidad de la región. Además, su instrumento de validación, el CSUQ (*Computer System Usability Questionnaire*), es estandarizado y podría adoptarse en la encuesta de satisfacción posterior al piloto (objetivo específico 3).
- **Diferencia que justifica este proyecto:** usa minikube, es decir, un solo nodo en un entorno local. Este proyecto propone un clúster de varios nodos en producción, con aislamiento por usuario y despliegue automático desde el repositorio.

### A3. PUCE Quito (Ecuador, 2022): diseño de una plataforma de despliegue con software libre (maestría) ✅

- **Referencia:** Malla, G. (2022). *Estudio y diseño de una solución para el despliegue de aplicaciones con opciones de software libre basado en contenedores (Kubernetes)*. Trabajo de titulación de Maestría en Tecnologías de Información, Pontificia Universidad Católica del Ecuador, Quito. Director: Mgtr. Charles Escobar.
- **Contenido verificado:** tiene una estructura metodológica clásica: planteamiento del problema; marco teórico (Docker, Kubernetes, Rancher, HAProxy); marco metodológico con tipo y diseño de investigación, técnicas e instrumentos; y un capítulo IV de levantamiento de requerimientos y diseño de un modelo con conmutación por error y monitoreo.
- **Aporte:** es un modelo de cómo presentar una solución de despliegue con Kubernetes bajo un marco metodológico formal, útil para el capítulo III. También sirve como referente en la comparación de alternativas (Rancher).
- **Pendiente:** el enlace estable del repositorio. Se consultó el PDF, pero falta la URL del registro.

### A4. Escuela Politécnica Nacional (Ecuador, 2022): servidor web con *hosts* virtuales en Kubernetes ✅ complementario

- **Referencia:** Montes Bravo, J. D. (2022). *Implementación de un prototipo de un servidor web con hosts virtuales mediante Kubernetes*. Trabajo de integración curricular de Tecnólogo Superior en Redes y Telecomunicaciones, Escuela Politécnica Nacional, Quito. Director: Fernando Vinicio Becerra Camacho. Disponible: https://bibdigital.epn.edu.ec/bitstream/15000/23057/1/CD%2012476.pdf [Consulta: 2026, octubre 4].
- **Aporte:** el enrutamiento de varios sitios por nombre de dominio sobre Kubernetes, equivalente a los subdominios por aplicación de este proyecto.
- **Limitación:** es de **nivel tecnólogo**. El Manual menciona trabajos de ingeniero, arquitecto o magíster, así que úsalo solo como complemento, no entre los tres obligatorios.

### Descartado

- **Tesis de la ESPOCH sobre Kubernetes y VMware Tanzu (Gemini):** ❌ no se localizó. Gemini dio solo la dirección del repositorio, sin título ni autor. Además, según su propia descripción, el contexto era empresarial ("sucursal Riobamba"), no universitario.
- **UTPL (2020), JupyterHub sobre Kubernetes:** queda fuera del límite de 5 años.
