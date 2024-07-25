func canPlaceFlowers(flowerbed []int, n int) bool {
	zeros := 0
	if flowerbed[0] == 0 && flowerbed[1] == 1{
       n -= 1
	}
	for i := 1; i < len(flowerbed); i++{
		if flowerbed[i] == 0{
			zeros += 1
		} else {
			zeros = 0
		}
		if zeros == 3{
			n -= 1 
		}
	}
	
	if flowerbed[len(flowerbed)-1] == 0 && flowerbed[len(flowerbed)-2] == 1{
		n -= 1
	 }
	return n<=0
}