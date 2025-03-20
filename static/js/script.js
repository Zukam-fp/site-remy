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

document.addEventListener("keydown", function (event) {
  if (event.key === "ArrowLeft") {
    document.getElementById("btn-prev").click();
  } else if (event.key === "ArrowRight") {
    document.getElementById("btn-next").click();
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const hamburger = document.getElementById("hamburger");
  const navLinks = document.getElementById("nav-links");
  const faBars = document.querySelector(".fa-bars");

  hamburger.addEventListener("click", (e) => {
    e.stopPropagation();
    const isOpening = !navLinks.classList.contains("active");

    navLinks.classList.toggle("active");
    faBars.classList.toggle("fa-times");

    document.body.classList.toggle("menu-open", isOpening);

    if (!isOpening) {
      document.querySelectorAll(".nav-links ul").forEach((sub) => {
        sub.classList.remove("mobile-visible");
      });
    }
  });

  document.querySelectorAll(".nav-links li").forEach((item) => {
    const link = item.querySelector("a");
    const submenu = item.querySelector("ul");

    if (submenu) {
      link.addEventListener("click", function (e) {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          const wasVisible = submenu.classList.contains("mobile-visible");

          if (!wasVisible) {
            const parentList = item.parentElement;
            parentList.querySelectorAll("li").forEach((sibling) => {
              if (sibling !== item) {
                const siblingSubmenu = sibling.querySelector("ul");
                if (siblingSubmenu) {
                  siblingSubmenu.classList.remove("mobile-visible");

                  siblingSubmenu.querySelectorAll("ul").forEach((child) => {
                    child.classList.remove("mobile-visible");
                  });
                }
              }
            });
          }

          submenu.classList.toggle("mobile-visible");

          if (wasVisible) {
            submenu.querySelectorAll("ul").forEach((childSub) => {
              childSub.classList.remove("mobile-visible");
            });
          } else {
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

      if (Math.abs(deltaY) > SWIPE_THRESHOLD) {
        e.stopPropagation();
      }
    },
    { passive: false }
  );
});

document.addEventListener("DOMContentLoaded", function () {
  const isMobile = window.matchMedia("(max-width: 767px)").matches;
  const tableauImage = document.querySelector(".tableau-image");
  const btnPrev = document.getElementById("btn-prev");
  const btnNext = document.getElementById("btn-next");

  if (isMobile && tableauImage && btnPrev && btnNext) {
    let touchStartX = 0;
    let touchEndX = 0;
    const swipeThreshold = 50;

    tableauImage.addEventListener(
      "touchstart",
      function (e) {
        touchStartX = e.touches[0].clientX;
      },
      { passive: true }
    );

    tableauImage.addEventListener(
      "touchend",
      function (e) {
        touchEndX = e.changedTouches[0].clientX;
        handleSwipeGesture();
      },
      { passive: true }
    );

    function handleSwipeGesture() {
      const deltaX = touchEndX - touchStartX;

      if (Math.abs(deltaX) > swipeThreshold) {
        if (deltaX > 0) {
          btnPrev.click();
        } else {
          btnNext.click();
        }
      }
    }

    tableauImage.addEventListener(
      "touchmove",
      function (e) {
        if (Math.abs(e.touches[0].clientX - touchStartX) > 10) {
          e.preventDefault();
        }
      },
      { passive: false }
    );
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const isMobile = window.matchMedia("(max-width: 767px)").matches;
  const tableauImage = document.querySelector(".masque-image");
  const btnPrev = document.getElementById("btn-prev");
  const btnNext = document.getElementById("btn-next");

  if (isMobile && tableauImage && btnPrev && btnNext) {
    let touchStartX = 0;
    let touchEndX = 0;
    const swipeThreshold = 50;

    tableauImage.addEventListener(
      "touchstart",
      function (e) {
        touchStartX = e.touches[0].clientX;
      },
      { passive: true }
    );

    tableauImage.addEventListener(
      "touchend",
      function (e) {
        touchEndX = e.changedTouches[0].clientX;
        handleSwipeGesture();
      },
      { passive: true }
    );

    function handleSwipeGesture() {
      const deltaX = touchEndX - touchStartX;

      if (Math.abs(deltaX) > swipeThreshold) {
        if (deltaX > 0) {
          btnPrev.click();
        } else {
          btnNext.click();
        }
      }
    }

    tableauImage.addEventListener(
      "touchmove",
      function (e) {
        if (Math.abs(e.touches[0].clientX - touchStartX) > 10) {
          e.preventDefault();
        }
      },
      { passive: false }
    );
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const isMobile = window.matchMedia("(max-width: 767px)").matches;
  const galleryCon = document.querySelector(".gallery-con");
  const btnPrev = document.getElementById("btn-prev");
  const btnNext = document.getElementById("btn-next");

  if (isMobile && galleryCon && btnPrev && btnNext) {
    let touchStartX = 0;
    let touchEndX = 0;
    const swipeThreshold = 50;

    galleryCon.addEventListener(
      "touchstart",
      function (e) {
        touchStartX = e.touches[0].clientX;
      },
      { passive: true }
    );

    galleryCon.addEventListener(
      "touchend",
      function (e) {
        touchEndX = e.changedTouches[0].clientX;
        handleSwipeGesture();
      },
      { passive: true }
    );

    function handleSwipeGesture() {
      const deltaX = touchEndX - touchStartX;

      if (Math.abs(deltaX) > swipeThreshold) {
        deltaX > 0 ? btnPrev.click() : btnNext.click();
      }
    }

    galleryCon.addEventListener(
      "touchmove",
      function (e) {
        if (Math.abs(e.touches[0].clientX - touchStartX) > 10) {
          e.preventDefault();
        }
      },
      { passive: false }
    );
  }
});
