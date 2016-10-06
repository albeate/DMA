let rec gcd a b = 
    if b = 0 then 
        a
    else
        (gcd b (a % b))

let a = 14
let b = 15
printf "%A\n" (gcd a b)