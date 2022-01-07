let li = document.querySelectorAll('.nav__item-news');

for(let i = 0; i < li.length; i++){
    li[i].addEventListener('click', function(){
        for(let j = 0; j < li.length; j++){
            li[j].classList.remove('active');
        }
        this.classList.add('active');
    });
}