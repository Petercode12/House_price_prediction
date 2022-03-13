function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var income = document.getElementById("income");
  var hs_age = document.getElementById("hs_age");
  var num_rooms = document.getElementById("num_rooms");
  var num_bedrooms = document.getElementById("num_bedrooms");
  var population = document.getElementById("population");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "/predict_home_price";
  $.post(
    url,
    {
      income: parseFloat(income.value),
      hs_age: parseFloat(hs_age.value),
      num_rooms: parseFloat(num_rooms.value),
      num_bedrooms: parseFloat(num_bedrooms.value),
      population: parseFloat(population.value),
    },
    function (data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML =
        "<h2>" + data.estimated_price.toString() + " USD</h2>";
      console.log(status);
    }
  );
}
