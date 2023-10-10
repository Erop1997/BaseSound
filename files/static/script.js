
setTimeout(()=>{
const some_note = document.getElementById('note');
// some_note.style.display='none';
some_note.style.opacity -= '0.5';
}, 1600);

function toogleMenu(){
    let modal = document.querySelector('.dropdown')
    modal.classList.toggle('is-active')
}

function showSongs(){
    let list = document.querySelector('.songs')
    let chevron = document.querySelector('#chevron')
    list.style.display = list.style.display === 'none' ? '' : 'none'
    chevron.name = chevron.name === 'chevron-down' ? 'chevron-up' : 'chevron-down'
}