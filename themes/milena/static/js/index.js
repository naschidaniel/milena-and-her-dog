import "../css/styles.css"

// ---- function Block ----

// Menu
function toggleMenu(){
  document.getElementById("nav-content").classList.toggle("hidden");
  document.getElementById("nav-button-open").classList.toggle("hidden");
  document.getElementById("nav-button-close").classList.toggle("hidden");
  }

function closeMenu(){
  if (window.innerWidth >= 640) {
    document.getElementById("nav-content").classList.add("hidden");
    document.getElementById("nav-button-close").classList.add("hidden");
    document.getElementById("nav-button-open").classList.remove("hidden");
  }
}

// slide show depending on screen size
function imgSlideShowMilena() {
  var imgElements = document.getElementsByTagName("img");
  for (let prop in Object.entries(imgElements)) {
    if (imgElements[prop].parentElement.id === 'img-slideshow') {
      if (window.innerWidth <= 640) {
        imgElements[prop].parentElement.classList.remove("flex")
        imgElements[prop].parentElement.classList.remove("justify-center")
        imgElements[prop].style.width = "100%"
      } else {
      const percentWidth = (100 - 10) / imgElements[prop].parentElement.childElementCount;
      imgElements[prop].parentElement.classList.add("flex")
      imgElements[prop].parentElement.classList.add("justify-center")
      imgElements[prop].style.width = `${percentWidth}%`
      }
    }
  }
}

// wrapper function
function actionOnResize() {
  closeMenu();
  imgSlideShowMilena();
}

// call functions on depending on actions
window.onload = imgSlideShowMilena;

window.onresize = actionOnResize;

document.getElementById("nav-toggle").onclick = toggleMenu;
