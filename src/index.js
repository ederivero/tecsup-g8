import express from "express";
import dotenv from "dotenv";
import { candidatosRouter } from "./routes/candidatos.routes.js";
// Carga el archivo .env a las variables de entorno para poder utilizarlas. Debe ir lo mas arriba posible en el proyecto, sobretodo en el archivo principal
dotenv.config();

const server = express();
const port = process.env.PORT ?? 5000;

// aceptar el body en formato JSON
server.use(express.json());

// Agregamos al middleware la informacion de las rutas del candidato
server.use(candidatosRouter);

server.listen(port, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${port}`);
});
