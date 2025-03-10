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
