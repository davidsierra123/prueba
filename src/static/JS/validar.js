function Login() {
    const correo = document.getElementById('documento');
    const pass = document.getElementById('Input');
    axios.post('login', {
        Ndocumento: correo.value,
        contraseña: pass.value
    })
        .then(function (response) {
            logueo();
            console.log(response);
            setTimeout(function() {
                window.location.href = '/fronted/menu';
            }, 2000); // Espera 2000 milisegundos (2 segundos) antes de redirigir
            document.getElementById('documento').value = "";
            document.getElementById('Input').value = "";
        })
        .catch(function (error) {
            console.log(error);
            Swal.fire({
                position: 'top-center',
                icon: 'error',
                title: '¡Datos invalidos!',
                showConfirmButton: false,
                timer: 2000,
            })
        });
}

// Este es el ojo que sirve para visualizar la contraseña
var input = document.getElementById('Input');
var img = document.getElementById('Clave');

img.addEventListener("click", function () {
    if (input.type == "password") {
        input.type = "text"
    } else {
        input.type = "password"
    }
})
function logueo() {
    axios.get('/fronted/obtener_datos_sesion')
        .then(function (response) {
            const datos = response.data;
            Swal.fire({
                position: 'top-center',
                icon: 'success',
                title: 'Bienvenido ' + datos.Nombre,
                showConfirmButton: false,
                timer: 2000,
            })
        })
        .catch(function (error) {
            console.log(error);
        });
}