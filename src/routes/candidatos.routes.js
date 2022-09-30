import { Router } from "express";
import { crearCandidato } from "../controllers/candidatos.controller.js";

export const candidatosRouter = Router();

candidatosRouter.post("/candidato", crearCandidato);
