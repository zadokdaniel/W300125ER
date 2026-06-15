import "dotenv/config";

import express from "express";
import cors from "cors";
import APIRoute from "./routes/api.route.js";
import staticSiteFallbackRoute from "./routes/staticSiteFallback.route.js";

const app = express();

app.use(cors());

app.use(express.json());

app.use("/api", APIRoute);

app.use(staticSiteFallbackRoute);

const PORT = process.env.NODE_PORT || 5000;
app.listen(PORT, () => console.log(`server is running on port ${PORT}`));
