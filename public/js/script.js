function changeName(){
    document.getElementById('n').innerHTML = "Player"
    pywebview.api.log("Hello")

}



window.addEventListener('pywebviewready', function() {
    var container = document.getElementById('pywebview-status')
    container.innerHTML = '<i>pywebview</i> is ready'
})


data = {
    name : "text",
    number : "integer",
    desc : "largetext",
    canFly : "boolean"
}

function createDataTable(){
    myJSON = JSON.stringify(data)
    dbname = "dynamiccreated"
    pywebview.api.createTableData(dbname, myJSON)
}