$(function () {
    $('.btnLimp').click(function (event) {
        event.preventDefault(); // Evitar el envío del formulario
        $('.txtEma, .txtCla, .txtRun, .txtNom, .txtApe, .txtFon, .region').val('');
        $('.txtFec').val('dd-mm-aaaa');
    });
    $('.btnGuar').click(function (event) {
        event.preventDefault(); // Evitar el envío del formulario

        // Comprobar correo
        if ($('.txtEma').val() == '') {
            alert('No especificó el correo');
        } else if (!/^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/.test($('.txtEma').val())) {
            alert('El formato del correo no es válido');
            // Comprobar contrasena
        } else if ($('.txtCla').val() == "") {
            alert('No especificó la clave');
        } else if (!/^[a-zA-Z0-9]+$/.test($('.txtCla').val())) {
            alert('La clave solo puede contener letras y números');
            // Comprobar Rut
        } else if ($('.txtRun').val() == '') {
            alert('No especificó el Run');
        } else if (!/^[0-9.]+[0-9kK-]{2}$/.test($('.txtRun').val())) {
            alert('El formato del Run no es válido');
            // Comprobar Nombre, Apellido, Fecha de nacimiento, Teléfono
        } else if ($('.txtNom').val() == '') {
            alert('No especificó el nombre');
        } else if ($('.txtApe').val() == '') {
            alert('No especificó el apellido');
        } else if ($('.txtFec').val() == '') {
            alert('No especificó la fecha de nacimiento');
        } else if ($('.txtFon').val() == '') {
            alert('No especificó el teléfono');
        } else if (!/^[0-9]+$/.test($('.txtFon').val())) {
            alert('El teléfono solo puede contener números');
        } else {
            // Enviar datos
            alert('Los datos se enviaron correctamente');
        }
    });
});