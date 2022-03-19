const { Router } = require('express');
const router = Router();
const pool = require("./db");

<<<<<<< Updated upstream
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
=======
router.post("/addTest", async (req, res) => {
  try {
    const { test } = req.body;
    const validate_login = await pool.query(
      "INSERT INTO test (test) VALUES ($1)",
      [test]
    );
    res.status(200).send({ code: 1, validate_login });
  } catch (err) {
    console.error(`-------------ERROR-------------\n${err.message}`);
    res.status(200).send({ code: 0, error: err.message });
  }
>>>>>>> Stashed changes
})

module.exports = router;