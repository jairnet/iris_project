document.getElementById("date-start").addEventListener("change", activateButton);
// document.getElementById("form-control").addEventListener("change", myFunction);
// document.getElementsByClassName("program-btn").addEventListener("click", myFunction);


function activateButton() {
    var x = document.getElementById("date-start");
    // document.getElementById("demo").innerHTML = "Fecha a Consultar: " + x.value;
    document.getElementById("button-consult").className = "btn btn-success btn-lg";
    // document.getElementById("button-consult").href = "{% url 'addressing-date' '" + x.value + "' %}"; 
}


