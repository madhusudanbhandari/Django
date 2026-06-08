import React from "react";
import { Link } from "react-router-dom";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function LoginForm() {

    const navigate=useNavigate();

    const[form, setForm]=useState({
        "username":'',
        "password":'',
    })
    
    const [loading, setLoading]=useState(false)

    const handleChange=(e)=>{
        setForm({...form,[e.target.name]:e.target.value})

    }



    const handleSubmit=async(e)=>{
        e.preventDefault()
        setLoading(true)

        try{
            const response=await fetch('http://127.0.0.1:8000/api/login/',{
                    method:'POST',
                    headers:{
                        'Content-Type':'application/json'
                    },
                    body:JSON.stringify(form)
            });
            const data = await response.json();

            if (!response.ok) {
                console.log("Login failed:", data);
                return;
            }
            console.log("Login successful:", data);

            localStorage.setItem('access',data.access);
            localStorage.setItem('refresh',data.refresh);
            navigate('todo/');
        } catch (error) {
            console.error("Error:", error);
        } finally {
            setLoading(false); 
        }
    };




  return (
   
        
    <div className="flex min-h-screen items-center justify-center bg-slate-50 p-4">
      <div className="w-full max-w-sm rounded-xl bg-white p-6 shadow-xl border border-slate-200">
        <h2 className="mb-6 text-center text-2xl font-semibold text-slate-800">
          Sign In
        </h2>
        
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-xs font-medium text-slate-500 mb-1">
              Username
            </label>
            <input
              type="text"
              name='username'
              value={form.username}
              onChange={handleChange}
              placeholder="Enter your username"
              className="w-full rounded-md bg-slate-50 border border-slate-300 px-3 py-2 text-sm text-slate-800 placeholder-slate-400 outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500"
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-500 mb-1">
              Password
            </label>
            <input
              type="password"
              name='password'
              onChange={handleChange}
              value={form.password}
              placeholder="Enter password"
              className="w-full rounded-md bg-slate-50 border border-slate-300 px-3 py-2 text-sm text-slate-800 placeholder-slate-400 outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500"
            />
          </div>

          <button
            type="submit"
            className="w-full rounded-md bg-sky-600 py-2 text-sm font-medium text-white hover:bg-sky-500 transition-colors"
          >
            Log In
          </button>
        </form>
        <p>Dont have an account? </p>
        <Link to='register/'>Register</Link>

      </div>
    </div>
   
  );
}
