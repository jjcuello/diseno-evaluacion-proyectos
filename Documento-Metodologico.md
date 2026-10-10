# Plataforma web institucional de alojamiento y despliegue continuo (PaaS) — Documento metodológico

> Documento dirigido al **tutor metodológico**. Su única versión para entregar es `Documento-Metodologico.pdf` (y `.docx`), que `generar_documentos.py` arma con el formato del Manual: portada, índice general y el texto desde el capítulo I. Los datos de la portada están en ese script. La línea de investigación y la modalidad están en la [propuesta corta](Propuesta-Corta.md); las convenciones de los marcadores pendientes, en el README.

## CAPÍTULO I. EL PROBLEMA

### Contextualización del Problema

La formación de profesionales en el área de la informática exige que los estudiantes no se limiten a escribir programas, sino que los publiquen y los mantengan en funcionamiento en internet, tal como ocurrirá en su ejercicio profesional. Una vía frecuente para cubrir esa necesidad son las plataformas comerciales de alojamiento y despliegue, conocidas como plataforma como servicio o *Platform as a Service* (PaaS). Estas plataformas permiten al usuario publicar una aplicación sin administrar los servidores que la sostienen. Su ventaja técnica es evidente; sin embargo, convierte a estudiantes y docentes en usuarios dependientes de las condiciones comerciales de empresas privadas, que pueden modificarlas en cualquier momento.

Un caso que ilustra esa dependencia es el de Heroku, una plataforma de este tipo que ofrecía planes de uso gratuito. En agosto de 2022, la empresa anunció que a partir del 28 de noviembre de ese año dejaría de ofrecer sus planes gratuitos de cómputo, de bases de datos Postgres y de almacenamiento Redis, y que comenzaría a desactivar los servicios que funcionaban bajo esa modalidad (Wise, 2022). Con esa decisión, las aplicaciones alojadas sin costo, entre ellas los proyectos académicos, quedaron sin soporte, y sus autores debieron migrarlas, pagar una suscripción en moneda extranjera o abandonarlas. El hecho muestra que la gratuidad de estos servicios no constituye una garantía, sino una condición comercial revocable.

Frente a ese escenario, algunas universidades han optado por operar su propia infraestructura en la nube. En el estado de Massachusetts, Estados Unidos, la Universidad de Boston y la Universidad de Harvard operan la New England Research Cloud (N.E.R.C.), una nube de producción que ofrece máquinas virtuales, contenedores y almacenamiento a la comunidad de investigación y docencia. Sus tarifas se ubican entre un tercio y la mitad del costo de la nube pública (Grzybowski, 2023). Su administración está a cargo de la alianza de la Mass Open Cloud, una iniciativa de nube abierta con sede en la Universidad de Boston. En 2021, la empresa Red Hat le donó suscripciones de *software* valoradas en 551,9 millones de dólares (Red Hat, 2021).

El resultado más relevante para esta investigación proviene de la experiencia docente de esa misma universidad. Según una publicación de divulgación de Red Hat, empresa asociada al proyecto (Shi, 2024), en 2022 los cursos de sistemas computacionales de la Universidad de Boston que funcionaban sobre una plataforma comercial alojada en Amazon Web Services costaban aproximadamente 150 dólares por estudiante. Tras su traslado a la nube universitaria, el costo descendió a cerca de 18 dólares por estudiante, una reducción cercana a 88 por ciento (cálculo propio). En el semestre de primavera de 2024, esa infraestructura sostuvo tres asignaturas con más de 600 estudiantes en conjunto. Los motivos declarados del traslado fueron la reducción del costo, la disponibilidad de un clúster dedicado a las clases y un mayor control sobre la gestión del servicio.

Las experiencias reseñadas muestran dos maneras de atender la necesidad de publicar los proyectos académicos. La primera consiste en recurrir a proveedores comerciales, cuyo servicio es cómodo, pero queda sujeto a decisiones empresariales ajenas a la institución, como ocurrió con la supresión de los planes gratuitos de Heroku. La segunda consiste en que la propia universidad opere una infraestructura compartida, con lo cual asume su administración, pero gana control sobre el servicio y reduce el costo por estudiante, como lo demuestra el caso de la Universidad de Boston. Ambas opciones, sin embargo, se han documentado en instituciones con recursos financieros y técnicos considerables, por lo que conviene examinar cómo se presenta esta situación en contextos con menos recursos, como el latinoamericano.

En América Latina, la tendencia a reducir la dependencia de los proveedores transnacionales también se manifiesta en las instituciones de educación universitaria. La Universidad Nacional Autónoma de México (U.N.A.M.) opera una infraestructura propia en la nube, la Nube UNAM, administrada por su Dirección General de Cómputo y de Tecnologías de Información y Comunicación (D.G.T.I.C.). El servicio comprende tres herramientas: una bóveda digital, infraestructura como servicio y respaldo como servicio. Según el portal de tecnologías de esa universidad, "mediante la implementación de esta nube privada se logra una reducción de costos por el uso de plataformas de empresas de tecnología" (JLOM, 2023). Se trata, por tanto, de una respuesta institucional orientada tanto al ahorro como al control de los servicios que emplea la comunidad universitaria.

La dimensión estratégica de esa decisión fue expresada por la directora de la D.G.T.I.C., para quien el propósito de la Nube UNAM es "disminuir la dependencia de servicios y plataformas contratados a las empresas transnacionales" (Paz, 2023). No obstante, el servicio no está concebido para el uso individual de los estudiantes. Lo solicitan las escuelas, facultades, centros, institutos y dependencias, por medio de sus responsables de tecnología, y la misma fuente precisa que "los estudiantes se benefician con la Nube UNAM cuando sus entidades académicas implementan plataformas" (Paz, 2023). Ello revela que, incluso en una de las universidades de mayor tamaño de la región, la nube institucional no ofrece al estudiante un medio de autoservicio para publicar sus propios proyectos.

Por su parte, la literatura académica regional registra el mismo problema en el plano de la formación en informática. Correa (2022) documenta que en la Facultad de Ingeniería en Ciencias Aplicadas de la Universidad Técnica del Norte, en Ecuador, las carreras de Sistemas y de *Software* necesitan llevar a producción los proyectos web elaborados en sus asignaturas, pero el servidor de virtualización de la facultad no satisface la demanda. En palabras del autor, "los estudiantes actualmente presentan restricciones al momento de acceder a la plataforma de virtualización debido a la creciente demanda" (p. 20). La coincidencia entre ese diagnóstico y la situación que motiva esta investigación sugiere que se trata de una carencia compartida por las instituciones de la región, y no de un caso aislado.

Las respuestas documentadas en la región ante esta carencia se han desarrollado, en los casos revisados, en entornos de prueba. Sánchez (2024) implementó una infraestructura basada en Kubernetes, un orquestador de contenedores, en la Unidad de Tecnologías de la Información de la Pontificia Universidad Católica del Ecuador, sede Ibarra, en cuatro etapas: planificación, desarrollo del entorno, pruebas de validación y traspaso al departamento de tecnología. El autor concluyó que la solución mejora la gestión de las aplicaciones en contenedores, en beneficio del personal técnico, los docentes y los estudiantes. Sin embargo, tanto ese trabajo como el de Correa (2022), que empleó una instalación de un solo nodo para prácticas locales, dejan abierta la necesidad de un servicio permanente en el que el estudiante publique sus proyectos por sí mismo.

A lo anterior se suma una barrera económica que no ha sido cuantificada. Las plataformas comerciales de alojamiento facturan en dólares estadounidenses y exigen medios de pago internacionales. Sin embargo, no se dispone de estudios regionales que midan cuántos estudiantes universitarios quedan excluidos de estos servicios por carecer de dichos medios, ni cuánto destinan de sus propios recursos a mantener sus proyectos en línea `[FUENTE PENDIENTE: datos de tenencia de tarjetas de crédito en la región, Global Findex del Banco Mundial]`. Esta ausencia de datos justifica que la presente investigación obtenga información primaria mediante un diagnóstico de campo. Como se expone a continuación, en el caso venezolano esta barrera adquiere un peso mayor, debido a las condiciones de la infraestructura y del sistema financiero del país.

En Venezuela, las limitaciones descritas se agravan por las condiciones de la infraestructura nacional. De acuerdo con Freedom House (2024), en mayo de 2024 la velocidad mediana de la banda ancha móvil del país ocupó el puesto 138 entre 147 naciones evaluadas, y 22 de los 23 estados estaban sometidos a racionamiento eléctrico diario. El mismo informe señala que más de 70 por ciento de los planes de acceso a internet relevados costaba entre 4,44 y 56,22 veces el salario mínimo mensual, y que solo 48 por ciento de los hogares tenía acceso a internet, según una encuesta de 2023. En el cuadro 1 se resumen estos indicadores. En consecuencia, depender de servicios alojados en el exterior implica para el estudiante venezolano un costo y una inestabilidad mayores que para sus pares de otras regiones.

**Cuadro 1**

**Indicadores de Conectividad y Electricidad en Venezuela, 2023-2024**

| Indicador | Valor |
|---|---|
| Puesto en velocidad mediana de banda ancha móvil (mayo de 2024) | 138 de 147 países |
| Velocidad mediana de bajada en banda ancha móvil | 12,17 Mbps |
| Velocidad mediana de bajada en conexión fija | 53,90 Mbps |
| Estados sometidos a racionamiento eléctrico diario | 22 de 23 |
| Hogares con acceso a internet (encuesta de 2023) | 48 % |
| Costo de más de 70 % de los planes de internet relevados | Entre 4,44 y 56,22 salarios mínimos mensuales |

*Nota.* Datos tomados de Freedom House (2024). Las velocidades corresponden a mediciones de Ookla.

Las instituciones de educación universitaria del país tampoco disponen de holgura financiera para atender estas necesidades. El Observatorio de Derechos Humanos de la Universidad de Los Andes (O.D.H.U.L.A., 2023) describe una "asfixia presupuestaria" de las universidades venezolanas, que se traduce en el deterioro de sus instalaciones por falta de mantenimiento e inversión. El mismo reporte recoge la denuncia de un consejero universitario sobre cortes de electricidad de entre tres y 10 horas en la ciudad de Mérida, que dificultan las clases virtuales. En ese contexto, cualquier solución tecnológica dirigida a la comunidad universitaria debe caracterizarse por un bajo costo de adquisición y de operación, y por aprovechar los recursos de los que ya dispone la institución.

En el plano del pago de servicios en el exterior, la banca venezolana ofrece productos para consumos internacionales, pero con montos restringidos. A modo de ejemplo, una entidad bancaria nacional fijó en 2024 un límite diario de 500 dólares para los consumos en el país y de 200 dólares para los consumos en el extranjero con su tarjeta de débito (Flores, 2024). Por consiguiente, contratar un servicio de alojamiento en el exterior no resulta imposible para el estudiante, pero sí le exige disponer de divisas y de un producto bancario específico, sujeto a límites. Para quien solo maneja una cuenta en bolívares, ello constituye una fricción adicional que se suma al costo del propio servicio.

Este es el contexto en el que se ubica el Instituto Universitario Politécnico "Santiago Mariño" (I.U.P.S.M.), específicamente en su Extensión Caracas. En la carrera de Ingeniería de Sistemas, los estudiantes desarrollan en distintas asignaturas aplicaciones web y otros proyectos de *software* que, para ser evaluados en condiciones reales, deben publicarse en internet. Hasta donde ha podido observar el autor, el Instituto no cuenta con un servicio propio que permita a estudiantes y docentes alojar y desplegar esos proyectos, por lo cual cada estudiante resuelve la publicación por su cuenta. Para ello recurre a cuentas personales en plataformas comerciales externas, sujetas a las restricciones de pago, de costo y de conectividad descritas `[DIAGNÓSTICO: confirmar con datos de la encuesta a estudiantes y de la entrevista al departamento de tecnología]`.

Frente a esa situación, lo deseable es que el Instituto disponga de un servicio propio de alojamiento y despliegue, al alcance de todos sus estudiantes y docentes, sin costo para ellos y sin depender de pagos en divisas. En ese escenario, cada estudiante publicaría su proyecto directamente desde su repositorio de código, en un entorno aislado del de sus compañeros y con límites de recursos que garanticen un uso equitativo de la infraestructura. Los docentes, por su parte, revisarían las versiones publicadas desde un punto único, y los proyectos se conservarían al cierre de cada período académico. Además, dicho servicio tendría que apoyarse en los equipos de los que ya dispone la institución y en *software* libre, en atención a las restricciones financieras descritas.

La distancia entre la situación actual y la deseada obedece a varias causas. A partir de lo descrito, se identifican como principales: (a) la ausencia en el Instituto de una infraestructura propia destinada al alojamiento y despliegue de los proyectos académicos; (b) la dependencia de plataformas comerciales extranjeras, cuyas condiciones de uso y de gratuidad pueden cambiar sin previo aviso; (c) las restricciones para efectuar pagos internacionales desde el sistema bancario venezolano; y (d) las limitaciones presupuestarias de las instituciones universitarias del país para adquirir servicios en la nube pública.

Entre las consecuencias que se derivan de esta situación destacan las siguientes. En primer lugar, los proyectos alojados en cuentas personales o en planes gratuitos tienden a perderse cuando dichas cuentas vencen o cuando el proveedor modifica sus condiciones `[DIAGNÓSTICO: frecuencia de pérdida de proyectos]`. En segundo lugar, los estudiantes invierten tiempo en configurar despliegues de forma manual, en lugar de dedicarlo al aprendizaje propio de la asignatura `[DIAGNÓSTICO: horas dedicadas a desplegar]`. Asimismo, los docentes carecen de un punto único desde el cual revisar las versiones publicadas de los proyectos que evalúan. Por último, se produce una desigualdad de condiciones entre los estudiantes que pueden pagar servicios en divisas y los que no pueden hacerlo.

De mantenerse esta situación, el Instituto continuará dependiendo de proveedores externos sobre los cuales no ejerce ningún control, y la publicación de los proyectos académicos seguirá condicionada a la capacidad de pago de cada estudiante. Las experiencias reseñadas indican que las condiciones de gratuidad de estos servicios pueden desaparecer sin previo aviso (Wise, 2022). Por ello, es previsible que una parte de la producción académica de los estudiantes siga perdiéndose al cierre de cada período, sin quedar disponible como evidencia de aprendizaje ni como base para trabajos posteriores.

Para su abordaje, la investigación se delimita en los siguientes términos. En lo espacial, se desarrolla en el Instituto Universitario Politécnico "Santiago Mariño", Extensión Caracas, en la carrera de Ingeniería de Sistemas, específicamente en las asignaturas de programación y desarrollo de *software*. En lo temporal, abarca `[PENDIENTE: período académico en que se ejecutará la investigación, una vez inscrita la asignatura]`. En lo temático, comprende el diseño y la evaluación de la factibilidad de una plataforma de alojamiento y despliegue continuo basada en la virtualización por contenedores. Los sujetos de estudio son los estudiantes y docentes de dichas asignaturas y el personal del departamento de tecnología del Instituto. Por su campo de trabajo, la investigación se inscribe en la línea de investigación Sistemas de Comunicación de la carrera, área Transmisión de Datos, sublínea Virtualización, con Seguridad de Datos como área complementaria.

En atención a lo expuesto, se formula la siguiente interrogante general: ¿En qué medida es factible, desde los puntos de vista técnico, operativo y económico, una plataforma institucional de alojamiento y despliegue continuo que permita a estudiantes y docentes del Instituto Universitario Politécnico "Santiago Mariño" publicar sus proyectos académicos sin depender de servicios externos de pago? De ella se desprenden las siguientes interrogantes específicas: (a) ¿Cuáles son las necesidades de alojamiento y despliegue de proyectos académicos de los estudiantes y docentes del Instituto?; (b) ¿Qué arquitectura debe tener una plataforma que atienda esas necesidades con aislamiento entre usuarios y límites de recursos?; y (c) ¿Es factible, en lo técnico, lo operativo y lo económico, la implantación de dicha plataforma en el Instituto?

### Objetivos de la Investigación

La investigación se orientará al logro de los siguientes objetivos.

#### Objetivo General

Diseñar una plataforma web institucional de alojamiento y despliegue continuo (PaaS) para el Politécnico Santiago Mariño.

#### Objetivos Específicos

1. Diagnosticar las necesidades de alojamiento y despliegue de proyectos académicos de los estudiantes y docentes.
2. Definir la arquitectura de la plataforma web de alojamiento y despliegue continuo, con aislamiento por contenedores y límites de recursos.
3. Evaluar la factibilidad técnica, operativa y económica de la plataforma.

### Justificación de la Investigación

La investigación se justifica por los aportes que ofrece a distintos actores de la comunidad del Instituto. Los estudiantes de Ingeniería de Sistemas serán sus beneficiarios directos, pues contarán con un medio propio, estable y sin costo para publicar los proyectos que desarrollan en sus asignaturas. Los docentes dispondrán de un punto único para revisar las versiones publicadas de los trabajos que evalúan. El departamento de tecnología obtendrá un modelo de referencia para administrar un servicio compartido con aislamiento entre usuarios. Por último, el Instituto en su conjunto podrá conservar la producción académica de sus estudiantes como evidencia de aprendizaje y como base para trabajos posteriores.

En cuanto a su relevancia científico-investigativa, el estudio sistematizará los fundamentos de la virtualización por contenedores, de la orquestación y del aislamiento entre usuarios, y los relacionará con las necesidades de una institución docente, relación poco documentada en el contexto venezolano según la revisión bibliográfica realizada. En el plano metodológico, aportará instrumentos validados para diagnosticar las necesidades de alojamiento de proyectos académicos, así como un conjunto de indicadores técnicos, operativos y económicos para evaluar plataformas de este tipo, que podrán ser reutilizados por otras instituciones del país. Asimismo, el estudio se inscribe en la sublínea Virtualización de la carrera de Ingeniería de Sistemas del Instituto y podrá servir como antecedente para trabajos posteriores sobre infraestructura institucional.

La investigación tiene, además, relevancia contemporánea, pues aborda un desafío actual de la formación en informática: la adopción de prácticas de despliegue que hoy son habituales en el ejercicio profesional. Según la encuesta anual de la Cloud Native Computing Foundation (C.N.C.F.), 91 por ciento de las organizaciones consultadas utilizaba contenedores en producción en 2024, frente a 80 por ciento en 2023, y 29 por ciento publicaba código varias veces al día (Silverthorne y Hendrick, 2025). Una plataforma institucional basada en estas tecnologías permitirá que los estudiantes se familiaricen, durante su formación, con el despliegue continuo y la virtualización por contenedores, y acercará así la práctica académica a las condiciones del mercado laboral.

En el plano económico, el estudio se apoya en el enfoque de la preparación y evaluación de proyectos. Para Sapag y Sapag (2000), un proyecto "no es ni más ni menos que la búsqueda de una solución inteligente al planteamiento de un problema tendiente a resolver, entre tantas, una necesidad humana" (p. 1). Los mismos autores distinguen dos etapas de la preinversión: la preparación, en la que se determina la magnitud de las inversiones, los costos y los beneficios, y la evaluación, en la que se mide la rentabilidad de la inversión (p. 2). La presente investigación abarca ambas etapas, sin comprender la ejecución de la inversión, y estimará el beneficio de una infraestructura propia en las condiciones del Instituto mediante la relación entre la inversión y los costos de operación, por un lado, y el costo evitado de los servicios externos, por el otro. Con ello aportará a la institución un criterio cuantitativo para decidir sobre la asignación de sus recursos.

En lo social, la plataforma contribuirá a que todos los estudiantes cuenten con las mismas condiciones para publicar su trabajo, con independencia de su capacidad de pago, y favorecerá que los proyectos académicos permanezcan disponibles para la comunidad. Dado que la plataforma no persigue un fin lucrativo, su conveniencia no puede medirse solo con criterios financieros privados. En términos de Sapag y Sapag (2000), corresponde a una evaluación social, que compara los beneficios y costos de una inversión para la comunidad en su conjunto e incorpora también los efectos intangibles que no pueden cuantificarse en dinero (pp. 7-8).

Desde la perspectiva tecnológica, la investigación aplica la virtualización por contenedores y la orquestación al contexto de una institución universitaria venezolana, y propone una arquitectura basada en *software* libre que aprovecha los equipos existentes. Con ello transforma conocimientos técnicos disponibles en una solución práctica para un problema concreto, y aporta un modelo de referencia que otras instituciones con restricciones similares podrán adaptar. Además, la definición de la arquitectura, con aislamiento entre usuarios y límites de recursos, ofrecerá al departamento de tecnología del Instituto una base técnica documentada para una eventual implantación.

En cuanto a su alcance, la investigación comprende el diagnóstico de las necesidades, la definición de la arquitectura de la plataforma y la evaluación de su factibilidad técnica, operativa y económica. Conforme al Manual del Instituto, el proyecto llega hasta la demostración de dicha factibilidad, apoyada en una prueba de concepto en laboratorio, la validación por expertos y el estudio de costos. La implantación de la plataforma en producción y su prueba piloto con asignaturas regulares se plantearán como recomendaciones para su ejecución. Quedan igualmente fuera de su alcance las bases de datos gestionadas, la alta disponibilidad del plano de control, la facturación y el escalado automático.

## CAPÍTULO II. MARCO REFERENCIAL

### Antecedentes de la Investigación

### Bases Teóricas

### Bases Legales

### Sistema de Hipótesis (si aplica)

### Sistema de Variables

### Operacionalización de Variables

### Definición de Términos Básicos

*Pendiente.*

## CAPÍTULO III. MARCO METODOLÓGICO

### Modalidad de la Investigación

### Diseño de la Investigación

### Tipo de la Investigación

### Procedimientos de la Investigación

### Población y Muestra

### Técnicas e Instrumentos de Recolección de Datos

### Técnicas de Análisis de Datos

### Limitaciones de la Investigación

*Pendiente.*

## Referencias

*Provisional: solo las obras citadas hasta ahora (capítulo I).*

Correa Cuvi, W. J. (2022). *Estudio de la plataforma Kubernetes para la administración automática de contenedores Docker en la facultad FICA de la Universidad Técnica del Norte*. Trabajo de grado de Ingeniería en Sistemas Computacionales no publicado, Universidad Técnica del Norte, Ibarra, Ecuador. Disponible: https://repositorio.utn.edu.ec/bitstream/123456789/12301/2/04%20ISC%20613%20TRABAJO%20GRADO.pdf [Consulta: 2026, octubre 4].

Flores, J. (2024, abril 27). Bancamiga aumentó los límites de su tarjeta de débito: estos son los montos. *El Diario* [Periódico en línea]. Disponible: https://eldiario.com/2024/04/27/bancamiga-limites-tarjeta-de-debito/ [Consulta: 2026, octubre 4].

Freedom House (2024). *Freedom on the Net 2024: Venezuela* [Documento en línea]. Disponible: https://freedomhouse.org/country/venezuela/freedom-net/2024 [Consulta: 2026, octubre 4].

Grzybowski, A. (2023, noviembre 28). *New England Research Cloud's affordable production cloud services now available to general research and education users* [Documento en línea]. Boston University, Hariri Institute for Computing. Disponible: https://www.bu.edu/hic/2023/11/28/the-newly-openednew-england-research-cloud-will-deliver-high-end-cloud-services-at-a-fraction-of-the-cost [Consulta: 2026, octubre 4].

JLOM (2023, junio 27). *Ofrece la UNAM servicios de nube a su comunidad* [Documento en línea]. Portal TIC UNAM. Disponible: https://www.tic.unam.mx/noticias/ofrece-unam-servicios-nube-comunidad/ [Consulta: 2026, octubre 9].

Observatorio de Derechos Humanos de la Universidad de Los Andes (2023, agosto). *Situación de las universidades venezolanas: reporte mensual, agosto 2023* [Documento en línea]. Disponible: https://www.uladdhh.org.ve/wp-content/uploads/2023/09/8.-Reporte-agosto-2023-Situacion-de-las-Universidades-Venezolanas.pdf [Consulta: 2026, octubre 4].

Paz, R. (2023, agosto 14). Nube UNAM, una herramienta democratizante. *Gaceta UNAM* [Periódico en línea]. Disponible: https://www.gaceta.unam.mx/nube-unam-una-herramienta-democratizante/ [Consulta: 2026, octubre 9].

Red Hat (2021, abril 27). *Red Hat and Boston University announce major partnership to advance open hybrid cloud research and operations at scale* [Documento en línea]. Disponible: https://www.redhat.com/es/about/press-releases/red-hat-and-boston-university-announce-major-partnership-advance-open-hybrid-cloud-research-and-operations-scale [Consulta: 2026, octubre 4].

Sánchez Villacis, D. A. (2024). *Infraestructura kubernetes para implementación de aplicaciones en contenedores en entorno de pruebas en la Unidad de Tecnologías de la Información de la PUCE-Ibarra*. Trabajo de titulación de pregrado no publicado, Pontificia Universidad Católica del Ecuador, Ibarra, Ecuador. Disponible: https://repositorio.puce.edu.ec/handle/123456789/44584 [Consulta: 2026, octubre 4].

Sapag Chain, N. y Sapag Chain, R. (2000). *Preparación y evaluación de proyectos* (4ª ed.). Santiago de Chile: McGraw-Hill.

Shi, D. (2024, noviembre). The Open Education Project is ready to scale. *Red Hat Research Quarterly* [Revista en línea]. Disponible: https://research.redhat.com/blog/article/the-open-education-project-is-ready-to-scale/ [Consulta: 2026, octubre 4].

Silverthorne, V. y Hendrick, S. (2025, marzo). *Cloud native 2024: Approaching a decade of code, cloud, and change* [Documento en línea]. The Linux Foundation y Cloud Native Computing Foundation. Disponible: https://www.cncf.io/reports/cncf-annual-survey-2024/ [Consulta: 2026, octubre 9].

Wise, B. (2022, agosto 25). *Heroku's next chapter* [Documento en línea]. Heroku. Disponible: https://www.heroku.com/blog/next-chapter/ [Consulta: 2026, octubre 4].
