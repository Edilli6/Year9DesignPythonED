document.getElementById("Inputcountries").onclick = clicked;


var countries = ["Austria","Botswana","Brazil","Estonia","Fiji","finland","Germany","Hungary","Ireland","Japan","Latvia","Lithuania","Montenegro","Morocco","Netherlands","Nigeria","Poland","Romania","Rwanda","Slovenia","South-Africa","Sudan","Sweedan","North Macedonia","United Republic",

percentBelowPovertyLine = [91.94,94.44,74.63,100,100,80.82,72.41,41.77,75.0,52.9,74.69,94.59,100,85.94,53.22,41,100,38.51,62.61,0,9.09,62.5,70.0,48.85,0,0

function clicked() {
	var value = document.getElementById("Inputcountries").value.toLowerCase()
	console.log(value);

	for(i = 0; i < countries.length; i = i + 1) {
		if (value === countries[i]) {
			console.log("Yes")
		}
	}
}

document.getElementById("countryInputButton").onclick = clicked;

function clicked() {

var value = document.getElementById("Inputcountries").value

for (i = 0; i < countries.length; i = i + 1) {
	if (value === countries[i]) {
		console.log(proportionofopenwaterbodieswithcleanwater[i]+"% of "+value+"'s population is below Average");
		document.getElementById("results").innerHTML = (proportionofopenwaterbodieswithcleanwater[i]+"% of "+value+"'s population is below Average");
		}
	}
}

