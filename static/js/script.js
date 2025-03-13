document.querySelectorAll(".tableau").forEach((tableau) => {
  tableau.addEventListener("mouseenter", () => {
    tableau.querySelector(".tbl-details").style.opacity = "1";
  });

  tableau.addEventListener("mouseleave", () => {
    tableau.querySelector(".tbl-details").style.opacity = "0";
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const fadeInElements = document.querySelectorAll(".fade-in-element");

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
        }
      });
    },
    { threshold: 0.03 }
  );

  fadeInElements.forEach((element) => {
    observer.observe(element);
  });
});

let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides((slideIndex += n));
}

function currentSlide(n) {
  showSlides((slideIndex = n));
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("demo");
  let captionText = document.getElementById("caption");

  if (n > slides.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = slides.length;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }

  if (slides[slideIndex - 1]) {
    slides[slideIndex - 1].style.display = "block";
  }
  if (dots[slideIndex - 1]) {
    dots[slideIndex - 1].className += " active";
    captionText.innerHTML = dots[slideIndex - 1].alt;
  }
}

// Fonction pour gérer les touches du clavier
document.addEventListener("keydown", function (event) {
  if (event.key === "ArrowLeft") {
    // Flèche gauche : bouton Prev
    document.getElementById("btn-prev").click();
  } else if (event.key === "ArrowRight") {
    // Flèche droite : bouton Next
    document.getElementById("btn-next").click();
  }
});

document.addEventListener("DOMContentLoaded", function () {
  // Éléments principaux
  const hamburger = document.getElementById("hamburger");
  const navLinks = document.getElementById("nav-links");
  const faBars = document.querySelector(".fa-bars");

  // Gestion du menu hamburger
  hamburger.addEventListener("click", (e) => {
    e.stopPropagation();
    const isOpening = !navLinks.classList.contains("active");

    // Basculer l'état du menu
    navLinks.classList.toggle("active");
    faBars.classList.toggle("fa-times");

    // Gestion du défilement de la page
    document.body.classList.toggle("menu-open", isOpening);

    // Fermeture des sous-menus si fermeture complète
    if (!isOpening) {
      document.querySelectorAll(".nav-links ul").forEach((sub) => {
        sub.classList.remove("mobile-visible");
      });
    }
  });

  // Gestion des sous-menus multi-niveaux
  document.querySelectorAll(".nav-links li").forEach((item) => {
    const link = item.querySelector("a");
    const submenu = item.querySelector("ul");

    if (submenu) {
      link.addEventListener("click", function (e) {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          const wasVisible = submenu.classList.contains("mobile-visible");

          // Fermer les dropdowns frères du même niveau
          if (!wasVisible) {
            const parentList = item.parentElement;
            parentList.querySelectorAll("li").forEach((sibling) => {
              if (sibling !== item) {
                const siblingSubmenu = sibling.querySelector("ul");
                if (siblingSubmenu) {
                  siblingSubmenu.classList.remove("mobile-visible");
                  // Fermer aussi les sous-menus enfants
                  siblingSubmenu.querySelectorAll("ul").forEach((child) => {
                    child.classList.remove("mobile-visible");
                  });
                }
              }
            });
          }

          // Basculer uniquement ce sous-menu
          submenu.classList.toggle("mobile-visible");

          // Gestion hiérarchique
          if (wasVisible) {
            // Fermer les enfants si on ferme le parent
            submenu.querySelectorAll("ul").forEach((childSub) => {
              childSub.classList.remove("mobile-visible");
            });
          } else {
            // Ouvrir les parents nécessaires
            let parentMenu = item.parentElement.closest("ul");
            while (parentMenu) {
              parentMenu.classList.add("mobile-visible");
              parentMenu = parentMenu.parentElement.closest("ul");
            }
          }

          e.stopImmediatePropagation();
        }
      });
    }
  });

  // Fermeture au clic externe
  document.addEventListener("click", (e) => {
    if (!e.target.closest(".primary-navigation") && window.innerWidth <= 768) {
      navLinks.classList.remove("active");
      faBars.classList.remove("fa-times");
      document.querySelectorAll(".nav-links ul").forEach((sub) => {
        sub.classList.remove("mobile-visible");
      });
      document.body.classList.remove("menu-open");
    }
  });

  // Optimisation du défilement tactile
  let touchStartY = 0;
  const SWIPE_THRESHOLD = 50;

  navLinks.addEventListener(
    "touchstart",
    (e) => {
      touchStartY = e.touches[0].clientY;
    },
    { passive: true }
  );

  navLinks.addEventListener(
    "touchmove",
    (e) => {
      const touchEndY = e.touches[0].clientY;
      const deltaY = touchEndY - touchStartY;

      // Contrôle du défilement naturel
      if (Math.abs(deltaY) > SWIPE_THRESHOLD) {
        e.stopPropagation();
      }
    },
    { passive: false }
  );
});
