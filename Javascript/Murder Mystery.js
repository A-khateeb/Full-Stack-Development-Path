var room = "dining room";
var suspect = "Mr. Parkes";
var weapon = "";
var solved = false;

if (room == "ballroom") {
    weapon = "poison";
    suspect = "Mrs. Sparr";
    solved = true;

} else if (room == "gallery" ) {
    weapon = "trophy";
    suspect = "Ms. Van Cleve";
    solved = true;
} else if (room == "billiards") {
    weapon = "pool stick";
    suspect = "Mrs. Sparr";
    solved = true;
} else {
    room = "dining"
    weapon = "knife"
    suspect = "Mr. Parkes"
    solved = true;
}
if (solved) {
    console.log(suspect+ " did it in the "+ room + " room with the "+ weapon);
}