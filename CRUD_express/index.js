import express from "express";

const servidor = express();

// Configurando la forma en la cual puede enviar informacion por el body
// use() > recibe middleware (intermediario entre el controlador final y la peticion)
// express.json() > middleware que convertira la informacion entrante del body y la transformara a un json legible mediante req.body
servidor.use(express.json());

const PUERTO = 5000;

servidor.get("/", (req, res) => {
  res.json({
    message: "Bienvenido a mi primera API de express y algo mas",
  });
});

servidor.post("/registro", (req, res) => {
  // req => la informacion que me llega del usuario
  // res => la informacion que voy a enviar como respuesta
  console.log(req.body);
  // Es IMPORTANTE siempre devolver alguna respuesta
  return res.json({
    message: "Registro creado exitosamente",
  });
  // No se puede utilizar el res mas de una vez
  // Si se utiliza en return ningun codigo siguiente sera accesible
  // console.log("Yo funcione despues de enviar la respuesta");
});

servidor.put("/actualizar-usuario/:id", (req, res) => {
  // Para acceder a los parametros seteados en la URL usamos req.params y siempre llegaran en string
  console.log(req.params);

  res.json({
    message: "Usuario actualizado exitosamente",
  });
});

servidor.get("/buscar-usuario", (req, res) => {
  // para acceder a los query params se hace mediante la propiedad req.query
  console.log(req.query);

  res.json({
    message: "No se encontro el usuario a buscar",
  });
});

// si queremos usar el mismo endpoint para diferentes metodos HTTP (get, post , put , delete, etc)
servidor
  .route("/productos")
  .get((req, res) => {
    res.json({
      message: "Soy el get",
    });
  })
  .post((req, res) => {
    res.json({
      message: "Soy el post",
    });
  })
  .delete((req, res) => {
    res.json({
      message: "Soy el delete",
    });
  });

servidor.listen(PUERTO, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PUERTO}`);
});
