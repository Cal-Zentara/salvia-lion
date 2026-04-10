// ================================================================
//  SALVIA LION — app.js
// ================================================================

// ─── SCROLL REVEAL ──────────────────────────────────────────────
function initScrollReveal() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
}

// ─── TESTIMONIAL CAROUSEL ───────────────────────────────────────
function initCarousel() {
  const track = document.getElementById('carouselTrack');
  const dotsContainer = document.getElementById('carouselDots');
  if (!track || !dotsContainer) return;

  const cards = track.querySelectorAll('.testimonial-card');
  let current = 0;
  let autoTimer;

  // Build dots
  cards.forEach((_, i) => {
    const dot = document.createElement('button');
    dot.className = 'dot-btn' + (i === 0 ? ' active' : '');
    dot.setAttribute('aria-label', `Go to testimonial ${i + 1}`);
    dot.addEventListener('click', () => { goTo(i); resetTimer(); });
    dotsContainer.appendChild(dot);
  });

  function goTo(index) {
    current = index;
    track.style.transform = `translateX(-${current * 100}%)`;
    dotsContainer.querySelectorAll('.dot-btn').forEach((d, i) => {
      d.classList.toggle('active', i === current);
    });
  }

  function next() {
    goTo((current + 1) % cards.length);
  }

  function resetTimer() {
    clearInterval(autoTimer);
    autoTimer = setInterval(next, 5000);
  }

  resetTimer();

  document.getElementById('carouselPrev')?.addEventListener('click', () => {
    goTo((current - 1 + cards.length) % cards.length);
    resetTimer();
  });

  document.getElementById('carouselNext')?.addEventListener('click', () => {
    goTo((current + 1) % cards.length);
    resetTimer();
  });
}

// ─── 3D CARD TILT ───────────────────────────────────────────────
function initCardTilt() {
  document.querySelectorAll('.tilt-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;
      card.style.transform = `perspective(600px) rotateY(${x * 10}deg) rotateX(${-y * 10}deg) scale3d(1.02,1.02,1.02)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(600px) rotateY(0deg) rotateX(0deg) scale3d(1,1,1)';
    });
  });
}

// ─── MAGNETIC BUTTON ────────────────────────────────────────────
function initMagneticButtons() {
  document.querySelectorAll('.magnetic-btn').forEach(btn => {
    btn.addEventListener('mousemove', (e) => {
      const rect = btn.getBoundingClientRect();
      const x = (e.clientX - rect.left - rect.width / 2) * 0.3;
      const y = (e.clientY - rect.top - rect.height / 2) * 0.3;
      btn.style.transform = `translate(${x}px, ${y}px)`;
    });

    btn.addEventListener('mouseleave', () => {
      btn.style.transform = 'translate(0, 0)';
    });
  });
}

// ─── HORIZONTAL SCROLL (STEPS) ──────────────────────────────────
function initHorizontalScroll() {
  const el = document.getElementById('stepsScroll');
  if (!el) return;

  let isDown = false;
  let startX, scrollLeft;

  el.addEventListener('mousedown', (e) => {
    isDown = true;
    el.classList.add('grabbing');
    startX = e.pageX - el.offsetLeft;
    scrollLeft = el.scrollLeft;
  });

  el.addEventListener('mouseleave', () => { isDown = false; el.classList.remove('grabbing'); });
  el.addEventListener('mouseup', () => { isDown = false; el.classList.remove('grabbing'); });

  el.addEventListener('mousemove', (e) => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - el.offsetLeft;
    const walk = (x - startX) * 1.5;
    el.scrollLeft = scrollLeft - walk;
  });
}

// ─── NAV SCROLL SHADOW ──────────────────────────────────────────
function initNavScroll() {
  const nav = document.querySelector('.nav');
  if (!nav) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      nav.style.boxShadow = '0 4px 32px rgba(0,0,0,0.5)';
    } else {
      nav.style.boxShadow = 'none';
    }
  }, { passive: true });
}

// ─── FAQ ACCORDION ──────────────────────────────────────────────
function initFAQ() {
  document.querySelectorAll('.faq-question').forEach(btn => {
    btn.setAttribute('aria-expanded', 'false');
    btn.addEventListener('click', () => {
      const item = btn.parentElement;
      const isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(i => {
        i.classList.remove('open');
        i.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
      });
      if (!isOpen) {
        item.classList.add('open');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });
}

// ─── MOBILE NAV ─────────────────────────────────────────────────
function initMobileNav() {
  const hamburger = document.getElementById('navHamburger');
  const overlay = document.getElementById('mobileNavOverlay');
  if (!hamburger || !overlay) return;

  function closeMenu() {
    hamburger.classList.remove('open');
    overlay.classList.remove('open');
    hamburger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  hamburger.addEventListener('click', () => {
    const isOpen = overlay.classList.contains('open');
    if (isOpen) {
      closeMenu();
    } else {
      hamburger.classList.add('open');
      overlay.classList.add('open');
      hamburger.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
    }
  });

  overlay.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', closeMenu);
  });
}

// ─── THEME TOGGLE ───────────────────────────────────────────────
function initThemeToggle() {
  const btn = document.getElementById('themeToggle');
  if (!btn) return;

  const saved = storageGet('sl-theme');
  if (saved === 'light') {
    document.body.classList.add('light-mode');
    btn.textContent = '🌙';
  }

  btn.addEventListener('click', () => {
    document.body.classList.toggle('light-mode');
    const isLight = document.body.classList.contains('light-mode');
    btn.textContent = isLight ? '🌙' : '☀️';
    storageSet('sl-theme', isLight ? 'light' : 'dark');
  });
}

// ─── INIT ────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  initScrollReveal();
  initCarousel();
  initCardTilt();
  initMagneticButtons();
  initHorizontalScroll();
  initNavScroll();
  initThemeToggle();
  initFAQ();
  initMobileNav();
});
