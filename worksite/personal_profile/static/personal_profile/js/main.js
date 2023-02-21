//console.log('hello world')
const countdownBox = document.getElementById('countdown-box')
time = countdownBox.textContent
console.log(time)
const now = new Date()
const split_time = time.split(':')
expected_hours = parseInt(now.getHours(), 10) +
parseInt(split_time[0], 10);
expected_minutes = parseInt(now.getMinutes(), 10) +
parseInt(split_time[1], 10);
const new_date = new Date();
new_date.setHours(expected_hours)
new_date.setMinutes(expected_minutes)

setInterval(()=>{
    const now = new Date()
    console.log(new_date)
    console.log(expected_hours, expected_minutes)
    access_true = Date.parse(new_date)
    current_seconds = Date.parse(now)
    console.log(access_true)
    console.log(current_seconds)
    diff = access_true - current_seconds
    console.log(diff)
    const h = Math.floor((now / (1000 * 60 * 60 * 24) - (new_date / (1000 * 60 * 60))) % 24
    const m = Math.floor(now / ())
    console.log(h)

}, 1000)