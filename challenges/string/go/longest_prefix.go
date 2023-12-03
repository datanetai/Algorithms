package main

func longestCommonPrefix(strs []string) string {
	prefix := ""
	if len(strs) == 0 {
		return prefix
	}
	prefix = strs[0]
	for i := 1; i < len(strs); i++ {
		prefix = commonPrefix(prefix, strs[i])
	}
	return prefix
}
func commonPrefix(s1, s2 string) string {
	prefix := ""
	for i := 0; i < len(s1) && i < len(s2); i++ {
		if s1[i] != s2[i] {
			break
		}
		prefix += string(s1[i])
	}
	return prefix
}
