var range = [20,30,32,234,12,46,3,456,874,37,64,52,8,165,49,15,23,56,16,13,4,91];
var threshold = 35;

var mountain = _.filter(range, function(data, index){
    return Math.abs(data - range[index+1]) > threshold;
});

document.write("Range: " + range);
document.write("<br><br>");
document.write("Mountain length: " + mountain.length);
