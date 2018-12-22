var items = document.getElementById("thelist").childNodes;
for(var i = 0; i < items.length; i++){
  items[i].addEventListener("click", function(event){
    document.getElementById("thelist").removeChild(event.target);
  });

  items[i].addEventListener("mouseover", function(event){
    document.getElementById("h").innerHTML = (event.target.innerText || event.target.textContent);
  });

  items[i].addEventListener("mouseout", function(event){
    document.getElementById("h").innerHTML = "Hello World!";
  });
}

document.getElementById("fb").addEventListener("click", function(){fibonacci()});
document.getElementById("b").addEventListener("click", function(){ol()});

var fibonacci = () => {
  var n = document.getElementById("fiblist").childNodes.length;
  var window = [0, 1];

  var newentry = document.createElement("li");
  if(n < 2){
    var fibval = document.createTextNode(window[n].toString());
    newentry.appendChild(fibval);
    document.getElementById("fiblist").appendChild(newentry);
  }else{
    var inc = 2;
    while(inc <= n){
      window[inc % 2] = window[(inc + 1) % 2] + window[inc % 2];
      inc++;
    }
    var fibval = document.createTextNode(window[(inc - 1) % 2].toString());
    newentry.appendChild(fibval);
    document.getElementById("fiblist").appendChild(newentry);
  }
}

var ol = () => {
  var newitem = document.createElement("li");
  var itemtxt = document.createTextNode("item " + document.getElementById("thelist").childNodes.length);
  newitem.appendChild(itemtxt);
  document.getElementById("thelist").appendChild(newitem);

  newitem.addEventListener("click", function(event){
    document.getElementById("thelist").removeChild(newitem);
  });

  newitem.addEventListener("mouseover", function(event){
    document.getElementById("h").innerHTML = (event.target.innerText || event.target.textContent);
  });

  newitem.addEventListener("mouseout", function(event){
    document.getElementById("h").innerHTML = "Hello World!";
  });
}