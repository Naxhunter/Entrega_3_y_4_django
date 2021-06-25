function login(){
    var validar = email();
    if(validar==false){
        return false;
    }
    validar = contra();
    if(validar==false){
        return false;
    }
    return true;
}
function email(){
    var email = document.getElementById('txtEmail').value;
    /*alert("entre");*/
    var quitar = email.trim();
    var nvoemail = quitar.length;
    if(nvoemail<6){
        error = "Su email no puede tener menos de 6 caracteres.";
        document.getElementById('error_0').innerHTML = error;
        return false;
    }
    document.getElementById('error_0').innerHTML = "";
    return true;
}

function contra(){
    var pass_user = document.getElementById('txtPasslog').value;
    var quitar = pass_user.trim();
    var nvapass = quitar.length;
    if(nvapass < 8 || nvapass >30){
        error = "Mínimo 8 caracteres para la contraseña y máximo 30 caracteres."
        document.getElementById('error_1').innerHTML = error;
        return false;
    }
    document.getElementById('error_1').innerHTML = "";
    return true;
}