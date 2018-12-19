var fibonacci = (n) => {
  var window = [0, 1];
    
  if(n < 2){
    return window[n];
  }else{
    var inc = 2;
    while(inc <= n){
      window[inc % 2] = window[(inc + 1) % 2] + window[inc % 2];
      inc++;
    }
    return window[(inc - 1) % 2];
  }
}

var gcd = (a, b) => {
  if(b == a){
    return a;
  }else if(a == 0){
    return b;
  }else if(b == 0){
    return a;
  }else{
    if(b > a){
      b = b % a;
      return gcd(a, b);
    }else{
      a = a % b;
      return gcd(a, b);
    }
  }
}

var randomStudent = () => {
  var names = ["brian", "amy", "catherine"];
  return names[Math.floor(Math.random() * 3)];
}
