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

