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

  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";
  captionText.innerHTML = dots[slideIndex - 1].alt;
}

const carouselSlides = document.querySelector(".carousel-slides");

carouselSlides.addEventListener("mouseenter", () => {
  carouselSlides.style.animationPlayState = "paused";
});

carouselSlides.addEventListener("mouseleave", () => {
  carouselSlides.style.animationPlayState = "running";
});
