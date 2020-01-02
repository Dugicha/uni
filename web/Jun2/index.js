const express = require("express")
const path = require("path")
const controllers = require("./controllers")

const app = express()
const PORT = process.env.PORT || 3000

app.get("/", (req, res) => {
  res.send("el slasho boio")
})

app.listen(PORT, () => {
  console.log(`Listening on port ${PORT}`)
})
