// CommonJS Module
// sirve para indicar al compilador que se tiene que ejecutar de arriba hacia abajo
"use strict";
function sumar(num1, num2) {
  return num1 + num2;
}

function restar(num1, num2) {
  return num1 - num2;
}

// que es lo que voy a exportar de este archivo
module.exports = {
  sumar, // sumar : sumar
  restar,
};
