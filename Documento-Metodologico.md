# Plataforma web institucional de alojamiento y despliegue continuo (PaaS) — Documento metodológico

> Documento dirigido al **tutor metodológico**. Desarrolla el trabajo de grado según el *Manual para la Elaboración del Trabajo de Grado* (5ª ed., 2015) y el *Reglamento de Trabajo de Grado* (2025) del Politécnico Santiago Mariño. El detalle técnico de la solución está en el [documento técnico](Documento-Tecnico.md).

## Línea de investigación

**Línea elegida:** Sistemas de Comunicación → Transmisión de Datos → **Virtualización**, con Seguridad de Datos como área complementaria.

La plataforma ejecuta los proyectos de los estudiantes en contenedores orquestados sobre un clúster propio. Esa virtualización a nivel de sistema operativo es el núcleo técnico del trabajo. El aislamiento entre usuarios (políticas de red, cuotas y contenedores sin privilegios) corresponde a Seguridad de Datos, una rama hermana dentro de la misma línea matriz.

*El aval formal corresponde al coordinador de línea de investigación al evaluar el protocolo (Reglamento, art. 22).*

## Modalidad de la investigación

**Propuesta:** Proyecto Factible, apoyado en una investigación de campo (diagnóstico en el Politécnico) y documental.

El manual define el proyecto factible como "la propuesta de un modelo funcional viable … con el objeto de satisfacer necesidades de entes específicos" e incluye expresamente los proyectos de sistema y de software. Además, exige demostrar la rentabilidad técnica, económica y operativa, lo que coincide con el objetivo específico 3 y con el enfoque de Sapag Chain de la asignatura. Sus tres fases corresponden a los objetivos específicos: diagnóstico (OE1), alternativas de solución y propuesta (OE2) y estudio de factibilidad (OE3).

La alternativa es la Investigación Tecnológica, si el tutor prefiere que el aporte central sea la construcción y validación del prototipo (capítulo IV, "Ingeniería del Proyecto").

*Por confirmar con el tutor metodológico.*

## Estructura de la propuesta

Según el esquema de Proyecto Factible: introducción; capítulo I, El Problema; capítulo II, Marco Referencial; capítulo III, Marco Metodológico; cronograma, referencias y anexos.

> **Convenciones de este borrador.** Los marcadores entre corchetes indican información que falta y que **no debe inventarse**:
> - `[DIAGNÓSTICO: …]`: dato del Politécnico que se obtendrá en la fase de diagnóstico o que debe aportar el autor.
> - `[PENDIENTE: …]`: dato administrativo por definir.
> - `[FUENTE PENDIENTE: …]`: afirmación que necesita respaldo bibliográfico.
>
> Todas las fuentes citadas están verificadas en `investigacion/fuentes.md`.

---

## CAPÍTULO I. EL PROBLEMA

### Contextualización del Problema

#### Nivel macro: el contexto mundial

La formación de profesionales en el área de la informática exige que los estudiantes no se limiten a escribir programas, sino que los publiquen y los mantengan en funcionamiento en internet, tal como ocurrirá en su ejercicio profesional. Una vía frecuente para cubrir esa necesidad son las plataformas comerciales de alojamiento y despliegue, conocidas como plataforma como servicio o *Platform as a Service* (PaaS). Estas plataformas permiten al usuario publicar una aplicación sin administrar los servidores que la sostienen. Su ventaja técnica es evidente; sin embargo, convierte a estudiantes y docentes en usuarios dependientes de las condiciones comerciales de empresas privadas, que pueden modificarlas en cualquier momento.

Un caso que ilustra esa dependencia es el de Heroku, una plataforma de este tipo que ofrecía planes de uso gratuito. En agosto de 2022, la empresa anunció que a partir del 28 de noviembre de ese año dejaría de ofrecer sus planes gratuitos de cómputo, de bases de datos Postgres y de almacenamiento Redis, y que comenzaría a desactivar los servicios que funcionaban bajo esa modalidad (Wise, 2022). Con esa decisión, las aplicaciones alojadas sin costo, entre ellas los proyectos académicos, quedaron sin soporte, y sus autores debieron migrarlas, pagar una suscripción en moneda extranjera o abandonarlas. El hecho muestra que la gratuidad de estos servicios no constituye una garantía, sino una condición comercial revocable.

Frente a ese escenario, algunas universidades han optado por operar su propia infraestructura en la nube. En el estado de Massachusetts, Estados Unidos, la Universidad de Boston y la Universidad de Harvard operan la New England Research Cloud (N.E.R.C.), una nube de producción que ofrece máquinas virtuales, contenedores y almacenamiento a la comunidad de investigación y docencia. Sus tarifas se ubican entre un tercio y la mitad del costo de la nube pública (Grzybowski, 2023). Su administración está a cargo de la alianza de la Mass Open Cloud, una iniciativa de nube abierta con sede en la Universidad de Boston. En 2021, la empresa Red Hat le donó suscripciones de *software* valoradas en 551,9 millones de dólares (Red Hat, 2021).

El resultado más relevante para esta investigación proviene de la experiencia docente de esa misma universidad. Según una publicación de divulgación de Red Hat, empresa asociada al proyecto (Shi, 2024), en 2022 los cursos de sistemas computacionales de la Universidad de Boston que funcionaban sobre una plataforma comercial alojada en Amazon Web Services costaban aproximadamente 150 dólares por estudiante. Tras su traslado a la nube universitaria, el costo descendió a cerca de 18 dólares por estudiante, una reducción cercana a 88 por ciento (cálculo propio). En el semestre de primavera de 2024, esa infraestructura sostuvo tres asignaturas con más de 600 estudiantes en conjunto. Los motivos declarados del traslado fueron la reducción del costo, la disponibilidad de un clúster dedicado a las clases y un mayor control sobre la gestión del servicio.

#### Nivel meso: el contexto latinoamericano

En América Latina, la tendencia a reducir la dependencia de los proveedores transnacionales también se manifiesta en las instituciones de educación universitaria. La Universidad Nacional Autónoma de México (U.N.A.M.) opera una infraestructura propia en la nube, la Nube UNAM, administrada por su Dirección General de Cómputo y de Tecnologías de Información y Comunicación. Según su directora, el propósito de este servicio es disminuir la dependencia de las plataformas contratadas a empresas transnacionales (Paz, 2023). No obstante, el servicio está dirigido a escuelas, facultades, institutos y dependencias, y no a los estudiantes de forma individual. Ello revela que, incluso en una de las universidades de mayor tamaño de la región, la nube institucional no ofrece al estudiante un medio de autoservicio para publicar sus propios proyectos.

Por su parte, la literatura académica regional registra el mismo problema en el plano de la formación en informática. Correa (2022) documenta que en la Facultad de Ingeniería en Ciencias Aplicadas de la Universidad Técnica del Norte, en Ecuador, las carreras de Sistemas y de *Software* necesitan llevar a producción los proyectos web elaborados en sus asignaturas. Sin embargo, el servidor de virtualización de la facultad se encuentra saturado, y los estudiantes enfrentan restricciones para acceder a él debido a la creciente demanda. La coincidencia entre ese diagnóstico y la situación que motiva esta investigación sugiere que se trata de una carencia compartida por instituciones de la región, y no de un caso aislado.

A lo anterior se suma una barrera económica que no ha sido cuantificada. Las plataformas comerciales de alojamiento facturan en dólares estadounidenses y exigen medios de pago internacionales. Sin embargo, no se dispone de estudios regionales que midan cuántos estudiantes universitarios quedan excluidos de estos servicios por carecer de dichos medios, ni cuánto destinan de sus propios recursos a mantener sus proyectos en línea `[FUENTE PENDIENTE: datos de tenencia de tarjetas de crédito en la región, Global Findex del Banco Mundial]`. Esta ausencia de datos justifica que la presente investigación obtenga información primaria mediante un diagnóstico de campo.

#### Nivel micro: el contexto venezolano y el Instituto Universitario Politécnico "Santiago Mariño"

En Venezuela, las limitaciones descritas se agravan por las condiciones de la infraestructura nacional. De acuerdo con Freedom House (2024), en mayo de 2024 la velocidad mediana de la banda ancha móvil del país ocupó el puesto 138 entre 147 naciones evaluadas. El mismo informe señala que 22 de los 23 estados del país estaban sometidos a racionamiento eléctrico diario, y que más de 70 por ciento de los planes de acceso a internet relevados costaba entre 4,44 y 56,22 veces el salario mínimo mensual. Una encuesta de 2023 citada en ese informe estimó que solo 48 por ciento de los hogares tenía acceso a internet. En consecuencia, depender de servicios alojados en el exterior implica para el estudiante venezolano un costo y una inestabilidad mayores que para sus pares de otras regiones.

Las instituciones de educación universitaria del país tampoco disponen de holgura financiera para atender estas necesidades. El Observatorio de Derechos Humanos de la Universidad de Los Andes (O.D.H.U.L.A., 2023) documenta la insuficiencia presupuestaria de las universidades venezolanas, el deterioro de sus instalaciones por falta de mantenimiento e inversión, y denuncias de estudiantes afectados por cortes eléctricos de entre tres y diez horas que dificultan sus actividades académicas. En ese contexto, cualquier solución tecnológica dirigida a la comunidad universitaria debe caracterizarse por un bajo costo de adquisición y de operación, y por aprovechar los recursos de los que ya dispone la institución.

En el plano del pago de servicios en el exterior, la banca venezolana ofrece productos para consumos internacionales, pero con montos restringidos. A modo de ejemplo, una entidad bancaria nacional fijó en 2024 un límite diario de 200 dólares para los consumos en el extranjero con su tarjeta de débito (Flores, 2024). Por consiguiente, contratar un servicio de alojamiento en el exterior no resulta imposible para el estudiante, pero sí le exige disponer de divisas y de un producto bancario específico. Para quien solo maneja una cuenta en bolívares, ello constituye una fricción adicional.

Este es el contexto en el que se ubica el Instituto Universitario Politécnico "Santiago Mariño" (I.U.P.S.M.), específicamente en su Extensión Caracas. En la carrera de Ingeniería de Sistemas, los estudiantes desarrollan en distintas asignaturas aplicaciones web y otros proyectos de *software* que, para ser evaluados en condiciones reales, deben publicarse en internet. Hasta donde ha podido observar el autor, el Instituto no cuenta con un servicio propio que permita a estudiantes y docentes alojar y desplegar esos proyectos, por lo cual cada estudiante resuelve la publicación por su cuenta. Para ello recurre a cuentas personales en plataformas comerciales externas, sujetas a las restricciones de pago, de costo y de conectividad descritas `[DIAGNÓSTICO: confirmar con datos de la encuesta a estudiantes y de la entrevista al departamento de tecnología]`.

#### Causas del problema

A partir de la situación descrita, se identifican como causas principales del problema: (a) la ausencia en el Instituto de una infraestructura propia destinada al alojamiento y despliegue de los proyectos académicos; (b) la dependencia de plataformas comerciales extranjeras, cuyas condiciones de uso y de gratuidad pueden cambiar sin previo aviso; (c) las restricciones para efectuar pagos internacionales desde el sistema bancario venezolano; y (d) las limitaciones presupuestarias de las instituciones universitarias del país para adquirir servicios en la nube pública.

#### Consecuencias del problema

Entre las consecuencias que se derivan de esta situación destacan las siguientes. En primer lugar, los proyectos alojados en cuentas personales o en planes gratuitos tienden a perderse cuando dichas cuentas vencen o cuando el proveedor modifica sus condiciones `[DIAGNÓSTICO: frecuencia de pérdida de proyectos]`. En segundo lugar, los estudiantes invierten tiempo en configurar despliegues de forma manual, en lugar de dedicarlo al aprendizaje propio de la asignatura `[DIAGNÓSTICO: horas dedicadas a desplegar]`. Asimismo, los docentes carecen de un punto único desde el cual revisar las versiones publicadas de los proyectos que evalúan. Por último, se produce una desigualdad de condiciones entre los estudiantes que pueden pagar servicios en divisas y los que no pueden hacerlo.

#### Pronóstico

De mantenerse esta situación, el Instituto continuará dependiendo de proveedores externos sobre los cuales no ejerce ningún control, y la publicación de los proyectos académicos seguirá condicionada a la capacidad de pago de cada estudiante. Las experiencias reseñadas indican que las condiciones de gratuidad de estos servicios pueden desaparecer sin previo aviso (Wise, 2022). Por ello, es previsible que una parte de la producción académica de los estudiantes siga perdiéndose al cierre de cada período, sin quedar disponible como evidencia de aprendizaje ni como base para trabajos posteriores.

#### Delimitación

- **Espacial:** el Instituto Universitario Politécnico "Santiago Mariño", Extensión Caracas, y la carrera de Ingeniería de Sistemas, específicamente las asignaturas de programación y desarrollo de *software*.
- **Temporal:** `[PENDIENTE: período académico en que se ejecutará la investigación, una vez inscrita la asignatura]`.
- **Temática:** el diseño y la evaluación de factibilidad de una plataforma de alojamiento y despliegue continuo basada en la virtualización por contenedores. Se enmarca en la línea de investigación Sistemas de Comunicación, área Transmisión de Datos, sublínea Virtualización, con Seguridad de Datos como área complementaria.
- **Población:** los estudiantes y docentes de las asignaturas de programación y desarrollo de *software* de la carrera y el personal del departamento de tecnología del Instituto.

#### Formulación del Problema

En atención a lo expuesto, se formula la siguiente interrogante general: ¿En qué medida es factible, desde los puntos de vista técnico, operativo y económico, una plataforma institucional de alojamiento y despliegue continuo que permita a estudiantes y docentes del Instituto Universitario Politécnico "Santiago Mariño" publicar sus proyectos académicos sin depender de servicios externos de pago?

De ella se desprenden las siguientes interrogantes específicas:

1. ¿Cuáles son las necesidades de alojamiento y despliegue de proyectos académicos de los estudiantes y docentes del Instituto?
2. ¿Qué arquitectura debe tener una plataforma que atienda esas necesidades con aislamiento entre usuarios y límites de recursos?
3. ¿Es factible, en lo técnico, lo operativo y lo económico, la implantación de dicha plataforma en el Instituto?

### Objetivos de la Investigación

La investigación se orientará al logro de los siguientes objetivos.

#### Objetivo General

Diseñar una plataforma web institucional de alojamiento y despliegue continuo (PaaS) para el Politécnico Santiago Mariño.

#### Objetivos Específicos

1. Diagnosticar las necesidades de alojamiento y despliegue de proyectos académicos de los estudiantes y docentes del Politécnico Santiago Mariño.
2. Definir la arquitectura de la plataforma web de alojamiento y despliegue continuo, con aislamiento por contenedores y límites de recursos.
3. Evaluar la factibilidad técnica, operativa y económica de la plataforma.

### Justificación de la Investigación

Desde el punto de vista **práctico**, la investigación responde a una necesidad concreta de la comunidad del Instituto: contar con un medio propio, estable y sin costo para el estudiante, para publicar los proyectos que desarrolla en sus asignaturas. La plataforma propuesta permitiría a los estudiantes desplegar sus aplicaciones desde su repositorio de código y a los docentes revisar las versiones publicadas desde un punto único. Además, conservaría los proyectos al cierre de cada período académico, en lugar de dejarlos expuestos a la expiración de cuentas personales.

En el plano **económico**, el estudio se apoya en el enfoque de la preparación y evaluación de proyectos. Para Sapag y Sapag (2000), un proyecto "no es ni más ni menos que la búsqueda de una solución inteligente al planteamiento de un problema tendiente a resolver, entre tantas, una necesidad humana" (p. 1). Los mismos autores distinguen dos etapas de la preinversión: la preparación, en la que se determina la magnitud de las inversiones, los costos y los beneficios, y la evaluación, en la que se mide la rentabilidad de la inversión (p. 2). Esa es la extensión que abarca la presente investigación, que no comprende la ejecución de la inversión. Por otra parte, la experiencia de la Universidad de Boston, donde el costo por estudiante descendió de unos 150 a unos 18 dólares al trasladar sus cursos a una nube universitaria (Shi, 2024), indica que una infraestructura propia puede representar un ahorro significativo. La presente investigación busca estimar ese beneficio en las condiciones del Instituto, mediante la relación entre la inversión y los costos de operación, por un lado, y el costo evitado de los servicios externos, por el otro.

Desde la perspectiva **tecnológica**, la investigación aplica tecnologías de virtualización por contenedores y de orquestación, de amplia adopción en la industria, al contexto de una institución universitaria venezolana. Con ello aporta un modelo de referencia para su uso con fines docentes. En el plano **social**, la plataforma contribuiría a reducir la desigualdad entre los estudiantes que pueden pagar servicios en divisas y los que no pueden hacerlo, al ofrecer a todos las mismas condiciones para publicar su trabajo. Dado que la plataforma no persigue un fin lucrativo, su conveniencia no puede medirse solo con criterios financieros privados. En términos de Sapag y Sapag (2000), corresponde a una evaluación social, que compara los beneficios y costos de una inversión para la comunidad en su conjunto e incorpora también los efectos intangibles que no pueden cuantificarse en dinero (pp. 7-8).

Desde el punto de vista **teórico**, la investigación sistematizará los fundamentos de la virtualización por contenedores, de la orquestación y del aislamiento entre usuarios, y los relacionará con las necesidades de una institución docente. Esa relación ha sido poco documentada en el contexto venezolano, como lo muestra la ausencia de antecedentes nacionales recientes identificados en la revisión bibliográfica.

En lo **metodológico**, la investigación aportará instrumentos validados para diagnosticar las necesidades de alojamiento de proyectos académicos, así como un conjunto de indicadores técnicos, operativos y económicos para evaluar plataformas de este tipo. Ambos podrán ser reutilizados por otras instituciones del país. Desde el punto de vista **científico-investigativo**, el estudio se inscribe en la línea de investigación Virtualización de la carrera de Ingeniería de Sistemas del Instituto, y podrá servir como antecedente para trabajos posteriores sobre infraestructura institucional.

En cuanto a su **alcance**, la investigación comprende el diagnóstico de las necesidades, la definición de la arquitectura de la plataforma y la evaluación de su factibilidad técnica, operativa y económica. Conforme al Manual del Instituto, el proyecto llega hasta la demostración de dicha factibilidad, apoyada en una prueba de concepto en laboratorio, la validación por expertos y el estudio de costos. La implantación de la plataforma en producción y su prueba piloto con asignaturas regulares se plantearán como recomendaciones para su ejecución. Quedan igualmente fuera de su alcance las bases de datos gestionadas, la alta disponibilidad del plano de control, la facturación y el escalado automático. El detalle técnico se desarrolla en el documento técnico.

---

## CAPÍTULO II. MARCO REFERENCIAL

*Pendiente.*

## CAPÍTULO III. MARCO METODOLÓGICO

*Pendiente.*

---

## Referencias

*Provisional: solo las obras citadas hasta ahora (capítulo I).*

Correa Cuvi, W. J. (2022). *Estudio de la plataforma Kubernetes para la administración automática de contenedores Docker en la facultad FICA de la Universidad Técnica del Norte*. Trabajo de grado de Ingeniería en Sistemas Computacionales no publicado, Universidad Técnica del Norte, Ibarra, Ecuador. Disponible: https://repositorio.utn.edu.ec/bitstream/123456789/12301/2/04%20ISC%20613%20TRABAJO%20GRADO.pdf [Consulta: 2026, octubre 4].

Flores, J. (2024, abril 27). Bancamiga aumentó los límites de su tarjeta de débito: estos son los montos. *El Diario* [Periódico en línea]. Disponible: https://eldiario.com/2024/04/27/bancamiga-limites-tarjeta-de-debito/ [Consulta: 2026, octubre 4].

Freedom House (2024). *Freedom on the Net 2024: Venezuela* [Documento en línea]. Disponible: https://freedomhouse.org/country/venezuela/freedom-net/2024 [Consulta: 2026, octubre 4].

Grzybowski, A. (2023, noviembre 28). *New England Research Cloud's affordable production cloud services now available to general research and education users* [Documento en línea]. Boston University, Hariri Institute for Computing. Disponible: https://www.bu.edu/hic/2023/11/28/the-newly-openednew-england-research-cloud-will-deliver-high-end-cloud-services-at-a-fraction-of-the-cost [Consulta: 2026, octubre 4].

Observatorio de Derechos Humanos de la Universidad de Los Andes (2023, agosto). *Situación de las universidades venezolanas: reporte mensual, agosto 2023* [Documento en línea]. Disponible: https://www.uladdhh.org.ve/wp-content/uploads/2023/09/8.-Reporte-agosto-2023-Situacion-de-las-Universidades-Venezolanas.pdf [Consulta: 2026, octubre 4].

Paz, R. (2023, agosto 14). Nube UNAM, una herramienta democratizante. *Gaceta UNAM* [Periódico en línea]. Disponible: https://www.gaceta.unam.mx/nube-unam-una-herramienta-democratizante/ [Consulta: 2026, octubre 4].

Red Hat (2021, abril 27). *Red Hat and Boston University announce major partnership to advance open hybrid cloud research and operations at scale* [Documento en línea]. Disponible: https://www.redhat.com/es/about/press-releases/red-hat-and-boston-university-announce-major-partnership-advance-open-hybrid-cloud-research-and-operations-scale [Consulta: 2026, octubre 4].

Sapag Chain, N. y Sapag Chain, R. (2000). *Preparación y evaluación de proyectos* (4ª ed.). Santiago de Chile: McGraw-Hill.

Shi, D. (2024, noviembre). The Open Education Project is ready to scale. *Red Hat Research Quarterly* [Revista en línea]. Disponible: https://research.redhat.com/blog/article/the-open-education-project-is-ready-to-scale/ [Consulta: 2026, octubre 4].

Wise, B. (2022, agosto 25). *Heroku's next chapter* [Documento en línea]. Heroku. Disponible: https://www.heroku.com/blog/next-chapter/ [Consulta: 2026, octubre 4].
