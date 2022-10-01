import { Router } from "express";
import { crearVotante } from "../controllers/votantes.controller.js";

export const votantesRouter = Router();

votantesRouter.post("/votante", crearVotante);
