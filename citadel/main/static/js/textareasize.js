document.querySelector('.text_area').addEventListener('input', function (e) {
    e.target.style.height = 'auto'
    e.target.style.height = e.target.scrollHeight + "px"
})