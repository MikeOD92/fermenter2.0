import React, { useRef } from "react";
import axios from "axios";
import { SyntheticEvent } from "react";

export default function Register() {
  const firstName = useRef<HTMLInputElement | null>(null);
  const lastName = useRef<HTMLInputElement | null>(null);
  const userName = useRef<HTMLInputElement | null>(null);
  const regEmail = useRef<HTMLInputElement | null>(null);
  const password = useRef<HTMLInputElement | null>(null);
  const confirm = useRef<HTMLInputElement | null>(null);

  const loginUser = useRef<HTMLInputElement | null>(null);
  const loginPass = useRef<HTMLInputElement | null>(null);

  const register = async (e: SyntheticEvent) => {
    e.preventDefault();
    if (password.current.value === confirm.current.value)
      console.log("helloworld");
    //   const response = await axios.post("http://localhost:8000/api/register",{
    //     "username": userName.current.value,
    //     "first_name"
    //     "last_name"
    //     "email"
    //     "password"
    //   })
  };
  return (
    <div className="w-full max-w-xl m-auto">
      <div id="registerFrom">
        <h2> Register</h2>
        <form className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
          <div className="mb-4">
            <input
              className="mr-3"
              type="text"
              placeholder="first name"
              ref={firstName}
            />
            <input
              className="mr-3"
              type="text"
              placeholder="last name"
              ref={lastName}
            />
          </div>
          <div className="mb-4">
            <input
              className="mr-3"
              type="text"
              placeholder="username"
              ref={userName}
            />
            <input
              className="mr-3"
              type="email"
              placeholder="email"
              ref={regEmail}
            />
          </div>
          <div className="mb-5">
            <input
              className="mr-3"
              type="password"
              placeholder="password confirm"
              ref={confirm}
            />
            <input
              className="mr-3"
              type="password"
              placeholder="password"
              ref={password}
            />
          </div>

          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full"
            type="submit"
          >
            {" "}
            Register
          </button>
        </form>
      </div>
      <div id="signinForm">
        <h2> Sign in </h2>
        <form className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
          <div className="mb-5">
            <input
              className="mr-3"
              type="text"
              placeholder="username"
              ref={loginUser}
            />
            <input
              className="mr-3"
              type="email"
              placeholder="email"
              ref={loginPass}
            />
          </div>
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full"
            type="submit"
          >
            {" "}
            Sign in
          </button>
        </form>
      </div>
    </div>
  );
}
