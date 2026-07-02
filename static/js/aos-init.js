/**
 * AOS (Animate On Scroll) initialization.
 * Requires https://unpkg.com/aos@2.3.1/dist/aos.js loaded before this file.
 */
(function () {
  "use strict";

  var DEFAULT_OPTIONS = {
    duration: 1200,
    easing: "ease-out-cubic",
    once: true,
    offset: 120,
    delay: 100,
  };

  var DETAIL_PAGE_OPTIONS = {
    duration: 1000,
    easing: "ease-out-cubic",
    once: true,
    offset: 90,
    delay: 60,
  };

  function initAOS(options) {
    if (typeof AOS === "undefined") {
      return;
    }

    AOS.init(options || DEFAULT_OPTIONS);
  }

  window.AfltAOS = {
    init: initAOS,
    initDefault: function () {
      initAOS(DEFAULT_OPTIONS);
    },
    initDetailPage: function () {
      initAOS(DETAIL_PAGE_OPTIONS);
    },
    DEFAULT_OPTIONS: DEFAULT_OPTIONS,
    DETAIL_PAGE_OPTIONS: DETAIL_PAGE_OPTIONS,
  };
})();
