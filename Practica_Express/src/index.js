import express from "express";
import morgan from "morgan";
const servidor = express();
const PORT = 5000;

servidor.use(express.json());
// https://expressjs.com/en/resources/middleware/morgan.html#predefined-formats
servidor.use(morgan("dev"));

servidor.listen(PORT, () => {
  console.log(`Servidor Corriendo exitosamente en el puerto ${PORT}`);
});
