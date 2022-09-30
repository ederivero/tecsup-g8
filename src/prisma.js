import prisma from "@prisma/client";
// es crear una sola instancia para todo el proyecto
// tendremos como maximo una conexion a la bd y con esto evitamos tener un cuello de botella con tantas conexion abiertas
// A veces las BD no soportan muchas conexiones por lo que sino la sabemos controlar se saturaran y caera nuestra BD
// Patron Singleton > Patron de diseño de arch que sirve para indicar que como maximo tendremos por toda la aplicacion una sola instancia (creacion de una clase)
export default new prisma.PrismaClient();

// Para exportar podemos hacer de dos maneras
// aca estaremos indicando que vamos a exportar la variable x
// export const x = 10;

// y para la importacion sera:
// import {x} from '...'

// Si queremos exportar un valor por defecto (no hacer la destructuracion en la importacion)
// NOTA: solamente puede haber una exportacion por defecto
// export default 10

// para la importacion del valor por defecto
// import palabra from '...'

// Si solamente vamos a exportar una sola funcionabilidad entonces se recomienda que sea por defecto (default) pero sin embargo vamos a exportar varias variables, metodos, funciones , entro otros se recomienda la exportacion normal
