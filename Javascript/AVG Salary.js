var education = 'high school diploma';
var salary = 0;
switch (education) {
    case "no high school diploma":
            salary = 25636;
            salary=salary.toLocaleString("en-US");
            console.log("In 2015, a person with " +education+" earned an average of $"+salary+"/year.");
            break;
    case "high school diploma":
            salary = 35256;
            salary=salary.toLocaleString("en-US");
            console.log("In 2015, a person with " +education+" earned an average of $"+salary+"/year.");
            break;
    case "an Associate's degree":
            salary = 41496;
            salary=salary.toLocaleString("en-US");
            console.log("In 2015, a person with " +education+" earned an average of $"+salary+"/year.");
            break;
    case "Bachelor's degree":
            salary = 59124;
            salary=salary.toLocaleString("en-US");
            console.log("In 2015, a person with " +education+" earned an average of $"+salary+"/year.");
            break;
    case  "Master's degree":
            salary = 69732;
            salary=salary.toLocaleString("en-US");
            console.log("In 2015, a person with " +education+" earned an average of $"+salary+"/year.");
            break;
    case  "Professional degree":
            salary = 89960;
            salary=salary.toLocaleString("en-US");
            console.log("In 2015, a person with " +education+" earned an average of $"+salary+"/year.");
            break;
    case "Doctoral degree":
            salary = 84396;
            salary=salary.toLocaleString("en-US");
            console.log("In 2015, a person with " +education+" earned an average of $"+salary+"/year.");
            break;
}


