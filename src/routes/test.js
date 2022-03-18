const { Router } = require('express');
const router = Router();
const pool = require("./db");

router.post("/addTest", (req, res) => {
  const { name, description, duration, price, category, image } = req.body;
  pool.query(
    "INSERT INTO test (name, description, duration, price, category, image) VALUES ($1, $2, $3, $4, $5, $6)",
    [name, description, duration, price, category, image],
    (error, results) => {
      if (error) {
        throw error;
      }
      res.status(200).send(`Test added with ID: ${results.insertId}`);
    }
  );
})

module.exports = router;