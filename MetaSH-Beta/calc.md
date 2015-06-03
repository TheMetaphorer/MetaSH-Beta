# calc #

The calc command allows you to calculate mathematical expressions inside of the
shell. It's expression syntax is straight forward, the operators are  
+, -, /, *, %, (remainder division) //, (floor division), **, (exponents),
sqrt, and rt.

You are most likely familiar with the 5 main operators, +, -, /, *, and **, so
I will not go over those ones. I will explain the // operator, the % operator,
and the rt operator.

// does floor division. Floor division rounds and decimal to that integer. For
example:

`calc 17 / 3` will return 5.666666667, but if you do

`calc 17 // 3`, it will return 5.

% does remainder division. So, it will do the division, and will return the
remainder. This can be useful for finding, prime numbers for example.

`calc 17 % 3` will return 2.

The rt operator does roots. For example,

`calc 2 rt 25` is also the same as `calc sqrt 25`, and both commands will
return 5.

You can calc cube roots, by doing 3 rt 25, or fourth roots, by doing 4 rt 25.
