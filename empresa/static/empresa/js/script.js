let swiper;

function initializeSwiper() {
    const screenWidth = window.innerWidth;
  
    if (screenWidth > 800) {
        swiper = new Swiper(".mySwiper", {
            slidesPerView: 3,
            spaceBetween: 30,
            slidesPerGroup: 3,
            loop: true,
            loopFillGroupWithBlank: true,
            pagination: {
                el: ".swiper-pagination",
                clickable: true,
            },
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
        });
    } else {
        swiper = new Swiper('.mySwiper', {
            slidesPerView: 1,
            spaceBetween: 10, 
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
        });
    }
}

// Inicializa el Swiper al cargar la página
initializeSwiper();

// Actualiza el Swiper al cambiar el tamaño de la ventana
window.addEventListener('resize', function () {
    if (swiper) {
        swiper.destroy(); 
    }
    initializeSwiper(); 
});
