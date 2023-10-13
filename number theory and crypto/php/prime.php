<?php
// test if num is prime
function isPrime($num)
{
    if($num < 2)
        return false;
    else if($num == 2)
        return true;
    else if($num % 2 == 0)
        return false;
    for($i = 3; $i <= ceil(sqrt($num)); $i = $i + 2)
    {
        if($num % $i == 0)
            return false;
    }
    return true;
}

$num = 49;
echo "is $num prime? " . (isPrime($num) ? "yes" : "no") . "\n";
?>