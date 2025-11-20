import PropTypes from 'prop-types'
import {useState } from 'react'
import CourseList from './CourseList';
//const course2 =2+4 ;//->Do any js code
function Course(props) {
    // if(props.show==true){
    //let Purchased=false;
    const [Purchased, setPurchased]= useState(false);
    // const [discount,setDiscount]=useState(props.price);
    function BuyCourse(discount){
    console.log(props.name,"Purchased with",discount,"%discount");
    setPurchased(true);
    // setDiscount(discount-amt)

  }
  
    return (
    <div className="card">
      <img src={props.img} alt="" />
      <h3>{props.name}</h3>
      <p>{props.price}</p>
      {/* <button onClick={(event)=>BuyCourse(10,event)}>Apply Offers</button>
       */}
      <button onClick={(event)=>BuyCourse(20,event)}>Buy Now</button>
      <p>{Purchased ?"Already Purchased" :"Get it Now"}</p>
      <button onClick={()=>props.delete(props.id)}>Delete</button>
    </div>
  );
}
// else{
//     return(
//         <div className="card">Course not Available</div>
//     )
// }
 // }
// Course.defaultProps = {
//   name: "Soker",
//   price: "Rs.500", 
//   img: Html,
// };

// Course.propTypes={
//     name:PropTypes.string,
//     rating:PropTypes.number,
//     show:PropTypes.bool,
// }

export default Course;