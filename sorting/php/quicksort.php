<?php 
 // quicksort
function partition (&$arr, $low, $high){
    $pivot = $arr[$high];
    $i = $low - 1;
    for ($j=$low; $j<$high; $j++){
        if ($arr[$j]<$pivot){
            $i++;
            $temp = $arr[$i];
            $arr[$i] = $arr[$j];
            $arr[$j] = $temp;
        }
    }
    $temp = $arr[$i+1];
    $arr[$i+1] = $arr[$high];
    $arr[$high] = $temp;
    return $i+1;
}

function quicksort(&$arr, $low, $high){
    if ($low < $high){
        $pi = partition($arr, $low, $high);
        quicksort($arr, $low, $pi-1);
        quicksort($arr, $pi+1, $high);
    }
}
// test 
$arr = array(7,6,4,2,1,3,5);
$n = count($arr);
quicksort($arr, 0, $n-1);
for ($i=0; $i<$n; $i++){
    echo $arr[$i];
    echo " ";
}

echo "<br>";
?>
