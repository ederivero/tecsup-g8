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

  await conexion.partidoPolitico.createMany({
    data: [
      {
        nombre: "Las uvas sabrosas",
        logo: "https://t3.ftcdn.net/jpg/05/32/87/20/240_F_532872053_Ux1cXZu0BWB4lyXJLs4D59jrqOyt8Wm8.jpg",
      },
      {
        nombre: "Los tres cerditos",
        logo: "https://t4.ftcdn.net/jpg/04/98/29/51/240_F_498295187_Knzh67lKqQjxyBrnNgMniaM4li06DIWf.jpg",
      },
      {
        nombre: "La nave espacial del futuro",
        logo: "https://t3.ftcdn.net/jpg/00/27/64/98/240_F_27649860_2MyaQ7hwMrZuYssYRkiFWj1bDH598iB1.jpg",
      },
      {
        nombre: "La naranja mecanica",
        logo: "https://t4.ftcdn.net/jpg/02/00/23/53/240_F_200235369_Hc2frRHwJlFmnweBGLAFcqxurU9ocH8j.jpg",
      },
    ],
    skipDuplicates: true,
  });

  console.log("Base de datos alimentada exitosamente");
}

alimentar();
