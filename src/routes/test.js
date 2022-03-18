const { Router } = require('express');
const router = Router();
const pool = require("./db");

router.post("/addTest", (req, res) => {
  const { test } = req.body;
  pool.query(
    "INSERT INTO test (test) VALUES ($1)",
    [test],
    (error, results) => {
      if (error) {
        throw error;
      }
      res.status(200).send(`Test added with ID: ${results}`);
    }
  );
})

module.exports = router;