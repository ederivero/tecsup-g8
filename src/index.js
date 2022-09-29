import express from "express";
import dotenv from "dotenv";
// Carga el archivo .env a las variables de entorno para poder utilizarlas. Debe ir lo mas arriba posible en el proyecto, sobretodo en el archivo principal
dotenv.config();

const server = express();
const port = process.env.PORT ?? 5000;

server.listen(port, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${port}`);
});
