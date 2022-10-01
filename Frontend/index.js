async function consultar() {
  try {
    const respuesta = await fetch("http://localhost:3000/candidato", {
      method: "GET",
    });
    console.log(respuesta);
    console.log(respuesta.status);
    console.log(await respuesta.json());
    console.log("La peticion fue exitosa");
  } catch (error) {
    console.log("Hubo un error al hacer la peticion");
  }
  //   .then((respuesta) => {
  //     console.log("La peticion fue exitosa");
  //   })
  //   .catch((error) => {
  //     console.log("Hubo un error al hacer la peticion");
  //   });
}

consultar();

const crearCandidato = document.getElementById("btn-crear");
const dni = document.getElementById("dni");

async function registrar(evento) {
  evento.preventDefault();
  console.log("me hizo click");
  console.log(dni.value);
  const valorDni = dni.value;

  if (valorDni === "") {
    alert("DNI no puede ser vacio");
  }

  try {
    const resultado = await fetch("http://localhost:3000/votante", {
      method: "POST",
      body: JSON.stringify({ dni: valorDni }), // { dni :'73500746'} > '{ "dni":"73500746" }'
      headers: { "Content-Type": "application/json" },
    });
    const json = await resultado.json();

    if (resultado.status == 400) {
      alert(json.content);
    } else {
      alert("EXITOS!");
      // TODO: redireccionar a la pagina de votacion
    }

    console.log(json);
  } catch (error) {
    console.error("Error al crear el votante");
  }
}

crearCandidato.addEventListener("click", registrar);
