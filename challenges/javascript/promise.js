function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const data = 'Here is some data';
            const error = null;

            if (error) {
                reject('Failed to fetch data');
            } else {
                resolve(data);
            }
        }, 2000); // Simulate a delay of 2 seconds
    });
}

fetchData().then((data) => {
    console.log('Data:', data);
}).catch((error) => {
    console.error('Error:', error);
});


// add two promises together
let promise1 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve(1);
    }, 2000);
}
);

let promise2 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve(2);
    }, 2000);
}

);

var addTwoPromises = async function (promise1, promise2) {
    let values = await Promise.all([promise1, promise2]);
    return values.reduce((a, b) => a + b, 0);
};

// sleeping for mills

/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    return new Promise(resolve => setTimeout(resolve, millis));
}

// cancel t millisecond

/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function (fn, args, t) {
    // Schedule the execution of fn after t milliseconds
    // and store the timeout ID in timeoutId
    let timeoutId = setTimeout(() => fn.apply(null, args), t);

    // Return a new function that, when called, cancels the scheduled execution of fn
    return function cancelFn() {
        clearTimeout(timeoutId);
    };
};

/**
 *  const result = [];
 *
 *  const fn = (x) => x * 5;
 *  const args = [2], t = 20, cancelTimeMs = 50;
 *
 *  const start = performance.now();
 *
 *  const log = (...argsArr) => {
 *      const diff = Math.floor(performance.now() - start);
 *      result.push({"time": diff, "returned": fn(...argsArr)});
 *  }
 *       
 *  const cancel = cancellable(log, args, t);
 *
 *  const maxT = Math.max(t, cancelTimeMs);
 *           
 *  setTimeout(cancel, cancelTimeMs);
 *
 *  setTimeout(() => {
 *      console.log(result); // [{"time":20,"returned":10}]
 *  }, maxT + 15)
 */



/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
let results = [];
let time = 0;

var cancellable = function (fn, args, t) {
    let intervalId;

    // Call the function immediately
    results.push({ "time": time, "returned": fn.apply(null, args) });

    // Set up the interval
    intervalId = setInterval(() => {
        time += t;
        results.push({ "time": time, "returned": fn.apply(null, args) });
    }, t);

    // Return the cancel function
    return function cancelFn() {
        clearInterval(intervalId);
    }
};

/**
 *  const result = [];
 *
 *  const fn = (x) => x * 2;
 *  const args = [4], t = 35, cancelTimeMs = 190;
 *
 *  const start = performance.now();
 *
 *  const log = (...argsArr) => {
 *      const diff = Math.floor(performance.now() - start);
 *      result.push({"time": diff, "returned": fn(...argsArr)});
 *  }
 *       
 *  const cancel = cancellable(log, args, t);
 *
 *  setTimeout(cancel, cancelTimeMs);
 *   
 *  setTimeout(() => {
 *      console.log(result); // [
 *                           //     {"time":0,"returned":8},
 *                           //     {"time":35,"returned":8},
 *                           //     {"time":70,"returned":8},
 *                           //     {"time":105,"returned":8},
 *                           //     {"time":140,"returned":8},
 *                           //     {"time":175,"returned":8}
 *                           // ]
 *  }, cancelTimeMs + t + 15)    
 */


type Fn = (...params: any[]) => Promise<any>;

function timeLimit(fn: Fn, t: number): Fn {
    
    return async function(...args) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                reject('Time Limit Exceeded');
            }, t);
            fn(...args).then(resolve).catch(reject);
        });
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */