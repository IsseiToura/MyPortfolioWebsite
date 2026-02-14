/**
 * navigation.js - Common navigation functionality for all pages
 * Handles navbar scroll effects, active link highlighting, mobile menu, and scroll animations
 */

// ==================== Navigation Scroll Effect ====================
window.addEventListener('scroll', function() {
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }
});

// ==================== Active Link Highlighting ====================
const sections = document.querySelectorAll('section[class*="container-fluid"]');
const navLinks = document.querySelectorAll('.nav-link, .navbar-brand');

window.addEventListener('scroll', function() {
  let current = '';
  
  // Get navbar height dynamically
  const navbar = document.querySelector('.navbar');
  const navbarHeight = navbar ? navbar.offsetHeight : 80;
  
  // Adjust offset based on screen size (matching CSS scroll-margin-top)
  let offset;
  if (window.innerWidth < 768) {
    offset = 100; // Mobile - matches CSS scroll-margin-top
  } else if (window.innerWidth < 1200) {
    offset = 120; // Tablet - matches CSS scroll-margin-top
  } else {
    offset = 130; // Desktop - matches CSS scroll-margin-top
  }
  
  // Get hero section (jumbotron) height
  const heroSection = document.querySelector('.jumbotron');
  const heroHeight = heroSection ? heroSection.offsetHeight : 0;
  
  // Check if we're at the bottom of the page
  const scrollPosition = window.pageYOffset + window.innerHeight;
  const pageHeight = document.documentElement.scrollHeight;
  const isAtBottom = scrollPosition >= pageHeight - 100;
  
  // If in hero section, don't activate any link
  if (window.pageYOffset < heroHeight - navbarHeight) {
    current = ''; // Keep empty to not activate any link
  }
  // If at bottom, force the last section (contact) to be active
  else if (isAtBottom) {
    const lastSection = sections[sections.length - 1];
    const anchor = lastSection?.querySelector('[id$="_anchor"]');
    if (anchor) {
      current = anchor.getAttribute('id');
    }
  } else {
    // Normal scroll detection
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.clientHeight;
      const scrollPos = window.pageYOffset + offset;
      
      // Check if scroll position is within this section
      if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
        const anchor = section.querySelector('[id$="_anchor"]');
        if (anchor) {
          current = anchor.getAttribute('id');
        }
      }
    });
  }

  navLinks.forEach(link => {
    link.classList.remove('active');
    if (current && link.getAttribute('href')?.includes(current)) {
      link.classList.add('active');
    }
  });
});

// ==================== Close Mobile Menu on Link Click ====================
document.addEventListener('DOMContentLoaded', function() {
  const navLinks = document.querySelectorAll('.nav-link, .navbar-brand');
  const menuToggle = document.getElementById('navbarNav');
  const navbarToggler = document.querySelector('.navbar-toggler');

  navLinks.forEach(link => {
    link.addEventListener('click', function() {
      // Check if menu is open (on mobile)
      if (menuToggle && menuToggle.classList.contains('show')) {
        // Use Bootstrap's collapse method to close menu
        const bsCollapse = bootstrap.Collapse.getInstance(menuToggle);
        if (bsCollapse) {
          bsCollapse.hide();
        } else {
          // Fallback: manually remove the 'show' class
          menuToggle.classList.remove('show');
          if (navbarToggler) {
            navbarToggler.classList.add('collapsed');
            navbarToggler.setAttribute('aria-expanded', 'false');
          }
        }
      }
    });
  });
});

// ==================== Intersection Observer for Scroll Animations ====================
document.addEventListener('DOMContentLoaded', function() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, observerOptions);

  // Observe all animated elements
  const animatedElements = document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right, .scale-in, .stagger-item');
  animatedElements.forEach(el => observer.observe(el));
});
