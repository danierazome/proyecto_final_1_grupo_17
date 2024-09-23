## ABCALL: Evaluación de Latencia, Escalabilidad y Disponibilidad en Microservicios

Este repositorio contiene los microservicios y el archivo de pruebas JMeter utilizados para realizar experimentos de evaluación en tres áreas clave: **latencia**, **escalabilidad**, y **disponibilidad**.

### Estructura del Proyecto

El proyecto está dividido en tres carpetas principales, cada una representando un microservicio asociado a los experimentos de latencia, escalabilidad, y disponibilidad, respectivamente:

#### 1. **`auth_ms_exp/` - Microservicio de Autenticación (Latencia)**
Este directorio contiene el microservicio que maneja la autenticación y autorización de usuarios. Utiliza Redis como caché para almacenar tokens JWT, permitiendo una reducción en la latencia durante el proceso de autenticación y consulta de PQRs.

- **Objetivo:** Validar si el uso de Redis como base de datos en caché permite realizar la autenticación y autorización en menos de 3 segundos en el 90% de los casos.
- **Endpoints:**
  - `auth/login`: Realiza el login del usuario y almacena el token JWT en Redis.
  - `auth/protected`: Valida el token JWT desde Redis y permite acceso a recursos protegidos.

#### 2. **`pqr_ms_exp/` - Microservicio de Consultas PQR (Escalabilidad)**
Este directorio contiene el microservicio que maneja las consultas de PQRs (Peticiones, Quejas y Reclamos). Se evaluó la escalabilidad del microservicio bajo distintas cargas para verificar su capacidad de respuesta en situaciones de alto volumen de usuarios concurrentes.

- **Objetivo:** Evaluar la escalabilidad del sistema bajo una carga de 500 usuarios concurrentes por segundo.
- **Resultados esperados:** Mantener la integridad y capacidad de respuesta del sistema bajo escenarios de alta demanda.

#### 3. **`users_ms_exp/` - Microservicio de Usuarios (Disponibilidad)**
Este directorio contiene el microservicio de gestión de usuarios. El enfoque de este experimento fue garantizar la **alta disponibilidad** del microservicio mediante estrategias como balanceo de carga, despliegues azules-verdes y monitoreo continuo.

- **Objetivo:** Asegurar la disponibilidad del servicio en un 99.99%, minimizando tiempos de inactividad.
- **Métricas:** Validar la capacidad del sistema para mantenerse disponible incluso durante despliegues y actualizaciones.

### Archivo de Pruebas JMeter: `experiments.jmx`

El archivo **`experiments.jmx`** es un script de pruebas desarrollado para JMeter que se utiliza para validar los experimentos descritos anteriormente. Este archivo incluye pruebas de carga y rendimiento sobre los microservicios de autenticación, PQR y usuarios. Las pruebas simulan un entorno con cientos de usuarios concurrentes para medir el desempeño y comportamiento bajo distintas condiciones.

#### Ejecución de las pruebas:

1. **Instalar JMeter**: Asegúrate de tener [Apache JMeter](https://jmeter.apache.org/download_jmeter.cgi) instalado en tu sistema.
2. **Abrir el archivo `experiments.jmx`**:
   - Inicia JMeter.
   - Abre el archivo `experiments.jmx` desde JMeter.
3. **Configurar los endpoints**:
   - Ajusta las variables dentro del archivo de acuerdo a la URL y puertos de tus microservicios desplegados.
4. **Ejecutar las pruebas**: Ejecuta las pruebas haciendo clic en el botón de inicio en JMeter.

### Requisitos Previos

- **Python 3.x**: Los microservicios están desarrollados en Flask, por lo que se requiere Python para su ejecución.
- **Redis**: Es necesario tener una instancia de Redis corriendo para el microservicio de autenticación.
- **JMeter**: Utilizado para las pruebas de carga y rendimiento.

### Cómo Correr los Microservicios

Cada microservicio tiene su propio archivo `run.py`. Sigue los pasos a continuación para ejecutar cada uno de ellos.

1. **Clonar el repositorio:**

2. **Instalar dependencias (repetir en cada carpeta de microservicio):**
   ```bash
   pip install -r requirements.txt
   ```

3. **Correr el microservicio (ejemplo para `auth_ms_exp`):**
   ```bash
   cd auth_ms_exp
   python run.py
   ```

### Resultados Esperados

Al realizar las pruebas de carga y rendimiento con JMeter, se espera obtener los siguientes resultados:

- **Latencia (auth_ms_exp):** El proceso de autenticación y autorización junto con la consulta de PQRs por usuario no debe superar los 3 segundos en el 90% de los casos.
- **Escalabilidad (pqr_ms_exp):** El microservicio de consultas PQR debe manejar la carga de usuarios concurrentes sin degradar significativamente el rendimiento.
- **Disponibilidad (users_ms_exp):** El microservicio de usuarios debe mantenerse disponible en un 99.99% de las pruebas, incluyendo durante despliegues y actualizaciones.