/**
 * @param {string} val
 * @return {Object}
 */
var expect = function (val) {
    // create object
    var obj = {};
    // add toBe method
    obj.toBe = function (val2) {
        if (val !== val2) {
            throw new Error('Not Equal');
        }
        return true;
    };
    // add notToBe method
    obj.notToBe = function (val2) {
        if (val === val2) {
            throw new Error('Equal');
        }
        return true;
    };
    // return object
    return obj;
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */


/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function (init) {

    return {
        name: 'counter',
        value: init,

        increment: function () {
            return ++this.value;
        },
        decrement: function () {
            return --this.value;
        },
        reset: function () {
            return this.value = init;

        }
    };
};

// approach 2 using class 
class Counter {
    constructor(init) {
        this.init = init;
        this.value = init;
    }
    increment() {
        return ++this.value;
    }
    decrement() {
        return --this.value;
    }
    reset() {
        return this.value = this.init;
    }
}

var createCounter = function (init) {
    return new Counter(init);
}
/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */