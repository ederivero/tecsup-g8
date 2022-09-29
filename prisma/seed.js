// el seed sirve para alimentar nuestra bd con determinada informacion que nunca va a cambiar, tbn se utiliza para crear data de prueba
import prisma from "@prisma/client";
const { PrismaClient } = prisma;
const conexion = new PrismaClient();

async function alimentar() {
  console.log("Iniciando el seeding");

  await conexion.region.createMany({
    data: [
      { nombre: "Amazonas" },
      { nombre: "Ancash" },
      { nombre: "Apurimac" },
      { nombre: "Arequipa" },
      { nombre: "Ayacucho" },
      { nombre: "Cajamarca" },
      { nombre: "Callao" },
      { nombre: "Cusco" },
      { nombre: "Huancavelica" },
      { nombre: "Huanuco" },
      { nombre: "Ica" },
      { nombre: "Junín" },
      { nombre: "La Libertad" },
      { nombre: "Lambayeque" },
      { nombre: "Lima" },
      { nombre: "Loreto" },
      { nombre: "Madre de Dios" },
      { nombre: "Moquegua" },
      { nombre: "Pasco" },
      { nombre: "Piura" },
      { nombre: "Puno" },
      { nombre: "San Martín" },
      { nombre: "Tacna" },
      { nombre: "Tumbes" },
      { nombre: "Ucayali" },
    ],
    skipDuplicates: true,
  });

  console.log("Base de datos alimentada exitosamente");
}

alimentar();
