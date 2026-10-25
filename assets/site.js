// Pauk — petits comportements du site (menu mobile, en-tête, dates, copie)
(function () {
  // Menu mobile
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  // Trait sous l'en-tête dès qu'on fait défiler
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () { header.classList.toggle('scrolled', window.scrollY > 8); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // Les dates dont data-end est passé disparaissent toutes seules de la setlist
  var today = new Date();
  today.setHours(0, 0, 0, 0);
  document.querySelectorAll('.setlist li[data-end]').forEach(function (li) {
    var end = new Date(li.getAttribute('data-end') + 'T23:59:59');
    if (!isNaN(end) && end < today) li.hidden = true;
  });
  document.querySelectorAll('.setlist').forEach(function (list) {
    var visible = list.querySelectorAll('li:not([hidden])').length;
    var empty = list.parentElement.querySelector('.setlist-empty');
    if (empty) empty.hidden = visible > 0;
  });

  // Boutons « Copier » (bio presse)
  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var src = document.getElementById(btn.getAttribute('data-copy'));
      if (!src) return;
      var text = src.innerText.trim();
      var done = function () {
        var label = btn.textContent;
        btn.textContent = 'Copié';
        setTimeout(function () { btn.textContent = label; }, 1600);
      };
      var fallback = function () {
        var range = document.createRange();
        range.selectNodeContents(src);
        var sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
        btn.textContent = 'Texte sélectionné';
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, fallback);
      } else {
        fallback();
      }
    });
  });
})();
