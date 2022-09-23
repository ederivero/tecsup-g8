import express from "express";

const servidor = express();

const PUERTO = 5000;

servidor.get("/", (req, res) => {
  res.json({
    message: "Bienvenido a mi API",
  });
});

servidor.listen(PUERTO, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PUERTO}`);
});
