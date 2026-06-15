import express from "express";

const route = express.Router();

route.get("/foo", (req, res) => {
  res.json("hello from backend");
});

route.use("", (req, res) => {
  res.json({ message: "hello from api" });
});

export default route;
