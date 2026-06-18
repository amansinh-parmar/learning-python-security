import React, { useEffect, useState } from "react";
import axios from "axios";
import "./index.css";

function App() {
  // Always keep todos as an array
  const [todos, setTodos] = useState([]);

  const [task, setTask] = useState("");

  // Get all todos from backend
  const fetchTodos = async () => {
    try {
      const res = await axios.get("http://localhost:5000/todos");

      // Make sure response is an array
      setTodos(res.data);
    } catch (error) {
      console.log("Error fetching todos:", error);
    }
  };

  // Load todos when app starts
  useEffect(() => {
    fetchTodos();
  }, []);

  // Add new todo
  const addTodos = async () => {
    if (!task.trim()) return;

    try {
      await axios.post("http://localhost:5000/todos", {
        task: task,
      });

      // Clear input
      setTask("");

      // FIX:
      // Do NOT do setTodos()
      // It makes todos undefined
      //
      // Reload list after adding
      fetchTodos();
    } catch (error) {
      console.log("Error adding todo:", error);
    }
  };

  // Complete / uncomplete todo
  const toggleTodo = async (id) => {
    try {
      await axios.put(`http://localhost:5000/todos/${id}`);

      fetchTodos();
    } catch (error) {
      console.log(error);
    }
  };

  // Delete todo
  const deleteTodo = async (id) => {
    try {
      await axios.delete(`http://localhost:5000/todos/${id}`);

      fetchTodos();
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex justify-center items-center">
      <div className="bg-white shadow-xl rounded-xl p-8 w-full max-w-md">
        <h1 className="text-3xl font-bold text-center text-blue-600 mb-6">
          To-Do List
        </h1>

        <div className="flex gap-2 mb-5">
          <input
            value={task}
            onChange={(e) => setTask(e.target.value)}
            placeholder="Enter task"
            className="
            flex-1
            border
            rounded-lg
            px-4
            py-2
            outline-none
            focus:ring-2
            focus:ring-blue-400
          "
          />

          <button
            onClick={addTodos}
            className="
            bg-blue-600
            text-white
            px-5
            rounded-lg
            hover:bg-blue-700
            transition
          "
          >
            Add
          </button>
        </div>

        <ul className="space-y-3">
          {todos?.map((todo) => (
            <li
              key={todo.id}
              className="
              flex
              justify-between
              items-center
              bg-gray-50
              p-3
              rounded-lg
              shadow-sm
            "
            >
              <span
                onClick={() => toggleTodo(todo.id)}
                className={`
                cursor-pointer
                text-lg
                ${
                  todo.completed
                    ? "line-through text-gray-400"
                    : "text-gray-800"
                }
              `}
              >
                {todo.task}
              </span>

              <button
                onClick={() => deleteTodo(todo.id)}
                className="
                bg-red-500
                text-white
                px-3
                py-1
                rounded
                hover:bg-red-600
              "
              >
                Delete
              </button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
