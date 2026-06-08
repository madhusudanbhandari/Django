import React from "react";
import { Link } from "react-router-dom";
import { useState } from "react";


export default function RegisterForm() {
    const[form, setForm]=useState({
        "username":'',
        "email":'',
        "password":'',
        "gender":"",
        "age":""
    })
    const [loading, setLoading]=useState(false)

    const handleChange=(e)=>{
        setForm({...form,[e.target.name]:e.target.value})

    }

    

    const handleSubmit=async(e)=>{
        e.preventDefault()
        setLoading(false)

        try{
        const response=await fetch('http://127.0.0.1:8000/api/register/',{
                method:'POST',
                headers:{
                    'Content-Type':'application/JSON'
                },
                body:JSON.stringify(form)
        });
         const data = await response.json();
            console.log("Success:", data);
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
          Register
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
              Email
            </label>
            <input
              type="email"
              name='email'
              value={form.email}
              onChange={handleChange}
              placeholder="Enter your email"
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
          <div>
            <label className="block text-xs font-medium text-slate-500 mb-1">
              Gender
            </label>
            <input
              type="text"
              name='gender'
              value={form.gender}
              onChange={handleChange}
              placeholder="Enter your gender"
              className="w-full rounded-md bg-slate-50 border border-slate-300 px-3 py-2 text-sm text-slate-800 placeholder-slate-400 outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500"
            />
          </div>
          <div>
            <label className="block text-xs font-medium text-slate-500 mb-1">
                Age
            </label>
            <input
              type="number"
              name='age'
              value={form.age}
              onChange={handleChange}
              placeholder="Enter your age"
              className="w-full rounded-md bg-slate-50 border border-slate-300 px-3 py-2 text-sm text-slate-800 placeholder-slate-400 outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500"
            />
          </div>

          <button
            type="submit"
            className="w-full rounded-md bg-sky-600 py-2 text-sm font-medium text-white hover:bg-sky-500 transition-colors"
          >
            Register
          </button>
        </form>
        <p>Already have an account? </p>
        <Link to='/'>Login</Link>

      </div>
    </div>
  );
}
