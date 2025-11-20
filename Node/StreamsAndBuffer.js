const fs=require('fs')

const readStream=fs.createReadStream('./Docs/BigFile.txt')
const writeStream=fs.createWriteStream('./Docs/copyBigFile.txt');

// readStream.on('data',(buffer)=>{
//     // console.log("\nNew Buffer\n")
//     // console.log(buffer.toString())
//     writeStream.write('\n New Buffer \n')
//     writeStream.write(buffer)
// })


readStream.pipe(writeStream);