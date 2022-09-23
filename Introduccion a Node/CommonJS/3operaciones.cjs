"use strict";
// Esta es la forma de trabajar en los ESModule
// import { sumar } from "./2libreria";

// Esta es la forma de importar en CommonJs
const { sumar } = require("./2libreria.cjs");

const resultado = sumar(10, 6);
console.log(resultado);

// su formato es .cjs
