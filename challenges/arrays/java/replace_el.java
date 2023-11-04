import java.util.Stack;

public class replace_el {
    public int[] replaceElements(int[] arr) {
        // declare stack
        Stack<Integer> stack = new Stack<Integer>();
        int[] result = new int[arr.length];
        result[arr.length - 1] = -1;
        stack.push(arr[arr.length - 1]);
        for (int i = arr.length - 2; i >= 0; i--) {
            result[i] = stack.peek();
            if (arr[i] > stack.peek()) {
                stack.pop();
                stack.push(arr[i]);
            }
        }
        return result;
    }
}
