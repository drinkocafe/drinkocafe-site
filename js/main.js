// DrinKo Cafe static site — small progressive-enhancement helpers.
// No build step, no framework, no backend calls.

document.addEventListener('DOMContentLoaded', function () {
  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var navRow = document.querySelector('.nav-row');
  if (toggle && navRow) {
    toggle.addEventListener('click', function () {
      var isOpen = navRow.classList.toggle('open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  }

  // Slideshow (counter-style, matches the real theme's gallery section)
  document.querySelectorAll('.slideshow').forEach(function (slideshow) {
    var track = slideshow.querySelector('.slideshow-track');
    var slides = track ? track.children.length : 0;
    var counter = slideshow.querySelector('.slideshow-counter');
    var index = 0;
    function update() {
      track.style.transform = 'translateX(-' + (index * 100) + '%)';
      if (counter) counter.textContent = (index + 1) + ' / ' + slides;
    }
    var prev = slideshow.querySelector('.slideshow-nav.prev');
    var next = slideshow.querySelector('.slideshow-nav.next');
    if (prev) prev.addEventListener('click', function () { index = (index - 1 + slides) % slides; update(); });
    if (next) next.addEventListener('click', function () { index = (index + 1) % slides; update(); });
    update();
  });

  // Forms have no backend on a static host. Rather than fail silently,
  // route submissions to a mailto link so a message is never lost.
  document.querySelectorAll('form[data-mailto]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var to = form.getAttribute('data-mailto');
      var data = new FormData(form);
      var lines = [];
      data.forEach(function (value, key) { if (value) lines.push(key + ': ' + value); });
      var subject = encodeURIComponent(form.getAttribute('data-subject') || 'Message from drinkocafe.com');
      var body = encodeURIComponent(lines.join('\n'));
      window.location.href = 'mailto:' + to + '?subject=' + subject + '&body=' + body;
    });
  });
});
