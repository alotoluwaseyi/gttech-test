# On this day, Nov 29, 2018, scrape the https://punchng.com/ sections as listed below
# 1. JUST IN
# 2. TRENDING
# Return the output as a JSON in Javascript

dataJustIn = document.querySelectorAll("h3");
response = {};
for(let i = 0; i < dataJustIn.length; i++){
response[i] = dataJustIn[i].textContent
}
document.write(JSON.stringify(response));


dataTrending = document.querySelectorAll("h1");
response = {};
for(let i = 0; i < dataTrending.length; i++){
response[i] = dataTrending[i].textContent
}
document.write(JSON.stringify(response));

