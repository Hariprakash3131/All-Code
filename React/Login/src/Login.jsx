import {useState} from 'react'
import './Login.css'
function Login() {
    const [pwd1,setPwd1]=useState('');
    const [pwd2,setPwd2]=useState('');
    const [same,setSame]=useState(true);

    function handlePwd1Change(event){
        setPwd1(event.target.value);

    }

      function handlePwd2Change(event){
        setPwd2(event.target.value);
        if(pwd1==event.target.value){
            console.log("Same")
            setSame(true)

        }
        else{
            console.log('Not a Same')
            setSame(false)
        }
        
    }


 

  return (
    <>
    <div className='Bg-Image'>
    <div
      className="d-flex justify-content-center align-items-center"
      style={{ height: '100vh' }} // Full viewport height
    >
      <form className="p-4 border rounded shadow" style={{ width: '30%' }}>
        <div className="mb-3">
          <label htmlFor="exampleInputEmail1" className="form-label">
            Email address
          </label>
          <input
            type="email"
            className="form-control"
          
            aria-describedby="emailHelp"
          />
        </div>

        <div className="mb-3">
          <label htmlFor="exampleInputPassword1" className="form-label">
            Password
          </label>
          <input
            value={pwd1}
            onChange={handlePwd1Change}
            type="password"
            className="form-control"
          
          />
        </div>

        <div className="mb-3">
          <label htmlFor="exampleInputPassword1" className="form-label">
           Re-Enter Password
          </label>
          <input
            value={pwd2}
            onChange={handlePwd2Change}
            type="password"
            className="form-control"
            
          />
        </div>

        <div className="mb-3 form-check">
          <input
            type="checkbox"
            className="form-check-input"
        
          />
          <label className="form-check-label" htmlFor="exampleCheck1">
            Check me out
          </label>
        </div>
        {!same &&<p>Password DoesNot Match</p>}

        <button type="submit" className="btn btn-primary w-100">
          Submit
        </button>
      </form>
    </div>
    </div>
    </>
  );
}

export default Login;
