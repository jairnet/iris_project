function myFunction(id) {
    console.log('ID ' + id)
    var NoPrescripcion = document.getElementById("NoPrescripcion_" + id)
    var TipoTec = document.getElementById("TipoTec_" + id)
    console.log(':::::DATA:::::' + ' ' + NoPrescripcion.firstChild.data + ' ' + TipoTec.firstChild.data);
}