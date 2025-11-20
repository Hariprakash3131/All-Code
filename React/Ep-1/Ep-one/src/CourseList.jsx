import './App.css'
import Course from './Course';
import Html from './assets/Html.jpg';
import loadingGif from './assets/loading-loading-gif.gif'; 
// import css from './assets/css.jpeg';
// import js from './assets/js.png';
import { useState,useEffect } from 'react';
import useFetch from './useFetch';
function CourseList(){


   
    const [courses,dummy,error]=useFetch('http://localhost:3000/courses');
    


    function handleDelete(id){
        console.log(id);
        const newCourse=courses.filter((course)=>course.id != id)
        setCourses(newCourse);
    }


    //  courses.sort((x,y)=>y.price -x.price) //Sorting to the price
    //  const minCourses=courses.filter((course)=>course.price<20000)

    if(!courses){
        return (
            <>
         {!error && <img src={loadingGif} alt="Loading..." />}
 
           {error&& <p>{error}</p>}
            </>
        )
        
    }

    const coursesList= courses.map(
        (course)=> <Course key={course.id}
        name={course.name}
        img={course.img} 
        price={course.price}
        delete={handleDelete} 
        id={course.id}/>);

   
    return(
        <>
        {coursesList}
         <button onClick={()=>{setDummy(false)}}>Dummy</button>
        </>

    );
}
export default CourseList;


//npx json-server --watch Ep-one\data\dummyData.json --port 3000 --static Ep-one\src\assets