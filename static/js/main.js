/**
 * AFRILOTT site-wide JavaScript entry point (Phase 2).
 * Initializes modules when their target DOM is present.
 */
(function () {
  "use strict";

  function onReady(callback) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", callback);
      return;
    }
    callback();
  }

  onReady(function () {
    if (window.AfltAOS) {
      if (document.querySelector(".petroleum-section")) {
        window.AfltAOS.initDetailPage();
      } else if (document.querySelector("[data-aos]")) {
        window.AfltAOS.initDefault();
      }
    }

    if (window.AfltRevealObserver) {
      window.AfltRevealObserver.init();
    }

    if (window.AfltServiceDetailEffects) {
      window.AfltServiceDetailEffects.init();
    }

    if (window.AfltHomeSlider && document.querySelector(".history-card-title")) {
      window.AfltHomeSlider.initHistorySlider(3000);
    }
  });
})();
