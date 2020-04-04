document.getElementById("Inputcountries").onclick = clicked;

var countries = ["World","Albania","Algeria","American Samoa","Angola","Antigua and Barbuda","Azerbaijan","Argentina","Bahamas","Bahrain","Bangladesh","Barbados","Australia and New Zealand", "Belgium", "Bermuda", "Central and Southern Asia", "Brazil", "Belize", "British", "Indian Ocean Territory", "Solomon Islands", "British Virgin Islands" "Brunei" "Darussalam", "Bulgaria", "Myanmar", "Cambodia", "Cameroon", "Canada"

proportionofopenwaterbodieswithcleanwater = [22736729.92,24229501.23,304.39251,110.26722,35457.57734,24.34117,171.59498,345.44749,41249.95475,3014642.643,47355.48699,94.82012,4458.35259,10.32045,407321.5286,1264.415670,25482,12419.81381,13.87036,972394.6254,3644.37028,641262.5106,1900.40161,3.31433,51.64986,2856.24123,11964.44587,89.10704,501.38859,164271.8851]

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

