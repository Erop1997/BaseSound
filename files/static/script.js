
setTimeout(()=>{
const some_note = document.getElementById('note');
// some_note.style.display='none';
some_note.style.opacity -= '0.5';
}, 1600);

function toogleMenu(){
    let modal = document.querySelector('.dropdown')
    modal.classList.toggle('is-active')
}