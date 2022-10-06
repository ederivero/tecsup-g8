import { Router } from "express";
import {
  crearSufragio,
  listarResultados,
} from "../controllers/sufragios.controller.js";

export const sufragiosRouter = Router();

sufragiosRouter.post("/sufragio", crearSufragio);
sufragiosRouter.get("/sufragio/:region", listarResultados);
