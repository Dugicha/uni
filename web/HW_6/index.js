
const express = require("express")
const app = express()
const bodyParser = require("body-parser")
const path = require("path")

const STATIC_DIR = path.resolve(__dirname, "static")

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))
app.use(express.static(STATIC_DIR))

const getViewFile = (fileName) => path.resolve(STATIC_DIR, fileName)

let view_count = 0

// View counter middleware
app.use((req, res, next) => {
  view_count += 1
  next()
})

// Return view count for current runtime
app.get("/api/viewcount", (req, res) => {
  res.status(200).json({ view_count: view_count })
})

app.get("/", (req, res) => {
  res.status(200).sendFile(getViewFile("index.html"))
})

app.get("/posts", (req, res) => {
  res.status(200).sendFile(getViewFile("posts.html"))
})

app.get("/talks", (req, res) => {
  res.status(200).sendFile(getViewFile("talks.html"))
})


// Handle 404 with middleware
app.use((req, res, next) => {
  if (req.accepts("html")) {
    res.status(404).sendFile(getViewFile("404.html"))
    return;
  }

  if (req.accepts("json")) {
    res.status(404).json({ error: "404: Not found" })
    return;
  }

  res.status(404).type("txt").send("404: Not found")
})


const server = app.listen(8080, () => {
  console.log("Running on port", server.address().port)
})
