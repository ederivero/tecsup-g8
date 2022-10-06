import conexion from "../prisma.js";
import fetch from "node-fetch";

export const crearVotante = async (req, res) => {
  // DISCLAIMER: en este caso al ser la API gratuita no nos proporciona el ubigeo por lo que modificaremos el endpoint para recibir la region a la cual pertenece
  const { dni, regionId } = req.body;
  try {
    const respuesta = await fetch(`https://apiperu.dev/api/dni/${dni}`, {
      headers: {
        Authorization: `Bearer ${process.env.API_PERU_TOKEN}`,
        "Content-Type": "application/json",
      },
      method: "GET",
    });
    const informacion = await respuesta.json();

    console.log(informacion);
    if (informacion.success) {
      const { data } = informacion;
      const votanteCreado = await conexion.votante.create({
        data: {
          apellido: data.apellido_paterno + " " + data.apellido_materno,
          nombre: data.nombres,
          dni: data.numero,
          regionId,
        },
      });

      return res.status(201).json({
        message: "Votante creado exitosamente, puede votar",
        content: votanteCreado,
      });
    } else {
      return res.status(400).json({
        message: "Error al crear el votante",
        content: informacion.message,
      });
    }
  } catch (error) {
    // el parametro que retorna el catch SIEMPRE va a ser una instancia de la clase error
    // new Error('error')
    // name > mostrara el nombre del error
    // message > mostrara el mensaje del error
    // stack > (opcional) muestra el seguimiento del error

    return res.status(400).json({
      message: "Error al crear el votante",
      content: error.message,
    });
  }
};
