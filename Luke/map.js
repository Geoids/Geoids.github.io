<meta charset="utf-8">
<meta name="viewport" content="initial-scale=1, maximum-scale=1, user-scalable=no">
<style>
  html, body, #viewDiv {
    padding: 0;
    margin: 0;
    height: 85%;
    width: 100%;
  }
</style>
<link rel="stylesheet" href="https://js.arcgis.com/4.6/esri/css/main.css">
<script src="https://js.arcgis.com/4.6/"></script>
<script>
require([
  "esri/Map",
  "esri/views/MapView",
  "dojo/domReady!"
], function(Map, MapView){
  var map = new Map({
    basemap: "streets"
  });
  var view = new MapView({
    container: "viewDiv",  // Reference to the scene div created in step 5
    map: map,  // Reference to the map object created before the scene
    zoom: 4,  // Sets zoom level based on level of detail (LOD)
    center: [15, 65]  // Sets center point of view using longitude,latitude
  });
});
</script>