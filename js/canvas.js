/**
 * Usage: python3 -m http.server
 * Then navigate to localhost:8000/test.html
 */

window.onload=function() {
    var map = document.getElementById('map');
    var svgDoc = map.contentDocument;

    var elem = svgDoc.getElementById('TZ.MW');
    elem.setAttribute('fill', '#2BB8DC');
    var elem = svgDoc.getElementById('TZ.MT');
    elem.setAttribute('fill', '#2BB8DC');
    var elem = svgDoc.getElementById('TZ.DS');
    elem.setAttribute('fill', '#2BB8DC');
    var elem = svgDoc.getElementById('TZ.KA');
    elem.setAttribute('fill', '#2BB8DC');

    svgDoc.addEventListener('click', function(e) {
        var clickedItem = e.target;
        var color = e.target.getAttribute('fill') == '#CEE3F5' ? '#2BB8DC' : '#CEE3F5';
        e.target.setAttribute('fill', color); 
    });
}