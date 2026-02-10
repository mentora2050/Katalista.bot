import express from "express";
import cors from "cors";

const app = express();
app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
  res.send("API شغالة ✅");
});

app.post("/chat", (req, res) => {
  res.json({
    reply: "ده رد تجريبي"
  });
});

app.listen(3000);
