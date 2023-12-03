// You are given a 0-indexed array of strings nums, where each string is of equal length and consists of only digits.

// You are also given a 0-indexed 2D integer array queries where queries[i] = [ki, trimi]. For each queries[i], you need to:

// Trim each number in nums to its rightmost trimi digits.
// Determine the index of the kith smallest trimmed number in nums. If two trimmed numbers are equal, the number with the lower index is considered to be smaller.
// Reset each number in nums to its original length.
class Pair {
  String value;
  int index;

  Pair(this.value, this.index);
}

class MinHeap {
  List<Pair> _data = [];

  int get size => _data.length;

  int left(int i) => 2 * i + 1;
  int right(int i) => 2 * i + 2;
  int parent(int i) => (i - 1) >> 1;

  void insert(Pair pair) {
    _data.add(pair);
    int i = size - 1;
    while (i != 0 && _data[parent(i)].value.compareTo(_data[i].value) > 0) {
      var temp = _data[i];
      _data[i] = _data[parent(i)];
      _data[parent(i)] = temp;
      i = parent(i);
    }
  }

  void minHeapify(int i) {
    var l = left(i);
    var r = right(i);
    var smallest = i;

    if (l < size && _data[l].value.compareTo(_data[i].value) < 0) {
      smallest = l;
    }
    if (r < size && _data[r].value.compareTo(_data[smallest].value) < 0) {
      smallest = r;
    }

    if (smallest != i) {
      var temp = _data[i];
      _data[i] = _data[smallest];
      _data[smallest] = temp;
      minHeapify(smallest);
    }
  }

  Pair extractMin() {
    if (size == 0) {
      throw Exception("Heap underflow");
    }
    if (size == 1) {
      return _data.removeLast();
    }

    Pair root = _data[0];
    _data[0] = _data.removeLast();
    minHeapify(0);
    return root;
  }

  Pair getMin() => _data[0];

  void removeLargest() {
    // Find the index of the largest element
    int i = _data.indexWhere((pair) =>
        pair.value ==
        _data
            .reduce((curr, next) =>
                curr.value.compareTo(next.value) > 0 ? curr : next)
            .value);

    // Check if the largest element is the last element in the heap
    if (i == _data.length - 1) {
      _data.removeLast();
    } else {
      // Replace the largest element with the last element and heapify
      _data[i] = _data.removeLast();
      minHeapify(i);
    }
  }

  void ensureMaxSize(int k) {
    while (size > k) {
      removeLargest();
    }
  }
}

class Solution {
  List<int> smallestTrimmedNumbers(List<String> nums, List<List<int>> queries) {
    var results = List<int>.filled(queries.length, 0);
    for (var q = 0; q < queries.length; q++) {
      var k = queries[q][0];
      var trim = queries[q][1];
      var trimmedpairs = List<Pair>.generate(nums.length, (i) {
        var num = nums[i];
        if (num.length > trim) {
          num = num.substring(num.length - trim);
        }
        return Pair(num, i);
      });

      // Sort the trimmed array using heap sort
      // Sort the trimmed array using heap sort
      var heap = MinHeap();
      for (var pair in trimmedpairs) {
        heap.insert(pair);
        heap.ensureMaxSize(k);
      }
      results[q] = heap
          .extractMin()
          .index; // Directly get the index of the k-th smallest element
    }
    return results;
  }
}
