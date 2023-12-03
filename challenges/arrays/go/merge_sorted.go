package main

func merge(nums1 []int, m int, nums2 []int, n int) {
	i := m - 1 // last index of nums1
	j := n - 1 // last index of nums2
	k := m + n - 1
	for i >= 0 && j >= 0 {
		if nums1[i] > nums2[j] {
			nums1[k] = nums1[i]
			i--
			k--
		} else {
			nums1[k] = nums2[j]
			j--
			k--
		}
	}
	for j >= 0 {
		nums1[k] = nums2[j]
		j--
		k--
	}
}
func main() {
	nums1 := []int{1, 2, 3, 0, 0, 0}
	m := 3
	nums2 := []int{2, 5, 6}
	n := 3
	merge(nums1, m, nums2, n)
	for _, num := range nums1 {
		println(num)
	}
}
