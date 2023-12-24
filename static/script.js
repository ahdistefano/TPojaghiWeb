document.addEventListener('DOMContentLoaded', () => {
    const submenuParents = document.querySelectorAll('.submenu-parent');

    submenuParents.forEach(parent => {
        const submenu = parent.querySelector('.submenu');
        let timeoutId = null;

        parent.addEventListener('mouseenter', () => {
            clearTimeout(timeoutId);
            submenu.style.display = 'block';
            submenu.classList.remove('fade-out');
            submenu.classList.add('fade-in');
        });

        parent.addEventListener('mouseleave', () => {
            submenu.classList.remove('fade-in');
            submenu.classList.add('fade-out');            
            timeoutId = setTimeout(() => {
                if (!submenu.matches(':hover')) {
                    submenu.style.display = 'none';
                }
            }, 490);    // 10ms shorter than the CSS animation duration to avoid display glitch
        });
    });
});


// Swiper.js integration
document.addEventListener('DOMContentLoaded', () => {
    var swiper;
    var currentPage = document.querySelector('section').id;
    if (currentPage === 'home') {
        swiper = new Swiper('.swiper', {
            effect: 'fade',
            loop: true,
            fadeEffect: {
                crossFade: false
            },
            autoplay: {
                delay: 4000,
                disableOnInteraction: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
        });
    } else if (currentPage === 'projects') {
        var swiper2 = new Swiper(".mySwiperBottom", {
            loop: true,
            spaceBetween: 0,
            slidesPerView: 3,
            breakpoints: {
                // when window width is >= 767px
                767: {
                    slidesPerView: 6,
                },
            },
            mousewheel: true,
            autoHeight: false,
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
            scrollbar: {
                el: '.swiper-scrollbar',
                draggable: true,
            },
        });
        var swiper = new Swiper(".mySwiperTop", {
            loop: true,
            slidesPerView: 1,
            freeMode: false,
            autoHeight: false,
            allowTouchMove: false,
            thumbs: {
                swiper: swiper2,
            },
        });
    };
});

// Footer copyright year
document.addEventListener('DOMContentLoaded', function () {
    var currentYear = new Date().getFullYear();
    document.getElementById('current-year').textContent = currentYear;
});

function showAlbumInfo(albumIndex) {
    var album = albumsData[albumIndex];
    var roles = "";
    for (let i = 0; i < album.roles.length; i++) {
        roles += '<li>'+album.roles[i]+'</li>';
    }
    document.getElementById('album-info').innerHTML =
        '<img src="/static/projects/' + album.cover + '">' +
        '<h1>' + album.artist + '</h1>' +
        '<h2>' + album.title + '</h2>' +
        '<h3>' + album.year + '</h3>' +
        '<p>Roles:</p>' + roles;
}

// Prevent img right-click
//document.addEventListener('DOMContentLoaded', (event) => {
//    document.querySelectorAll('img').forEach(img => {
//        img.addEventListener('contextmenu', e => e.preventDefault());
//    });
//});