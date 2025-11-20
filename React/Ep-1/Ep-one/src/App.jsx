import Navbar from './Navbar';
import Course from './Course';
import Footer from './Footer';
import './App.css'
// import Html from './assets/Html.jpg';
// import css from './assets/css.jpeg';
// import js from './assets/js.png';
import CourseList from './CourseList';
function App() {

  return (
    <>
   
     {/* <Course name="HTML" price="Rs.200" img={Html} show={true} />
     <Course name="CSS" price="Rs.100"  img={css} show={true}/>
     <Course name="JS" price="Rs.1200" img={js} show={true}/> */}
     <CourseList/>
    

    </>
  );
}

export default App
