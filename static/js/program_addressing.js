function loadAddressings(id) {
    if (id) {
        var ID = document.getElementById("ID_" + id);
        var NoPrescripcion = document.getElementById("NoPrescripcion_" + id);
        var TipoTec = document.getElementById("TipoTec_" + id);
        var ConTec = document.getElementById("ConTec_" + id);
        var NoIdPaciente = document.getElementById("NoIdPaciente_" + id);
        var NoEntrega = document.getElementById("NoEntrega_" + id);
        var NoSubEntrega = document.getElementById("NoSubEntrega_" + id);
        var TipoIDProv = document.getElementById("TipoIDProv_" + id);
        var NoIDProv = document.getElementById("NoIDProv_" + id);
        var CodMunEnt = document.getElementById("CodMunEnt_" + id);
        var FecMaxEnt = document.getElementById("FecMaxEnt_" + id);
        var CantTotAEntregar = document.getElementById("CantTotAEntregar_" + id);
        var DirPaciente = document.getElementById("DirPaciente_" + id);
        var CodTecAEntregar = document.getElementById("CodTecAEntregar_" + id);

        document.getElementById("numAddressing2").innerHTML = "Direccionamiento: " + NoPrescripcion.firstChild.data;
        document.getElementById("ID").value = ID.firstChild.data;
        document.getElementById("numAddressing").value = NoPrescripcion.firstChild.data;
        document.getElementById("TipoTec").value = TipoTec.firstChild.data;
        document.getElementById("ConTec").value = ConTec.firstChild.data;
        document.getElementById("NoIdPaciente").value = NoIdPaciente.firstChild.data;
        document.getElementById("NoEntrega").value = NoEntrega.firstChild.data;
        document.getElementById("NoSubEntrega").value = NoSubEntrega.firstChild.data;
        document.getElementById("TipoIDProv").value = TipoIDProv.firstChild.data;
        document.getElementById("NoIDProv").value = NoIDProv.firstChild.data;
        document.getElementById("CodMunEnt").value = CodMunEnt.firstChild.data;
        document.getElementById("FecMaxEnt").value = FecMaxEnt.firstChild.data;
        document.getElementById("CantTotAEntregar").value = CantTotAEntregar.firstChild.data;
        document.getElementById("DirPaciente").value = DirPaciente.firstChild.data;
        document.getElementById("CodTecAEntregar").value = CodTecAEntregar.firstChild.data;
    }
}