$(document).ready(function() { /* Esperamos a que el DOM se cargue por completo */
    $('#modalHVM').on('submit', function(event) { /* Recibimos el evento */
        event.preventDefault(); /* Evitamos que la pagina se actualice */

        $.ajax({ /* Realizamos la solicitud ajax para los mensajitos */
            type: 'POST',         
            url: $(this).attr('action'), /* Obtenemos la url del metodo action en el formulario de html */
            data: $(this).serialize(), /* Serializamos los datos, osea, los volvemos simples para que se envien con facilidad */
            success: function(response) {
                /* Mostramos los mensajitos */
                if (response.status === 'success') {
                    alert(response.message); /* Mensaje de exito */
                    location.reload(); /* Recargamos la pagina */
                } else {
                    alert(response.message); /* Mensaje de error */
                }
            },
            error: function(xhr, status, error) {
                alert('Ha ocurrido un error: ' + error); /* Mensaje de exito si el post falla */
            }
        });
    });
    
    $('.FormAjax').on('submit', function(event) { /* Recibimos el evento */
        event.preventDefault(); /* Evitamos que la pagina se actualice */

        $.ajax({ /* Realizamos la solicitud ajax para los mensajitos */
            type: 'POST',         
            url: $(this).attr('action'), /* Obtenemos la url del metodo action en el formulario de html */
            data: $(this).serialize(), /* Serializamos los datos, osea, los volvemos simples para que se envien con facilidad */
            success: function(response) {
                /* Mostramos los mensajitos */
                if (response.status === 'success') {
                    alert(response.message); /* Mensaje de exito */
                    location.reload(); /* Recargamos la pagina */
                } else if (response.status === 'redirect') { /* En caso de redireccionar */
                    window.location.href = response.url;
                }else {
                    alert(response.message); /* Mensaje de error */
                }
            },
            error: function(xhr, status, error) {
                alert('Ha ocurrido un error: ' + error); /* Mensaje de exito si el post falla */
            }
        });
    });
});