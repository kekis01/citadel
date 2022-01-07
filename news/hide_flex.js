function hiddenClick(element_id) {
    let csgo = document.querySelectorAll('.cs-go');
    let dota2 = document.querySelectorAll('.dota-2');
    let fifa = document.querySelectorAll('.fifa');
    let lol = document.querySelectorAll('.lol');
    let event = document.querySelectorAll('.event');
    let all = document.querySelectorAll('.all');
    if (element_id == 'cs-go') {
        clearClick();
        for(let i = 0; i < all.length; i++) {
            if (i < event.length) {
                event[i].style.display = "none";
            }
            if (!csgo[i].classList.contains('dota-2')) {
                dota2[i].style.display = "none";
            }
            if (i < lol.length) {
                lol[i].style.display = "none";
            }
            if (i < fifa.length) {
                fifa[i].style.display = "none";
            }
        }
    } else if(element_id == 'dota-2') {
        clearClick();
        for(let i = 0; i < all.length; i++) {
            if (i < event.length) {
                event[i].style.display = "none";
            }
            if (!dota2[i].classList.contains('cs-go')) {
                csgo[i].style.display = "none";
            }
            if (i < lol.length) {
                lol[i].style.display = "none";
            }
            if (i < fifa.length) {
                fifa[i].style.display = "none";
            }
        }
    } else if(element_id == 'fifa') {
        clearClick();
        for(let i = 0; i < all.length; i++) {
            if (i < event.length) {
                event[i].style.display = "none";
            }
            if (i < csgo.length) {
                csgo[i].style.display = "none";
            }
            if (i < lol.length) {
                lol[i].style.display = "none";
            }
            if (i < dota2.length) {
                dota2[i].style.display = "none";
            }
        }
    } else if(element_id == 'lol') {
        clearClick();
        for(let i = 0; i < all.length; i++) {
            if (i < event.length) {
                event[i].style.display = "none";
            }
            if (i < csgo.length) {
                csgo[i].style.display = "none";
            }
            if (i < dota2.length) {
                dota2[i].style.display = "none";
            }
            if (i < fifa.length) {
                fifa[i].style.display = "none";
            }
        }
    } else if(element_id == 'event') {
        clearClick();
        for(let i = 0; i < all.length; i++) {
            if (i < lol.length) {
                lol[i].style.display = "none";
            }
            if (i < csgo.length) {
                csgo[i].style.display = "none";
            }
            if (i < dota2.length) {
                dota2[i].style.display = "none";
            }
            if (i < fifa.length) {
                fifa[i].style.display = "none";
            }
        }
    } else {
        clearClick();
    }
    function clearClick() {
        for(let i = 0; i < all.length; i++) {
            if (i < lol.length) {
                lol[i].style.display = "flex";
            }
            if (i < csgo.length) {
                csgo[i].style.display = "flex";
            }
            if (i < dota2.length) {
                dota2[i].style.display = "flex";
            }
            if (i < fifa.length) {
                fifa[i].style.display = "flex";
            }
            if (i < event.length) {
                event[i].style.display = "flex";
            }
        }
    }
};