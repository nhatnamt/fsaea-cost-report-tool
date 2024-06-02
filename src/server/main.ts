import express from "express";
import ViteExpress from "vite-express";

const app = express();

app.get("/hello", (_, res) => {
  res.send("Hello Vite + React + TypeScript!");
});

const PORT = 3000;
ViteExpress.listen(app, PORT, () =>
  console.log(`Server is running on http://localhost:${PORT}`)
);
