const { Router } = require('express');
const router = Router();
const pool = require("./db");

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
})

module.exports = router;