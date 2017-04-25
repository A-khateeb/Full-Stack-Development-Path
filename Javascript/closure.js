function wrapFun(n){
var localvariable = n;
return function()
{
	return localvariable;
};
	}
	var wrap1= wrapFun(1);
	var wrap2= wrapFun(2);
	document.write(wrap1());
	document.write('\n');
	document.write(wrap2());
