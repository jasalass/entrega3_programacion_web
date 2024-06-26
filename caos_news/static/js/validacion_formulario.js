function validarRut(rut, dv) {
    // Convertir el RUT a mayúsculas
    rut = rut.toUpperCase();

    // Validar que el RUT y el dígito verificador sean numéricos
    if (!/^\d+$/.test(rut) || (dv !== 'K' && !/^\d$/.test(dv))) {
        return false;
    }

    // Calcular el dígito verificador esperado
    var suma = 0;
    var multiplo = 2;
    for (var i = rut.length - 1; i >= 0; i--) {
        suma += parseInt(rut.charAt(i)) * multiplo;
        if (multiplo === 7) {
            multiplo = 2;
        } else {
            multiplo++;
        }
    }
    var resto = suma % 11;
    var dvEsperado = 11 - resto === 11 ? 0 : (11 - resto === 10 ? 'K' : 11 - resto);

    // Comparar el dígito verificador calculado con el proporcionado
    return dvEsperado.toString() === dv.toString();
}





//Comprobar el ingreso en el textarea y mostrar caracteres restantes
$("#resena").on("input", () => {
    let texto = $("#resena").val(); // Captura el texto ingresado al textarea

    let restante = 1000 - texto.length; // Calcula los caracteres restantes

    $("#restante").text(`Caracteres restantes: ${restante}`); //Muestra los caracteres restantes en la etiqueta <p>
});


//Comprobar longitud de rut
$("#rut").on("input", function() {
    // Obtener el valor del campo de entrada del RUT
    var rut = $(this).val();
    // Limitar la longitud del RUT a 8 caracteres
    if (rut.length > 8) {
        $(this).val(rut.slice(0, 8));
    }
});

//Validación de campos en formulario
$("#boton-enviar").click((event) =>{
    event.preventDefault() //Previene el envío del formulario al hacer click en el botón de submit

    //Asignar variables 
    let rut = $("#rut")
    let dv = $("#dv")
    let nombre = $("#nombre")
    let email = $("#email")
    
    //Validar rut
    let validacion_rut = validarRut(rut.val(), dv.val()) //Enviar rut y dv como parámetros a la función


    if (!validacion_rut || !nombre.val() || !email.val()){
        if(!validacion_rut){
            rut.addClass("is-invalid ") //Agregar clases a las etiquetas para mostrar los campos inválidos
            dv.addClass("is-invalid ")
        }else{
            rut.removeClass("is-invalid")
            VarDate.removeClass("is-invalid")
        }

        if(!nombre.val()){
            nombre.addClass("is-invalid")
        }else{
            nombre.removeClass("is-invalid")
        }

        if(!email.val()){
            email.addClass("is-invalid")
        }else{
            email.removeClass("is-invalid")
        }

        alert("Revise la información ingresada")
        
    } else {
        $("#form-laboral").submit()
    }
})