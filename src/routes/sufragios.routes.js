import { Router } from "express";
import { crearSufragio } from "../controllers/sufragios.controller.js";

export const sufragiosRouter = Router();

sufragiosRouter.post("/sufragio", crearSufragio);
