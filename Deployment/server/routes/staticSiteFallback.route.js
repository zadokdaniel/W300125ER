import path from "path";

import express from "express";

const route = express.Router();

const DIST_DIRECTORY = path.resolve(process.cwd(), "./dist");

route.use(express.static(DIST_DIRECTORY));

route.use((req, res) => {
  res.sendFile(DIST_DIRECTORY, "./index.html");
});

export default route;
