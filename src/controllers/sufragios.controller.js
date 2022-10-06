import conexion from "../prisma.js";

export const crearSufragio = async (req, res) => {
  const { candidatoId, votanteId } = req.body;
  try {
    // Buscar si el candidatoId existe
    await conexion.candidato.findUniqueOrThrow({ where: { id: candidatoId } });
    // Buscar si el votanteId existe
    await conexion.votante.findUniqueOrThrow({ where: { dni: votanteId } });
    // Buscar si ya hay un sufragio con ese votanteId
    const sufragio = await conexion.sufragio.findFirst({
      where: { votanteId },
    });

    if (sufragio) {
      return res.status(400).json({
        message: "El votante ya realizo su voto",
        content: null,
      });
    }

    await conexion.sufragio.create({
      data: {
        candidatoId,
        votanteId,
      },
    });

    return res.status(201).json({
      message: "Se registro el voto exitosamente",
    });
  } catch (error) {
    return res.status(400).json({
      message: "Error al registrar el sufragio",
      content: error.message,
    });
  }
};

export const listarResultados = async (req, res) => {
  // aca devolveremos los candidatos filtrados por region y su cantidad de votos
  // http://127.0.0.1:5000/sufragio/AREQUIPA
  const { region } = req.params;
  console.log(region);

  // SELECT * FROM sufragios INNER JOIN candidatos ON sufragios.candidato_id = candidatos.id INNER JOIN regiones ON candidatos.region_id = regiones.id WHERE regiones.nombre = 'AREQUIPA';
  const data = await conexion.sufragio.findMany({
    where: {
      candidate: {
        region: {
          nombre: region,
        },
      },
    },
  });
  return res.status(200).json({
    message: null,
    content: data,
  });
};
