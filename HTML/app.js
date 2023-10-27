// Función para mostrar la animación de carga
function showLoader() {
    const loaderContainer = document.getElementById("loader-container");
    loaderContainer.style.opacity = "1";
}

// Función para ocultar la animación de carga
function hideLoader() {
    const loaderContainer = document.getElementById("loader-container");
    loaderContainer.style.opacity = "0";
}

// Event listener para los enlaces del menú
const menuLinks = document.querySelectorAll("nav ul li a");
menuLinks.forEach(link => {
    link.addEventListener("click", event => {
        event.preventDefault();
        showLoader();
        
        // Simula una demora de 1 segundo antes de cargar la página
        setTimeout(() => {
            // Obtén la URL del enlace y redirige a esa página
            window.location.href = event.target.getAttribute("href");
        }, 1000); // 1000 milisegundos (1 segundo)
    });
});
