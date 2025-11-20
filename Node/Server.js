const http=require('http')
const fs=require('fs')
const server=http.createServer((req,res)=>{
    
    res.setHeader('Content-Type','text/html')
     console.log(req.url)
     let path='./Docs/'

     if(req.url=='/home'||req.url=='/'){
        path+='index.html'
     }
     else if(req.url=='/joinus'||req.url=='/joinus'){
        path+='join.html'
     }
     else if(req.url=='/about'){
        path+='about.html'
     }
     else{
        path+='notFound.html'
     }

    fs.readFile(path,(err,data)=>{
       
        if(err){
            console.log(err.message)
            res.end()
        }
        else{
            
            res.end(data)
        }
    })
    
});
server.listen(4000, 'localhost', () => {
    console.log("Server is listening on port 4000");
});


