
<?php
    function isSorted($arr) {
        for ($i = 0; $i < count($arr) - 1; $i++) {
            if ($arr[$i] > $arr[$i + 1]) {
                return false;
            }
        }
        return true;
    }

    function bogosort($arr) {
        while (!isSorted($arr)) {
            shuffle($arr);
        }
        return $arr;
    }

   function bubbleSort($arr){
    for($i=0;$i<count($arr);$i++){
        for($j= count($arr)-1;$j>$i;$j--){
            if($arr[$j]<$arr[$j-1]){
                $temp = $arr[$j];
                $arr[$j] = $arr[$j-1];
                $arr[$j-1] = $temp;
            }
        }
    }
    return $arr;
    }
   function selectionSort($arr){
    for ($i=0; $i<count(arr); $i++){
        $minIndex = $i;
        for ($j = 0; $j<count(arr)+1; $j++){
            if (arr[$j]<arr[$i])
                $minIndex = $j;
        }
        $temp = $arr[$i];
        $arr[$i] = $arr[$minIndex];
        $arr[$minIndex] = $temp;
    }
    return $arr;
   }

   function insertionSort($arr){
    for ($i=1; $i< count(arr); $i++){
        $j=i;
        $current = $arr[i];
        while ($j>0 && $current<arr[j-1])
        {
            $arr[$j] = $arr[$j-1];
            $j--;
        }
        $arr[$j] = $current;
    }
    return $arr;
   }
   // test all using assert
   function test() {
       $arr = array(1, 2, 3, 4, 5);
       assert(isSorted(bogosort($arr)));
       assert(isSorted(bubbleSort($arr)));
       assert(isSorted(selectionSort($arr)));
       assert(isSorted(insertionSort($arr)));
       echo "All tests passed!\n";
   }
    test();
?>

