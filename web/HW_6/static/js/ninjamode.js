const ninjutsu = () => {
  const body = document.getElementsByTagName("body")[0]
  body.classList.add("ninja")
}

window.onload = () => {
  let ninjamode = localStorage.getItem("ninjamode")

  if (ninjamode == "true")
    ninjutsu()
  document.querySelector("#ninja-btn").addEventListener("click", () => {
    localStorage.setItem("ninjamode", "true")
    ninjutsu()
  })
}
