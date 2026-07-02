/**
 * Scroll-reveal via IntersectionObserver.
 * Supports .reveal-up (subsidiaries list) and .afos-reveal (AFOS page).
 */
(function () {
  "use strict";

  function observeElements(selector, visibleClass, options) {
    var items = document.querySelectorAll(selector);
    if (!items.length) {
      return;
    }

    var settings = Object.assign(
      { threshold: 0.18, rootMargin: "0px" },
      options || {}
    );

    if ("IntersectionObserver" in window) {
      var observer = new IntersectionObserver(function (entries, obs) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add(visibleClass);
            obs.unobserve(entry.target);
          }
        });
      }, settings);

      items.forEach(function (item) {
        observer.observe(item);
      });
      return;
    }

    items.forEach(function (item) {
      item.classList.add(visibleClass);
    });
  }

  function initRevealObserver() {
    observeElements(".reveal-up", "is-visible", { threshold: 0.18 });

    var afosItems = document.querySelectorAll(".afos-reveal");
    if (afosItems.length) {
      document.documentElement.classList.add("js-motion");
      observeElements(".afos-reveal", "afos-visible", {
        threshold: 0.18,
        rootMargin: "0px 0px -4% 0px",
      });
    }
  }

  window.AfltRevealObserver = {
    init: initRevealObserver,
    observeElements: observeElements,
  };
})();
