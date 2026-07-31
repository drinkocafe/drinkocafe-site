// DrinKo Cafe static site — small progressive-enhancement helpers.
// No build step, no framework, no backend calls.

document.addEventListener('DOMContentLoaded', function () {
  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.primary-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var isOpen = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  }

  // FAQ accordion
  document.querySelectorAll('.faq-item').forEach(function (item) {
    var q = item.querySelector('.faq-q');
    if (!q) return;
    q.addEventListener('click', function () {
      var wasOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(function (o) { o.classList.remove('open'); });
      if (!wasOpen) item.classList.add('open');
    });
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
