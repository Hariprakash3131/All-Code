import { useState } from "react";
import { useParams } from "react-router-dom"
function Post(){
    const [post,setPost]=useState();
    const {id}=useParams();
    
     fetch('http://localhost:4000/posts/'+id)
        .then(response => response.json())
        .then((data) => {
            console.log(data);
            setPost(data); // ✅ Set received data into state
        })
        .catch(err => {
            console.log(err);
        });


    return(
        <div>
           {post&& <div className="container m-5">
              Post:{id}
              <h2>{post.title}</h2>
              <h4>{post.content}</h4>
          </div>}
          </div>
    )
}
export default Post