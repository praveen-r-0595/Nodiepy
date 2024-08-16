function changeName(){
    document.getElementById('n').innerHTML = "Player"
    pywebview.api.log("Hello")

}

function addDB(){
    props = {
        user : "CharField()",
        number : "IntegerField()",
        phone : "CharField()"
    }
    pywebview.api.StartAndAddData(props)
}

window.addEventListener('pywebviewready', function() {
    var container = document.getElementById('pywebview-status')
    container.innerHTML = '<i>pywebview</i> is ready'
})