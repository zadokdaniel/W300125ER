import "dotenv/config";

import express from "express";
import cors from "cors";

const app = express();

app.use(
  cors({
    origin: "http://localhost:5173",
  }),
);

app.use(express.json());

app.get("/api/foo", (req, res) => {
  res.json("hello from backend");
});

app.use("/api", (req, res) => {
  res.json({ message: "hello from api" });
});

const PORT = process.env.NODE_PORT || 5000;
app.listen(PORT, () => console.log(`server is running on port ${PORT}`));
