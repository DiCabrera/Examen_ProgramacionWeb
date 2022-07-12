//VALIDACIÓN
function validar() {
    var nom_consulturio = document.formulario_vac.txt_nom_consultorio.value
    var nom_enfermero = document.formulario_vac.txt_nom_enfermero.value
    var rut_enfermero = document.formulario_vac.txt_rut_enfermero.value
    var nro_dosis = document.formulario_vac.num_dosis.value
    var grupo_etario = document.formulario_vac.txt_grupo_etario.value
    //VALIDAR CONSULTORIO
    if (nom_consulturio.length < 3) {
        alert("El nombre del vacunatorio debe tener al menos 3 caracteres")
        document.formulario_vac.txt_nom_consultorio.focus()
        return false;
    }
    ///VALIDAR NOMBRE ENFERMERO
    if (nom_enfermero.length < 3) {
        alert("El nombre debe tener al menos 3 caracteres")
        document.formulario_vac.txt_nom_enfermero.focus()
        return false;
    }

    //VALIDAR RUT ENFERMERO
    if (rut_enfermero.length < 9 || rut_enfermero.length > 10 || rut_enfermero.indexOf('-') === -1) {
        alert("Rut invalido")
        document.formulario_vac.txt_rut_enfermero.focus()
        return false;
    }

    //VALIDAR DOSIS
    if (nro_dosis > 1) {
        alert("El número de la dosis debe ser mayor a 1")
        document.formulario_vac.num_dosis.focus()
        return false;
    }

    //VALIDAR GRUPO ETARIO
    if (grupo_etario.length > 3) {
        alert("El dato ingresado es invalido")
        document.formulario_vac.txt_grupo_etario.focus()
        return false
    }
    
    document.formulario_vac.action = "/ingreso_vacunatorio/"
    document.formulario_vac.submit() = true
    alert("La información ha sido ingresada con exito")
}