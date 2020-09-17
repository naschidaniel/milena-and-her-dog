// toggle the menu
document.getElementById("nav-toggle").onclick = function(){
  document.getElementById("nav-content").classList.toggle("hidden");
  document.getElementById("nav-button-open").classList.toggle("hidden");
  document.getElementById("nav-button-close").classList.toggle("hidden");
  }

  // close menu on window width >= 640
  function reportWindowSize() {
    if (window.innerWidth >= 640) {
      document.getElementById("nav-content").classList.add("hidden");
      document.getElementById("nav-button-close").classList.add("hidden");
      document.getElementById("nav-button-open").classList.remove("hidden");
    }
  }
  window.onresize = reportWindowSize;
