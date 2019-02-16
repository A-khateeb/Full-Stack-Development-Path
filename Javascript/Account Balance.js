var balance = 325.00;
var checkBalance = false;
var isActive = true;

if (checkBalance == true){
    if (isActive && balance >0){
        console.log("Your balance is "+ balance.toFixed(2));
    }
    else if (isActive == false){
        console.log("Your account is no longer active")
    }
    else if (balance==0){
        console.log("Your account is empty")
    }
    else if (balance < 0)
        console.log("Your account is has negative balance, please contact the bank")
}
else{
    console.log("Have a nice day!")
}

