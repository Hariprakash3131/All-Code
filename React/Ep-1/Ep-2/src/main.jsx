import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import Login from './Login'
import Home from './Home'
import NotFound from './NotFound'
import Counter from './Counter'
import Post from './Post'
import {createBrowserRouter,RouterProvider} from 'react-router-dom'

const router=createBrowserRouter([
  {
    path:'/',
    element:<Home/>,
    errorElement:<NotFound/>
    
  },
  {
    path:'/login',
    element:<Login/>
  },
  {
    path:'/counter',
    element:<Counter/>
  }
  ,{
    path:'/post/:id',
    element:<Post/>
  }
]);
createRoot(document.getElementById('root')).render(
  
  
    <RouterProvider router={router}/>


)
