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
