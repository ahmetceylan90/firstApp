myDict = {
"file1" : "ba.png",
"file2" : "ba.jpg",
"file3" : "ba.gif",
"file4" : "ba.png",
"file5" : "ba.tff",
"file6" : "ba.mp3",
"file7" : "ba.mp4",
"file8" : "ba.jpg",
"file9" : "ba.gif",
"file10" : "ba.png",
"file11" : "ba.gif"
} 



result = list(filter(lambda n: "png" in n , myDict))

print(result)




