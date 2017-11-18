function animalnumber(cows,chiken){
	var cowsString = String(cows);
	while (cowsString.lenght<3)
		cowsString='0'+cowsString;
		document.write(cowsString+"Cows");
		var chikenstring = String(chiken);
		while (chikenstring.lenght<3)
			chikenstring='0'+chikenstring;
			document.write(chikenstring+"Chikens");
}

animalnumber(3,10);
