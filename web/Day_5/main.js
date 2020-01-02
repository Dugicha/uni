// main.js

const canvas = document.getElementById("canvas")
const ctx = canvas.getContext("2d")

ctx.fillStyle = "rgba(255, 0, 0, 0.4)"
ctx.fillRect(10, 10, 200, 200)

ctx.fillStyle = "rgba(0, 255, 0, 0.4)"
ctx.fillRect(100, 100, 200, 200)
