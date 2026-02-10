# 🚀 Node.js Basics - Guía Completa

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/d/d9/Node.js_logo.svg" alt="Node.js Logo" width="300"/>
</p>

## 📋 Tabla de Contenidos

1. [¿Qué es Node.js?](#-qué-es-nodejs)
2. [¿Por qué usar Node.js?](#-por-qué-usar-nodejs)
3. [Arquitectura de Node.js](#-arquitectura-de-nodejs)
4. [El Event Loop Explicado](#-el-event-loop-explicado)
5. [Ejecutar JavaScript con Node.js](#-ejecutar-javascript-con-nodejs)
6. [Sistema de Módulos](#-sistema-de-módulos)
7. [Módulos Integrados (Built-in)](#-módulos-integrados-built-in)
8. [Process API](#-process-api)
9. [Sistema de Archivos (fs)](#-sistema-de-archivos-fs)
10. [Lectura de Archivos: Síncrono vs Asíncrono](#-lectura-de-archivos-síncrono-vs-asíncrono)
11. [Creando un Servidor HTTP](#-creando-un-servidor-http)
12. [Express.js: El Framework Web](#-expressjs-el-framework-web)
13. [NPM: El Gestor de Paquetes](#-npm-el-gestor-de-paquetes)
14. [Babel y ES6+](#-babel-y-es6)
15. [Nodemon para Desarrollo](#-nodemon-para-desarrollo)
16. [Estructura del Proyecto](#-estructura-del-proyecto)
17. [Requisitos](#-requisitos)
18. [Recursos Adicionales](#-recursos-adicionales)

---

## 🌟 ¿Qué es Node.js?

**Node.js** es un **entorno de ejecución de JavaScript** construido sobre el motor **V8 de Chrome**. Pero, ¿qué significa esto exactamente?

### 🧠 Entendámoslo paso a paso:

Imagina que JavaScript es como un idioma que solo se podía hablar dentro de una casa específica (el navegador web). Node.js es como darle a JavaScript un pasaporte para que pueda viajar y "hablar" en cualquier parte: en servidores, en tu computadora, ¡en cualquier lugar!

```
┌─────────────────────────────────────────────────────────────┐
│                    ANTES DE NODE.JS                         │
│                                                             │
│   JavaScript 🗣️ ────────► Solo en navegadores 🌐            │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                    CON NODE.JS                              │
│                                                             │
│   JavaScript 🗣️ ────────► Navegadores 🌐                    │
│                  ────────► Servidores 🖥️                    │
│                  ────────► Herramientas CLI ⚡               │
│                  ────────► Aplicaciones de escritorio 💻    │
│                  ────────► IoT (Internet de las cosas) 📱   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 🔧 Motor V8: El Corazón de Node.js

El **motor V8** es el componente de Google Chrome que convierte código JavaScript en código máquina que tu computadora puede ejecutar directamente. Es increíblemente rápido porque:

- **Compila JavaScript a código máquina nativo** (no interpreta línea por línea)
- **Optimiza el código en tiempo real** (JIT - Just In Time compilation)
- **Gestiona la memoria automáticamente** (Garbage Collection)

```javascript
// Este código JavaScript...
const saludo = "¡Hola, Node.js!";
console.log(saludo);

// V8 lo convierte en instrucciones que tu CPU entiende directamente
// ¡Esto ocurre en milisegundos!
```

---

## 💡 ¿Por qué usar Node.js?

### 1. **JavaScript en Todas Partes (Full Stack JS)**

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│    Frontend          Backend           Base de Datos         │
│    ┌──────┐         ┌──────┐          ┌──────┐              │
│    │ React│         │Node  │          │Mongo │              │
│    │ Vue  │◄───────►│ js   │◄────────►│ DB   │              │
│    │ etc  │         │      │          │      │              │
│    └──────┘         └──────┘          └──────┘              │
│        │               │                  │                  │
│        └───────────────┼──────────────────┘                  │
│                        │                                     │
│              TODO EN JAVASCRIPT 🎉                           │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### 2. **No Bloqueante (Non-Blocking I/O)**

Esta es la **superpotencia** de Node.js. Mientras otros lenguajes esperan a que una tarea termine para comenzar otra, Node.js puede manejar miles de operaciones simultáneamente.

**Ejemplo del restaurante:**

```
SERVIDOR TRADICIONAL (Bloqueante):
─────────────────────────────────
Mesero 1: Toma pedido → Va a cocina → Espera → Sirve → (Siguiente cliente)
          Cliente 2, 3, 4... esperando 😴

NODE.JS (No Bloqueante):
────────────────────────
Mesero: Toma pedido A → Toma pedido B → Toma pedido C
        ↓               ↓               ↓
      Cocina A       Cocina B       Cocina C
        ↓               ↓               ↓
      Sirve A        Sirve B        Sirve C
      
¡Todos atendidos casi al mismo tiempo! 🚀
```

### 3. **Ecosistema Gigante (NPM)**

NPM tiene más de **2 millones de paquetes**. Es como tener acceso a una biblioteca infinita de código que otros desarrolladores han creado.

### 4. **Rendimiento Excepcional**

- **Alta concurrencia**: Puede manejar miles de conexiones simultáneas
- **Bajo consumo de memoria**: Un solo hilo maneja múltiples conexiones
- **Rápido**: Gracias al motor V8

---

## 🏗️ Arquitectura de Node.js

```
┌─────────────────────────────────────────────────────────────────┐
│                     Tu Código JavaScript                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       Node.js APIs                              │
│  (fs, http, path, os, crypto, etc.)                            │
└─────────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
│     Motor V8     │ │     libuv        │ │  Otros bindings  │
│  (JavaScript)    │ │  (Event Loop,    │ │  (c-ares, zlib,  │
│                  │ │   I/O async)     │ │   OpenSSL)       │
└──────────────────┘ └──────────────────┘ └──────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Sistema Operativo                             │
│              (Windows, Linux, macOS)                            │
└─────────────────────────────────────────────────────────────────┘
```

### Componentes Clave:

| Componente | Función |
|------------|---------|
| **V8** | Ejecuta y compila JavaScript |
| **libuv** | Maneja operaciones asíncronas y el Event Loop |
| **Node.js APIs** | Proporciona funcionalidades (archivos, red, etc.) |
| **C++ Bindings** | Conecta JavaScript con código de bajo nivel |

---

## 🔄 El Event Loop Explicado

El **Event Loop** es el corazón de Node.js. Es lo que permite que Node.js sea no bloqueante.

### 🎭 Analogía: El Chef Multitarea

Imagina un chef que puede:
1. Poner agua a hervir (no espera mirando la olla)
2. Mientras, corta verduras
3. Mientras, prepara la salsa
4. Cuando el agua hierve, recibe una "notificación" y actúa

```
┌───────────────────────────────────────────────────────────────┐
│                        EVENT LOOP                             │
│                                                               │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│   │   Timers    │───►│   Pending   │───►│    Idle     │     │
│   │ setTimeout  │    │  Callbacks  │    │   Prepare   │     │
│   │ setInterval │    │             │    │             │     │
│   └─────────────┘    └─────────────┘    └─────────────┘     │
│          ▲                                     │              │
│          │                                     ▼              │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│   │    Close    │◄───│    Check    │◄───│    Poll     │     │
│   │  Callbacks  │    │ setImmediate│    │   (I/O)     │     │
│   │             │    │             │    │             │     │
│   └─────────────┘    └─────────────┘    └─────────────┘     │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

### Ejemplo Práctico:

```javascript
console.log('1. Inicio');  // Síncrono - se ejecuta primero

setTimeout(() => {
    console.log('2. Timeout');  // Se agenda para después
}, 0);

Promise.resolve().then(() => {
    console.log('3. Promise');  // Microtarea - prioridad alta
});

console.log('4. Fin');  // Síncrono - se ejecuta segundo

// Salida:
// 1. Inicio
// 4. Fin
// 3. Promise
// 2. Timeout
```

**¿Por qué este orden?**
1. El código síncrono se ejecuta primero (Inicio, Fin)
2. Las Promesas (microtareas) tienen prioridad sobre timers
3. setTimeout se ejecuta en la siguiente iteración del Event Loop

---

## ⚡ Ejecutar JavaScript con Node.js

### Método 1: Ejecutar un archivo

```bash
# Crear un archivo
echo 'console.log("¡Hola desde Node.js!")' > app.js

# Ejecutarlo
node app.js
```

### Método 2: REPL (Read-Eval-Print Loop)

```bash
# Iniciar REPL
node

# Ahora puedes escribir JavaScript directamente
> 2 + 2
4
> const nombre = "Holberton"
undefined
> console.log(`Hola, ${nombre}!`)
Hola, Holberton!
```

### Método 3: Ejecutar código inline

```bash
node -e "console.log('Código inline!')"
```

---

## 📦 Sistema de Módulos

Node.js utiliza un sistema de módulos para organizar el código. Existen dos sistemas:

### 1. CommonJS (El tradicional)

```javascript
// ══════════════════════════════════════════════════════
// archivo: matematicas.js (EXPORTAR)
// ══════════════════════════════════════════════════════

const sumar = (a, b) => a + b;
const restar = (a, b) => a - b;
const PI = 3.14159;

// Exportar múltiples elementos
module.exports = {
    sumar,
    restar,
    PI
};

// O exportar uno por uno
module.exports.multiplicar = (a, b) => a * b;
```

```javascript
// ══════════════════════════════════════════════════════
// archivo: app.js (IMPORTAR)
// ══════════════════════════════════════════════════════

// Importar todo el módulo
const matematicas = require('./matematicas');
console.log(matematicas.sumar(5, 3));  // 8

// O usar destructuring
const { sumar, PI } = require('./matematicas');
console.log(sumar(10, 5));  // 15
console.log(PI);  // 3.14159
```

### 2. ES Modules (El moderno - ES6+)

```javascript
// ══════════════════════════════════════════════════════
// archivo: matematicas.mjs (EXPORTAR)
// ══════════════════════════════════════════════════════

export const sumar = (a, b) => a + b;
export const restar = (a, b) => a - b;
export const PI = 3.14159;

// Export default
export default function multiplicar(a, b) {
    return a * b;
}
```

```javascript
// ══════════════════════════════════════════════════════
// archivo: app.mjs (IMPORTAR)
// ══════════════════════════════════════════════════════

import multiplicar, { sumar, PI } from './matematicas.mjs';

console.log(sumar(5, 3));       // 8
console.log(multiplicar(4, 2)); // 8
console.log(PI);                // 3.14159
```

### Comparación:

| Característica | CommonJS | ES Modules |
|----------------|----------|------------|
| Sintaxis | `require()` / `module.exports` | `import` / `export` |
| Carga | Síncrona | Asíncrona |
| Extensión | `.js` | `.mjs` o `"type": "module"` |
| Uso | Node.js tradicional | Estándar moderno |

---

## 🧰 Módulos Integrados (Built-in)

Node.js viene con módulos ya incluidos que no necesitas instalar:

```javascript
// ══════════════════════════════════════════════════════
// MÓDULOS PRINCIPALES DE NODE.JS
// ══════════════════════════════════════════════════════

const fs = require('fs');          // Sistema de archivos
const path = require('path');      // Rutas de archivos
const http = require('http');      // Servidor HTTP
const https = require('https');    // Servidor HTTPS
const os = require('os');          // Info del sistema operativo
const crypto = require('crypto'); // Criptografía
const events = require('events'); // Manejo de eventos
const util = require('util');      // Utilidades
const stream = require('stream');  // Streams de datos
const url = require('url');        // Parsing de URLs
const querystring = require('querystring'); // Query strings
const readline = require('readline'); // Input del usuario
const child_process = require('child_process'); // Procesos hijos
```

### Ejemplos de uso:

```javascript
// ══════════════════════════════════════════════════════
// OS - Información del Sistema
// ══════════════════════════════════════════════════════
const os = require('os');

console.log('Sistema:', os.platform());        // 'win32', 'linux', 'darwin'
console.log('Arquitectura:', os.arch());       // 'x64', 'arm64'
console.log('CPUs:', os.cpus().length);        // Número de núcleos
console.log('Memoria Total:', os.totalmem());  // Bytes de RAM
console.log('Memoria Libre:', os.freemem());   // Bytes libres
console.log('Home Dir:', os.homedir());        // Directorio home
console.log('Usuario:', os.userInfo().username);
```

```javascript
// ══════════════════════════════════════════════════════
// PATH - Manejo de Rutas
// ══════════════════════════════════════════════════════
const path = require('path');

// Unir rutas de forma segura (multiplataforma)
const ruta = path.join('carpeta', 'subcarpeta', 'archivo.txt');
console.log(ruta);  // carpeta/subcarpeta/archivo.txt (o \ en Windows)

// Obtener extensión
console.log(path.extname('documento.pdf'));  // .pdf

// Obtener nombre del archivo
console.log(path.basename('/ruta/al/archivo.js'));  // archivo.js

// Obtener directorio
console.log(path.dirname('/ruta/al/archivo.js'));  // /ruta/al

// Ruta absoluta
console.log(path.resolve('archivo.js'));  // /ruta/completa/archivo.js
```

---

## 🔧 Process API

El objeto `process` es global y proporciona información sobre el proceso actual de Node.js.

```javascript
// ══════════════════════════════════════════════════════
// PROCESS - Control del Proceso
// ══════════════════════════════════════════════════════

// Argumentos de línea de comandos
// Si ejecutas: node app.js argumento1 argumento2
console.log(process.argv);
// ['/ruta/node', '/ruta/app.js', 'argumento1', 'argumento2']

// Variables de entorno
console.log(process.env.PATH);         // PATH del sistema
console.log(process.env.NODE_ENV);     // 'development' o 'production'

// Información del proceso
console.log(process.pid);              // ID del proceso
console.log(process.cwd());            // Directorio de trabajo actual
console.log(process.version);          // Versión de Node.js

// Salir del proceso
process.exit(0);    // Salida exitosa
process.exit(1);    // Salida con error

// Entrada estándar
process.stdin.on('data', (data) => {
    console.log(`Escribiste: ${data}`);
});

// Salida estándar
process.stdout.write('Hola sin salto de línea');
process.stderr.write('Mensaje de error');
```

### Ejemplo Práctico: CLI con argumentos

```javascript
// archivo: saludo.js

const args = process.argv.slice(2);  // Quitar 'node' y 'script.js'
const nombre = args[0] || 'Mundo';
const idioma = args[1] || 'es';

const saludos = {
    es: '¡Hola',
    en: 'Hello',
    fr: 'Bonjour'
};

console.log(`${saludos[idioma] || saludos.es}, ${nombre}!`);

// Uso:
// node saludo.js María es  → ¡Hola, María!
// node saludo.js John en   → Hello, John!
```

---

## 📁 Sistema de Archivos (fs)

El módulo `fs` permite interactuar con el sistema de archivos:

```javascript
const fs = require('fs');

// ══════════════════════════════════════════════════════
// LEER ARCHIVOS
// ══════════════════════════════════════════════════════

// Asíncrono (recomendado)
fs.readFile('archivo.txt', 'utf-8', (error, contenido) => {
    if (error) {
        console.error('Error:', error.message);
        return;
    }
    console.log(contenido);
});

// Con Promesas (moderno)
const fsPromises = require('fs').promises;

async function leerArchivo() {
    try {
        const contenido = await fsPromises.readFile('archivo.txt', 'utf-8');
        console.log(contenido);
    } catch (error) {
        console.error('Error:', error.message);
    }
}

// ══════════════════════════════════════════════════════
// ESCRIBIR ARCHIVOS
// ══════════════════════════════════════════════════════

// Crear/Sobrescribir archivo
fs.writeFile('nuevo.txt', 'Contenido del archivo', (error) => {
    if (error) throw error;
    console.log('Archivo creado!');
});

// Añadir al final del archivo
fs.appendFile('log.txt', 'Nueva línea\n', (error) => {
    if (error) throw error;
    console.log('Línea añadida!');
});

// ══════════════════════════════════════════════════════
// OPERACIONES CON DIRECTORIOS
// ══════════════════════════════════════════════════════

// Crear directorio
fs.mkdir('nueva-carpeta', { recursive: true }, (error) => {
    if (error) throw error;
});

// Listar contenido de directorio
fs.readdir('.', (error, archivos) => {
    if (error) throw error;
    console.log('Archivos:', archivos);
});

// Verificar si existe
fs.access('archivo.txt', fs.constants.F_OK, (error) => {
    console.log(error ? 'No existe' : 'Existe');
});

// Obtener información del archivo
fs.stat('archivo.txt', (error, stats) => {
    if (error) throw error;
    console.log('Es archivo:', stats.isFile());
    console.log('Es directorio:', stats.isDirectory());
    console.log('Tamaño:', stats.size, 'bytes');
});
```

---

## ⚖️ Lectura de Archivos: Síncrono vs Asíncrono

### 🐢 Síncrono (Bloqueante)

```javascript
const fs = require('fs');

console.log('Inicio');

// ⚠️ BLOQUEA todo hasta que termine de leer
const contenido = fs.readFileSync('archivo.txt', 'utf-8');
console.log(contenido);

console.log('Fin');

// Salida (en orden):
// Inicio
// [contenido del archivo]
// Fin
```

**Cuándo usar:** Solo al inicio de la aplicación (configuración, carga inicial).

### 🚀 Asíncrono (No Bloqueante)

```javascript
const fs = require('fs');

console.log('Inicio');

// ✅ NO bloquea - continúa ejecutando
fs.readFile('archivo.txt', 'utf-8', (error, contenido) => {
    if (error) throw error;
    console.log(contenido);
});

console.log('Fin');

// Salida (el orden puede variar):
// Inicio
// Fin
// [contenido del archivo]
```

**Cuándo usar:** Siempre que sea posible, especialmente en servidores.

### 📊 Comparación Visual

```
SÍNCRONO:
─────────
Tarea 1 ████████████████░░░░░░░░░░░░░░░░░░░░░░░
Tarea 2 ░░░░░░░░░░░░░░░░████████████████░░░░░░░
Tarea 3 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████
                                          Tiempo ───►

ASÍNCRONO:
──────────
Tarea 1 ████████████████
Tarea 2 ████████████████
Tarea 3 ████████████████
        ─────────────────
                          Tiempo ───►
        ¡Mucho más rápido! 🚀
```

---

## 🌐 Creando un Servidor HTTP

### Servidor HTTP Básico

```javascript
const http = require('http');

// Crear el servidor
const servidor = http.createServer((request, response) => {
    // request = información de la petición entrante
    // response = objeto para enviar la respuesta

    // Configurar headers
    response.writeHead(200, {
        'Content-Type': 'text/html; charset=utf-8'
    });

    // Enviar respuesta
    response.end('<h1>¡Hola desde mi servidor Node.js!</h1>');
});

// Escuchar en puerto 3000
const PORT = 3000;
servidor.listen(PORT, () => {
    console.log(`🚀 Servidor corriendo en http://localhost:${PORT}`);
});
```

### Servidor con Rutas

```javascript
const http = require('http');
const url = require('url');

const servidor = http.createServer((req, res) => {
    const rutaParseada = url.parse(req.url, true);
    const ruta = rutaParseada.pathname;
    const metodo = req.method;

    res.setHeader('Content-Type', 'application/json');

    // Router simple
    if (ruta === '/' && metodo === 'GET') {
        res.statusCode = 200;
        res.end(JSON.stringify({ mensaje: 'Bienvenido a la API' }));

    } else if (ruta === '/usuarios' && metodo === 'GET') {
        res.statusCode = 200;
        res.end(JSON.stringify({ usuarios: ['Ana', 'Carlos', 'María'] }));

    } else if (ruta === '/saludo' && metodo === 'GET') {
        const nombre = rutaParseada.query.nombre || 'Visitante';
        res.statusCode = 200;
        res.end(JSON.stringify({ saludo: `¡Hola, ${nombre}!` }));

    } else {
        res.statusCode = 404;
        res.end(JSON.stringify({ error: 'Ruta no encontrada' }));
    }
});

servidor.listen(3000, () => {
    console.log('🚀 API corriendo en http://localhost:3000');
});
```

---

## 🚂 Express.js: El Framework Web

**Express** simplifica enormemente la creación de servidores y APIs.

### Instalación

```bash
npm install express
```

### Servidor Express Básico

```javascript
const express = require('express');
const app = express();

// Middleware para parsear JSON
app.use(express.json());

// Ruta GET básica
app.get('/', (req, res) => {
    res.send('¡Hola desde Express!');
});

// Ruta con parámetros
app.get('/usuarios/:id', (req, res) => {
    const { id } = req.params;
    res.json({ mensaje: `Usuario con ID: ${id}` });
});

// Ruta POST
app.post('/usuarios', (req, res) => {
    const { nombre, email } = req.body;
    res.status(201).json({
        mensaje: 'Usuario creado',
        usuario: { nombre, email }
    });
});

// Query parameters
app.get('/buscar', (req, res) => {
    const { q, limite } = req.query;
    res.json({ busqueda: q, limite: limite || 10 });
});

// Iniciar servidor
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`🚀 Express corriendo en http://localhost:${PORT}`);
});
```

### Comparación: HTTP nativo vs Express

```javascript
// ══════════════════════════════════════════════════════
// HTTP NATIVO (verbose)
// ══════════════════════════════════════════════════════
const http = require('http');
http.createServer((req, res) => {
    if (req.url === '/api/data' && req.method === 'GET') {
        res.writeHead(200, {'Content-Type': 'application/json'});
        res.end(JSON.stringify({data: 'value'}));
    }
}).listen(3000);

// ══════════════════════════════════════════════════════
// EXPRESS (limpio y simple)
// ══════════════════════════════════════════════════════
const express = require('express');
const app = express();
app.get('/api/data', (req, res) => res.json({data: 'value'}));
app.listen(3000);
```

---

## 📦 NPM: El Gestor de Paquetes

NPM (Node Package Manager) es el gestor de paquetes de Node.js.

### Comandos Esenciales

```bash
# ══════════════════════════════════════════════════════
# INICIALIZACIÓN
# ══════════════════════════════════════════════════════
npm init              # Crear package.json interactivo
npm init -y           # Crear package.json con valores por defecto

# ══════════════════════════════════════════════════════
# INSTALACIÓN DE PAQUETES
# ══════════════════════════════════════════════════════
npm install express          # Instalar paquete (dependencia)
npm install -D nodemon       # Instalar como devDependency
npm install                  # Instalar todas las dependencias del package.json

# Atajos
npm i express               # 'i' es alias de 'install'
npm i -D jest               # '-D' es alias de '--save-dev'

# ══════════════════════════════════════════════════════
# DESINSTALACIÓN
# ══════════════════════════════════════════════════════
npm uninstall express       # Desinstalar paquete
npm un express              # Atajo

# ══════════════════════════════════════════════════════
# OTROS COMANDOS ÚTILES
# ══════════════════════════════════════════════════════
npm list                    # Ver paquetes instalados
npm outdated                # Ver paquetes desactualizados
npm update                  # Actualizar paquetes
npm run <script>            # Ejecutar script del package.json
```

### package.json Explicado

```json
{
  "name": "mi-proyecto",
  "version": "1.0.0",
  "description": "Descripción de mi proyecto",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js",
    "test": "jest"
  },
  "keywords": ["nodejs", "api"],
  "author": "Tu Nombre",
  "license": "MIT",
  "dependencies": {
    "express": "^4.18.2"
  },
  "devDependencies": {
    "nodemon": "^3.0.1"
  }
}
```

### Versionado Semántico

```
Versión: MAJOR.MINOR.PATCH
         1.2.3

^1.2.3  → Acepta: 1.2.3, 1.2.9, 1.9.0 (NO 2.0.0)
~1.2.3  → Acepta: 1.2.3, 1.2.9 (NO 1.3.0)
1.2.3   → Solo acepta exactamente 1.2.3
```

---

## 🔄 Babel y ES6+

**Babel** permite usar las últimas características de JavaScript (ES6+) en entornos que no las soportan nativamente.

### ¿Por qué Babel?

```javascript
// ══════════════════════════════════════════════════════
// Código moderno (ES6+)
// ══════════════════════════════════════════════════════
const saludar = (nombre) => `¡Hola, ${nombre}!`;
const { a, b } = objeto;
import modulo from './modulo.js';

// ══════════════════════════════════════════════════════
// Babel lo transforma a código compatible (ES5)
// ══════════════════════════════════════════════════════
var saludar = function(nombre) {
    return "¡Hola, " + nombre + "!";
};
var a = objeto.a, b = objeto.b;
var modulo = require('./modulo.js');
```

### Instalación y Configuración

```bash
# Instalar Babel
npm install -D @babel/core @babel/cli @babel/preset-env @babel/node
```

```json
// babel.config.json
{
  "presets": [
    ["@babel/preset-env", {
      "targets": {
        "node": "current"
      }
    }]
  ]
}
```

```json
// package.json - scripts
{
  "scripts": {
    "start": "node dist/index.js",
    "dev": "babel-node src/index.js",
    "build": "babel src -d dist"
  }
}
```

---

## 🔄 Nodemon para Desarrollo

**Nodemon** reinicia automáticamente tu servidor cuando detecta cambios en los archivos.

### Sin Nodemon (tedioso) 😫

```bash
# Cambias código → Ctrl+C → node app.js → Cambias código → Ctrl+C → node app.js...
```

### Con Nodemon (automático) 🎉

```bash
npm install -D nodemon

# Ejecutar
npx nodemon app.js

# O configurar en package.json
"scripts": {
    "dev": "nodemon app.js"
}

# Y luego
npm run dev
```

### Configuración Avanzada (nodemon.json)

```json
{
  "watch": ["src"],
  "ext": "js,json",
  "ignore": ["node_modules", "test/*"],
  "exec": "babel-node src/index.js"
}
```

---

## 📂 Estructura del Proyecto

```
Node_JS_basic/
│
├── 📄 package.json          # Configuración del proyecto
├── 📄 babel.config.js       # Configuración de Babel
├── 📄 .eslintrc.js          # Configuración de ESLint
├── 📄 README.md             # Documentación (este archivo)
│
├── 📁 src/                  # Código fuente
│   ├── 📄 0-console.js      # Tarea 0: función displayMessage
│   ├── 📄 1-stdin.js        # Tarea 1: input del usuario
│   ├── 📄 2-read_file.js    # Tarea 2: lectura síncrona
│   ├── 📄 3-read_file_async.js  # Tarea 3: lectura asíncrona
│   ├── 📄 4-http.js         # Tarea 4: servidor HTTP básico
│   ├── 📄 5-http.js         # Tarea 5: servidor HTTP complejo
│   ├── 📄 6-http_express.js # Tarea 6: servidor Express básico
│   ├── 📄 7-http_express.js # Tarea 7: servidor Express complejo
│   └── 📁 full_server/      # Tarea 8+: servidor organizado
│       ├── 📁 controllers/
│       ├── 📁 routes/
│       └── 📄 server.js
│
├── 📁 database/             # Archivos de datos
│   └── 📄 database.csv
│
└── 📁 test/                 # Pruebas
    └── 📄 *.test.js
```

---

## ✅ Requisitos

### Entorno

| Requisito | Versión |
|-----------|---------|
| Ubuntu | 18.04 LTS |
| Node.js | 12.x.x |
| NPM | 6.x.x |

### Archivos de Configuración

Los siguientes archivos deben estar en la raíz del proyecto:

- `package.json`
- `babel.config.js`
- `.eslintrc.js`

### Comandos para Verificar

```bash
# Verificar versión de Node
node -v

# Verificar versión de NPM
npm -v

# Instalar dependencias
npm install

# Ejecutar linter
npm run lint

# Ejecutar con Babel
npm run dev
```

---

## 🎓 Resumen de Conceptos Clave

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONCEPTOS DE NODE.JS                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  🔹 Node.js = JavaScript fuera del navegador                    │
│                                                                 │
│  🔹 Event Loop = Maneja operaciones sin bloquear                │
│                                                                 │
│  🔹 NPM = Gestor de paquetes con millones de librerías         │
│                                                                 │
│  🔹 CommonJS = require() / module.exports                       │
│                                                                 │
│  🔹 ES Modules = import / export                                │
│                                                                 │
│  🔹 fs = Módulo para archivos                                   │
│                                                                 │
│  🔹 http = Módulo para servidores                               │
│                                                                 │
│  🔹 Express = Framework web popular                             │
│                                                                 │
│  🔹 Babel = Transpilador para ES6+                              │
│                                                                 │
│  🔹 Nodemon = Reinicio automático en desarrollo                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📚 Recursos Adicionales

### Documentación Oficial
- [Node.js Documentation](https://nodejs.org/docs/)
- [NPM Documentation](https://docs.npmjs.com/)
- [Express.js Guide](https://expressjs.com/)

### Tutoriales Recomendados
- [Node.js Best Practices](https://github.com/goldbergyoni/nodebestpractices)
- [JavaScript Info - Async](https://javascript.info/async)

### Herramientas Útiles
- [Postman](https://www.postman.com/) - Probar APIs
- [VS Code](https://code.visualstudio.com/) - Editor recomendado
- [Node.js REPL](https://nodejs.org/api/repl.html) - Experimentar con código

---

## 👨‍💻 Autor

**Proyecto de Holberton School**

---

<p align="center">
  <i>"Node.js no es solo una tecnología, es una forma de pensar en código asíncrono y eficiente."</i>
</p>

<p align="center">
  <b>¡Happy Coding! 🚀</b>
</p>
