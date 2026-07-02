/**
 * Service detail page effects: panel height sync and image parallax.
 * Used on pages with .petroleum-content and .petroleum-images.
 */
(function () {
  "use strict";

  function syncServicePanelHeight() {
    var left = document.querySelector(".petroleum-content");
    var panel = document.querySelector(".petroleum-images");

    if (!left || !panel) {
      return;
    }

    if (window.innerWidth > 991) {
      panel.style.minHeight = left.offsetHeight + "px";
    } else {
      panel.style.minHeight = "";
    }
  }

  function setupImageParallax() {
    var wrap = document.querySelector(".petroleum-images");
    var main = document.querySelector(".main-image");
    var small = document.querySelector(".small-image");

    if (!wrap || !main || !small || window.innerWidth <= 991) {
      return;
    }

    if (wrap.dataset.parallaxBound === "true") {
      return;
    }
    wrap.dataset.parallaxBound = "true";

    wrap.addEventListener("mousemove", function (event) {
      var rect = wrap.getBoundingClientRect();
      var x = (event.clientX - rect.left) / rect.width - 0.5;
      var y = (event.clientY - rect.top) / rect.height - 0.5;

      main.style.transform =
        "translate3d(" + x * 8 + "px," + y * 10 + "px,0)";
      small.style.transform =
        "translate3d(" + x * -10 + "px," + y * -8 + "px,0)";
    });

    wrap.addEventListener("mouseleave", function () {
      main.style.transform = "";
      small.style.transform = "";
    });
  }

  function initServiceDetailEffects() {
    if (!document.querySelector(".petroleum-section")) {
      return;
    }

    syncServicePanelHeight();
    setupImageParallax();

    window.addEventListener("resize", syncServicePanelHeight);
    window.addEventListener("resize", setupImageParallax);
  }

  window.AfltServiceDetailEffects = {
    init: initServiceDetailEffects,
    syncServicePanelHeight: syncServicePanelHeight,
    setupImageParallax: setupImageParallax,
  };
})();
