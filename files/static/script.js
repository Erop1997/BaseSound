
setTimeout(()=>{
const some_note = document.getElementById('note');
// some_note.style.display='none';
some_note.style.opacity -= '0.5';
}, 1600);


function showSongs(pk){
    console.log(pk);
    let list = document.querySelector('.album-' + pk)
    let chevron = document.querySelector('.chevron-' + pk)
    list.style.display = list.style.display === 'none' ? '' : 'none'
    chevron.name = chevron.name === 'chevron-down' ? 'chevron-up' : 'chevron-down'
}