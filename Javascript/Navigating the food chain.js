var eatsPlants = false;
var eatsAnimals = true;

var category = ((eatsPlants && !eatsAnimals) ? "herbivore" : (!eatsPlants && eatsAnimals) ? "carnivore" : (eatsAnimals && eatsPlants) ? "omnivore" : "");
console.log(category);