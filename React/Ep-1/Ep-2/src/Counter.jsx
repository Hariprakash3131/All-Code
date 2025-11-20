import { useState,useEffect,useContext,useRef } from "react"
import { dataContext } from "./Home";
function Counter(){
    const [count,setCount]=useState(0);

      let refCount=useRef(0);



    const data=useContext(dataContext);


    function inc(){
       // setCount(count+1);  //setCount(c=>c+1);  -> (preCount=>preCount+1)
        refCount.current+=1;
        // setCount(c=>c+1);  //Batch update function
    }
    useEffect(()=>{
       // console.log(count);
        console.log(refCount);

    });

    return(
         <>
          <h1>{data}</h1>
           <h1 className="m-5">{refCount.current}</h1>
           <button className="mx-5 btn btn-primary" onClick={inc}>Up</button>
           <button className="btn btn-secondary" onClick={()=>{setCount(refCount.current)}}>Update</button>
         </>
    )
}
export default Counter