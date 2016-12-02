//init prototype string formating enabled
//myString.format(param);
if (!String.prototype.format) {
  String.prototype.format = function() {
    var args = arguments;
    return this.replace(/{(\d+)}/g, function(match, number) { 
      return typeof args[number] != 'undefined'
        ? args[number]
        : match
      ;
    });
  };
}
//String.format(myString, param);
if (!String.format) {
  String.format = function(format) {
    var args = Array.prototype.slice.call(arguments, 1);
    return format.replace(/{(\d+)}/g, function(match, number) { 
      return typeof args[number] != 'undefined'
        ? args[number] 
        : match
      ;
    });
  };
}

function italic_beautifier(val) {
	val = String(val);
	ret = "<i>";

	//replace with regex ?? yes ! :D
	is_char = true;

	for (var i = 0; i < val.length; i++) {
		if (((65 <= val.charCodeAt(i)) && (val.charCodeAt(i) < 91))
				||(97 <= val.charCodeAt(i)) && (val.charCodeAt(i) < 123)) {
			if (!is_char) {
				ret += "<i>";
				is_char = true;
			}
			ret += val.charAt(i);
		} else {
			if (is_char) {
				ret += "</i>";
				is_char = false;
			}
			ret += val.charAt(i)==" " ? "&nbsp;" : val.charAt(i);
		}

	}

	ret += "</i>";

	//non italics functions replacement
	fcts = ret.match(/\<[i]\>[a-zA-Z]+\<\/[i]\>\(/g);
	if (fcts != null)
		for (var i = 0; i < fcts.length; i++) {
			fn = fcts[i].match(/[a-zA-Z]+/g)[1] + "(";
			ret = ret.replace(fcts[i], fn);
		}

	/*//remove italic from mathematics functions 
	//replace all this special cases by :  if next chars == "</i>(" -> it's a function to un-italic
	//trigo functions
	ret = ret.replace(/acos/g, "</i>acos<i>");
	ret = ret.replace(/asin/g, "</i>asin<i>");
	ret = ret.replace(/atan/g, "</i>atan<i>");
	ret = ret.replace(/cos/g, "</i>cos<i>");
	ret = ret.replace(/sin/g, "</i>sin<i>");
	ret = ret.replace(/tan/g, "</i>tan<i>");
	//absolute function
	ret = ret.replace(/abs/g, "</i>abs<i>");*/

	//making to exponent (a**b or a^b)
	//tpw = ret.match(/**);

	return ret;
}

function fraction(a, b) { // a over b
	return "<div class=\"fraction\">          	\
				<span class=\"fup\">{0}</span>	\
				<span class=\"bar\">/</span>  	\
				<span class=\"fdn\">{1}</span>	\
			</div>".format(
				italic_beautifier(a), 
				italic_beautifier(b));
}

function limes(a, b) { // a -> b
	return "<div class=\"limes\"> 				\
				<span class=\"overup\">lim</span>	\
				<span class=\"overdn\">				\
					{0}&rarr;{1}					\
				</span>								\
			</div>".format(
				italic_beautifier(a), 
				italic_beautifier(b));
}

function sy(a) { // add the supp arrow of vector
	return "<span class=\"sy\">							\
				<i>{0}</i>								\
				<span class=\"oncapital\">&rarr;</span>	\
			</span>".format(
				italic_beautifier(a));
}

function sum(a, b) { //a stopping limit, b begining
	return "<span class=\"intsuma\">					\
				<span class=\"lim\">{0}</span>			\
				<span class=\"sum-frac\">&sum;</span>	\
				<span class=\"lim\">{1}</span>			\
			</span>".format(
				italic_beautifier(a),
				italic_beautifier(b));
}

function integral(a, b) {
	return "<span class=\"intsuma\">					\
				<span class=\"lim\">{0}</span>			\
				<span class=\"sum-frac\">&int;</span>	\
				<span class=\"lim\">{1}</span>			\
			</span>".format(
				italic_beautifier(a),
				italic_beautifier(b));
}

function pow(a, b) { //a**b
	return "{0}<sup>{1}</sup>".format(
				italic_beautifier(a),
				italic_beautifier(b));
}


function interpreter(formula) {
	
}


