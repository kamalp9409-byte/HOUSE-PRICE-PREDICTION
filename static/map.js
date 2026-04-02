var map = L.map('map').setView([28.6139, 77.2090], 12); // Delhi default

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19
}).addTo(map);

let marker;

map.on("click", function (event) {
    let lat = event.latlng.lat;
    let lon = event.latlng.lng;

    document.getElementById("lat").value = lat;
    document.getElementById("lon").value = lon;

    if (marker) {
        map.removeLayer(marker);
    }

    marker = L.marker([lat, lon]).addTo(map);
});
