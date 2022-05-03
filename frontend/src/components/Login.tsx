import React, { useRef, SyntheticEvent } from "react";
import axios from "axios";

export default function Login() {
  const loginUser = useRef<HTMLInputElement | null>(null);
  const loginPass = useRef<HTMLInputElement | null>(null);

  const login = async (e: SyntheticEvent) => {
    e.preventDefault();
    if (loginUser.current?.value && loginPass.current?.value) {
      const response = await axios.post("http://localhost:8000/api/login", {
        username: loginUser.current.value,
        password: loginPass.current.value,
      });
      console.log(response);
    }
  };
  return (
    <>
      <h2> Sign in </h2>
      <form
        onSubmit={login}
        className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4"
      >
        <div className="mb-5">
          <input
            className="mr-3"
            type="text"
            placeholder="username"
            ref={loginUser}
          />
          <input
            className="mr-3"
            type="password"
            placeholder="password"
            ref={loginPass}
          />
        </div>
        <button
          className="bg-gradient-to-r from-orange-400 via-red-500 to-pink-500 text-white font-bold py-2 px-4 rounded-full"
          type="submit"
        >
          {" "}
          Sign in
        </button>
      </form>
    </>
  );
}
