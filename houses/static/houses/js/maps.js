var encodedAddress = encodeURIComponent(address);
var uri = `https://maps.googleapis.com/maps/api/geocode/json?address=${encodedAddress}&key=AIzaSyC1_2LQmZ65yW8ttfBbHMgsJFqmc4UlCdY`;

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        let res = JSON.parse(xhttp.responseText);
        let lat = res.results[0].geometry.location.lat;
        let lng = res.results[0].geometry.location.lng;
        initMap(lat, lng);
    }
};
xhttp.open("GET", uri, true);
xhttp.send();

function initMap(lat, lng) {
  const house = { lat, lng };
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 16,
    center: house,
  });
  const marker = new google.maps.Marker({
    position: house,
    map: map,
  });
}