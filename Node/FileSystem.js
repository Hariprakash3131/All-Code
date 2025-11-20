// // FileSystem
 const fs=require('fs')


if(! fs.existsSync('./docs')){
fs.mkdir('./docs', (err)=>{        //Folder Create
    if(err){
        console.log(err.message)
    }
    else{
        console.log("Folder Created")
    }
})
    console.log("Here Here")
}

fs.writeFile('./docs/file.txt',"soker da nee",(err)=>{
    if(err){
        console.log(err.message)
    }
    else{
        console.log("File written")
    }
})
if(fs.existsSync('./docs/file.txt')){
fs.readFile('./docs/file.txt',(err,data)=>{
    if(err){
        console.log(err.message)
    }
    else{
        console.log(data.toString())
    }
})
}

if(fs.existsSync('./docs/file.txt')){
    fs.unlink('./docs/file.txt',(err)=>{
        if(err){
            console.log(err.message)
        }
        else{
            console.log("file Deleted")
        }
    })
}
if(('./docs')){
fs.rmdir('./docs',(err)=>{
    if(err){
        console.log(err.message)

    }
    else{
        console.log("Folder Deleted")
    }
})
}