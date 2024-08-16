function changeName(){
    document.getElementById('n').innerHTML = "Player"
    pywebview.api.log("Hello")

}



window.addEventListener('pywebviewready', function() {
    var container = document.getElementById('pywebview-status')
    container.innerHTML = '<i>pywebview</i> is ready'
})