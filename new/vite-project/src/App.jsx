import { useState } from 'react'
import {Route,Routes,BrowserRouter} from 'react-router-dom'
import Login from './pages/Login'
import Register from './pages/Register'
import Todo from './pages/Todo'

export default function App() {
      return (
          <div>
            <BrowserRouter>
              <Routes>
                <Route path='/' element={<Login/>}></Route>
                <Route path='register/' element={<Register/>}></Route>
                <Route path='todo/' element={<Todo/>}></Route>
              </Routes>
            </BrowserRouter>
          </div>
        )
}


