/*
function power(base, exponent) {
    if (exponent == undefined)
        exponent = 2;
    var result = 1;
    for (count = 0; count < exponent; count++)
        result *= base;
    return result;
}
*/
function power(base,exponent){
	if(exponent == 0)
		return 1;
	else
		return base  * power(base , exponent-1);

}
document.write(power(4,4));
