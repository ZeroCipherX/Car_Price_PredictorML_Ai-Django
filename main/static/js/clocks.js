let clock = document.getElementById('clock');

setInterval(() => {
    let date = new Date();
    let options = {
        timeZone: 'Asia/Karachi' // PKT time zone
    };
    clock.innerHTML = date.toLocaleTimeString('en-US', options);
});

