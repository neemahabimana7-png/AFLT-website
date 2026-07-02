/**
 * About page history section text slider (.history-card-title + .history-dots).
 * Home hero carousel uses Bootstrap data-bs-ride and needs no custom JS.
 */
(function () {
  "use strict";

  function initHistorySlider(intervalMs) {
    var slides = document.querySelectorAll(".history-card-title");
    var dots = document.querySelectorAll(".history-dots .dot");

    if (!slides.length || !dots.length) {
      return;
    }

    var currentSlide = 0;
    var totalSlides = slides.length;
    var delay = intervalMs || 3000;

    function showSlide(index) {
      slides.forEach(function (slide) {
        slide.classList.remove("active");
        slide.style.opacity = "0";
        slide.style.transform = "translateX(20px)";
      });
      dots.forEach(function (dot) {
        dot.classList.remove("active");
      });

      slides[index].classList.add("active");
      slides[index].style.opacity = "1";
      slides[index].style.transform = "translateX(0)";
      dots[index].classList.add("active");
    }

    function nextSlide() {
      currentSlide = (currentSlide + 1) % totalSlides;
      showSlide(currentSlide);
    }

    dots.forEach(function (dot, index) {
      dot.addEventListener("click", function () {
        currentSlide = index;
        showSlide(currentSlide);
      });
    });

    showSlide(0);
    window.setInterval(nextSlide, delay);
  }

  window.AfltHomeSlider = {
    initHistorySlider: initHistorySlider,
  };
})();
