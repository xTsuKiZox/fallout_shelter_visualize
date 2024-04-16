var userAgent = navigator.userAgent;
var deviceInfo = {};

if (userAgent.match(/iPhone/i) || userAgent.match(/iPad/i)) {
    deviceInfo.brand = 'Apple';
} else if (userAgent.match(/Android/i)) {
    deviceInfo.brand = 'Android';
} else {
    deviceInfo.brand = 'Unknown';
}

// console.log(deviceInfo);
