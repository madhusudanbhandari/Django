import React, { useEffect, useState } from "react";

export default function Todo() {
  const access = localStorage.getItem("access");

 
  const [todos, setTodos] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const [form, setForm] = useState({
    title: "",
    description: "",
    date: "",
    completed: false,
  });

  const [editingId, setEditingId] = useState(null);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;

    setForm({
      ...form,
      [name]: type === "checkbox" ? checked : value,
    });
  };

  const fetchTodos = async () => {
    try {
      setLoading(true);

      const res = await fetch("http://127.0.0.1:8000/api/todos/", {
        headers: {
          Authorization: `Bearer ${access}`,
        },
      });

      if (!res.ok) throw new Error("Failed to fetch todos");

      const data = await res.json();
      setTodos(data);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTodos();
  }, []);

 
  const createTodo = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch("http://127.0.0.1:8000/api/todos/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${access}`,
        },
        body: JSON.stringify(form),
      });

      if (!res.ok) throw new Error("Create failed");

      setForm({
        title: "",
        description: "",
        date: "",
        completed: false,
      });

      fetchTodos(); 
    } catch (err) {
      console.log(err);
    }
  };

  
  const deleteTodo = async (id) => {
    try {
      const res = await fetch(
        `http://127.0.0.1:8000/api/todos/${id}/`,
        {
          method: "DELETE",
          headers: {
            Authorization: `Bearer ${access}`,
          },
        }
      );

      if (!res.ok) throw new Error("Delete failed");

      fetchTodos(); // refresh list
    } catch (err) {
      console.log(err);
    }
  };

  
  const startEdit = (todo) => {
    setEditingId(todo.id);
    setForm({
      title: todo.title,
      description: todo.description,
      date: todo.date,
      completed: todo.completed,
    });
  };

  const updateTodo = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch(
        `http://127.0.0.1:8000/api/todos/${editingId}/`,
        {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${access}`,
          },
          body: JSON.stringify(form),
        }
      );

      if (!res.ok) throw new Error("Update failed");

      setEditingId(null);
      setForm({
        title: "",
        description: "",
        date: "",
        completed: false,
      });

      fetchTodos();
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-6">

      <h1 className="text-2xl font-bold mb-4">Todo App</h1>

      {loading && <p>Loading...</p>}
      {error && <p className="text-red-500">{error}</p>}

      <p>My todos</p>
      <div className="space-y-3 mb-6">
        {todos.map((todo) => (
          <div
            key={todo.id}
            className="p-3 border rounded flex justify-between"
          >
            <div>
              <h3 className="font-semibold">{todo.title}</h3>
              <p className="text-sm">{todo.description}</p>
              <p className="text-xs text-gray-500">{todo.date}</p>
              <p className="text-xs">
                {todo.completed ? "Done" : "Pending"}
              </p>
            </div>

            <div className="space-x-2">
              <button
                onClick={() => startEdit(todo)}
                className="px-2 py-1 bg-yellow-400"
              >
                Edit
              </button>

              <button
                onClick={() => deleteTodo(todo.id)}
                className="px-2 py-1 bg-red-500 text-white"
              >
                Delete
              </button>
            </div>
          </div>
        ))}
      </div>

      {/* FORM */}
      <form
        onSubmit={editingId ? updateTodo : createTodo}
        className="space-y-3 border p-4 rounded"
      >
        <h2 className="font-bold">
          {editingId ? "Update Todo" : "Create Todo"}
        </h2>

        <input
          name="title"
          value={form.title}
          onChange={handleChange}
          placeholder="Title"
          className="border p-2 w-full"
        />

        <textarea
          name="description"
          value={form.description}
          onChange={handleChange}
          placeholder="Description"
          className="border p-2 w-full"
        />

        <input
          type="date"
          name="date"
          value={form.date}
          onChange={handleChange}
          className="border p-2 w-full"
        />

        <label className="flex items-center gap-2">
          <input
            type="checkbox"
            name="completed"
            checked={form.completed}
            onChange={handleChange}
          />
          Completed
        </label>

        <button className="bg-blue-500 text-white px-4 py-2">
          {editingId ? "Update" : "Create"}
        </button>
      </form>
    </div>
  );
}