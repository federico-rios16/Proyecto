document.addEventListener('DOMContentLoaded', function() {
    var map = L.map('map').setView([-26.1830, -58.1750], 14);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    var alquileres = [
        {
            lat: -26.1822,
            lng: -58.1745,
            nombre: "Departamento en el Centro",
            precio: "$120.000/mes",
            tipo: "departamento",
            imagen: "https://images.pexels.com/photos/164558/pexels-photo-164558.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            habitaciones: 4,
            banos: 2,
            metrosCuadrados: 400
        },
        {
            lat: -26.1850,
            lng: -58.1700,
            nombre: "Casa en el Barrio San Miguel",
            precio: "$180.000/mes",
            tipo: "casa",
            imagen: "https://images.pexels.com/photos/1396122/pexels-photo-1396122.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            habitaciones: 4,
            banos: 2,
            metrosCuadrados: 400
        },
        {
            lat: -26.1780,
            lng: -58.1800,
            nombre: "Local Comercial en Avenida",
            precio: "$250.000/mes",
            tipo: "local",
            imagen: "https://images.pexels.com/photos/5998048/pexels-photo-5998048.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            habitaciones: 4,
            banos: 2,
            metrosCuadrados: 400
        },
        {
            lat: -26.1880,
            lng: -58.1780,
            nombre: "Departamento con Vista al Río",
            precio: "$150.000/mes",
            tipo: "departamento",
            imagen: "https://images.pexels.com/photos/1115804/pexels-photo-1115804.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            habitaciones: 4,
            banos: 2,
            metrosCuadrados: 400
        },
        {
            lat: -26.1800,
            lng: -58.1720,
            nombre: "Casa Quinta en las Afueras",
            precio: "$220.000/mes",
            tipo: "casa",
            imagen: "https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            habitaciones: 4,
            banos: 2,
            metrosCuadrados: 400
        },
        {
            lat: -26.1830,
            lng: -58.1760,
            nombre: "Oficina en Edificio Moderno",
            precio: "$200.000/mes",
            tipo: "oficina",
            imagen: "https://images.pexels.com/photos/3182823/pexels-photo-3182823.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            habitaciones: 4,
            banos: 2,
            metrosCuadrados: 400
        },
        {
            lat: -26.1860,
            lng: -58.1730,
            nombre: "Departamento Amoblado",
            precio: "$130.000/mes",
            tipo: "departamento",
            imagen: "https://images.pexels.com/photos/1743231/pexels-photo-1743231.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            habitaciones: 4,
            banos: 2,
            metrosCuadrados: 400
        },
        {
            lat: -26.1810,
            lng: -58.1790,
            nombre: "Casa con Pileta",
            precio: "$280.000/mes",
            tipo: "casa",
            imagen: "https://images.pexels.com/photos/186077/pexels-photo-186077.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            habitaciones: 4,
            banos: 2,
            metrosCuadrados: 400
        },
        {
            lat: -26.1840,
            lng: -58.1710,
            nombre: "Local en Galería",
            precio: "$180.000/mes",
            tipo: "local",
            imagen: "https://images.pexels.com/photos/2215088/pexels-photo-2215088.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            habitaciones: 4,
            banos: 2,
            metrosCuadrados: 400
        },
        {
            lat: -26.1870,
            lng: -58.1750,
            nombre: "Departamento en Alquiler Temporal",
            precio: "$160.000/mes",
            tipo: "departamento",
            imagen: "https://images.pexels.com/photos/1129447/pexels-photo-1129447.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            habitaciones: 4,
            banos: 2,
            metrosCuadrados: 400
        }
    ];

    function updateMapAndResults(alquileresFiltrados) {
        map.eachLayer(layer => {
            if (layer instanceof L.Marker) {
                map.removeLayer(layer);
            }
        });

        let resultsDiv = document.querySelector('.results');
        resultsDiv.innerHTML = '';

        alquileresFiltrados.forEach(function(alquiler) {
            L.marker([alquiler.lat, alquiler.lng])
                .addTo(map)
                .bindPopup(`<b>${alquiler.nombre}</b><br>${alquiler.precio}`);

                if (typeof alquiler.precio === 'string' && alquiler.precio.trim() !== '') {
                    let precioNumerico = parseInt(alquiler.precio.replace(/\D/g, ''));
                    if (!isNaN(precioNumerico)) {
                        // El precio tiene un formato válido, podemos usar precioNumerico
                        let resultItem = document.createElement('div');
                        // ... (Tu código existente) ...
                    } else {
                        console.error(`Precio inválido para ${alquiler.nombre}: ${alquiler.precio}`);
                        // Manejar el error o asignar un valor predeterminado
                    }
                } else {
                    console.error(`Precio inválido para ${alquiler.nombre}: ${alquiler.precio}`);
                    // Manejar el error o asignar un valor predeterminado
                }


            let resultItem = document.createElement('div');
            resultItem.classList.add('result-item');
            resultItem.innerHTML = `
                <img src="${alquiler.imagen}" alt="${alquiler.nombre}">
                <h3>${alquiler.nombre}</h3>
                <p>Precio: ${alquiler.precio}</p>
                <p>Habitaciones: ${alquiler.habitaciones}</p>
                <p>Baños: ${alquiler.banos}</p>
                <p>Metros Cuadrados: ${alquiler.metrosCuadrados} m²</p>
            `;
            resultsDiv.appendChild(resultItem);

            // Evento click para mostrar detalles de la propiedad
            resultItem.addEventListener('click', function() {
            showPropertyDetails(alquiler);
            });
        });
    }

    function showPropertyDetails(alquiler) {
        let propertyDetailsDiv = document.getElementById('propertyDetails');
        propertyDetailsDiv.innerHTML = `
            <h3>${alquiler.nombre}</h3>
            <img src="${alquiler.imagen}" alt="${alquiler.nombre}">
            <p>Precio: ${alquiler.precio}</p>
            <p>Habitaciones: ${alquiler.habitaciones}</p>
            <p>Baños: ${alquiler.banos}</p>
            <p>Metros Cuadrados: ${alquiler.metrosCuadrados} m²</p>
            <p>Descripción: ${alquiler.descripcion || 'Sin descripción disponible'}</p>
            <button onclick="hidePropertyDetails()">Cerrar</button>
        `;
        propertyDetailsDiv.style.display = 'block';
    }

    function hidePropertyDetails() {
    document.getElementById('propertyDetails').style.display = 'none';
    }

    document.getElementById('searchButton').addEventListener('click', function() {
        let location = document.getElementById('locationSearch').value.toLowerCase();
        let propertyType = document.getElementById('propertyTypeFilter').value.toLowerCase();
        let maxPrice = parseInt(document.getElementById('maxPriceFilter').value);

        let alquileresFiltrados = alquileres.filter(function(alquiler) {
            let matchesLocation = alquiler.nombre.toLowerCase().includes(location);
            let matchesType = !propertyType || alquiler.tipo === propertyType;
            let matchesPrice = isNaN(maxPrice) || parseInt(alquiler.precio.replace(/\D/g, '')) <= maxPrice;

            return matchesLocation && matchesType && matchesPrice;
        });

        updateMapAndResults(alquileresFiltrados);
    });

    document.getElementById('resetButton').addEventListener('click', function() {
        document.getElementById('locationSearch').value = '';
        document.getElementById('propertyTypeFilter').value = '';
        document.getElementById('maxPriceFilter').value = '';
        updateMapAndResults(alquileres);
    });

    let isGridView = true; // Variable para rastrear la vista actual

    document.getElementById('viewToggleButton').addEventListener('click', function() {
        let resultsDiv = document.querySelector('.results');
        resultsDiv.classList.toggle('list-view'); // Alternar la clase list-view
        isGridView = !isGridView; // Cambiar el estado de la vista

        // Actualizar el texto del botón
        this.textContent = isGridView ? 'Cambiar Vista' : 'Cambiar Cuadrícula';
    });

    document.querySelectorAll('.dropdown-content a').forEach(item => {
        item.addEventListener('click', function(event) {
            event.preventDefault(); // Evitar la recarga de la página
            let sortType = this.dataset.sort;
            let alquileresOrdenados = [...alquileres]; // Crear una copia del array

            switch (sortType) {
                case 'precio-asc':
                    alquileresOrdenados.sort((a, b) => parseInt(a.precio.replace(/\D/g, '')) - parseInt(b.precio.replace(/\D/g, '')));
                    break;
                case 'precio-desc':
                    alquileresOrdenados.sort((a, b) => parseInt(b.precio.replace(/\D/g, '')) - parseInt(a.precio.replace(/\D/g, '')));
                    break;
                case 'metros-asc':
                    alquileresOrdenados.sort((a, b) => a.metrosCuadrados - b.metrosCuadrados);
                    break;
                case 'metros-desc':
                    alquileresOrdenados.sort((a, b) => b.metrosCuadrados - a.metrosCuadrados);
                    break;
            }

        updateMapAndResults(alquileresOrdenados);
    });
    });

    updateMapAndResults(alquileres);
});
