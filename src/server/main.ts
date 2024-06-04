import express from "express";
import ViteExpress from "vite-express";
import mongoose from "mongoose";


const app = express();

app.get("/hello", (_, res) => {
  res.send("Hello Vite + React + TypeScript!");
});

mongoose.connect('mongodb+srv://general:rT7jfSoj8Wv9T6NZ@cluster0.4byppj8.mongodb.net/')

async function listDatabases(client: any){
  const databaseList = await client.db.admin().listDatabases();
  console.log(databaseList);
};

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', () => {
  console.log('Connected to MongoDB');
  // List all databases
  listDatabases(db);
});

const PORT = 3000;
ViteExpress.listen(app, PORT, () =>
  console.log(`Server is running on http://localhost:${PORT}`)
);
