import React, { useRef, SyntheticEvent } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const firstName = useRef<HTMLInputElement | null>(null);
  const lastName = useRef<HTMLInputElement | null>(null);
  const userName = useRef<HTMLInputElement | null>(null);
  const regEmail = useRef<HTMLInputElement | null>(null);
  const password = useRef<HTMLInputElement | null>(null);
  const confirm = useRef<HTMLInputElement | null>(null);

  let navigate = useNavigate();

  const register = async (e: SyntheticEvent) => {
    e.preventDefault();
    if (
      password.current?.value === confirm.current?.value &&
      password.current?.value !== ""
    ) {
      const response = await axios.post("http://localhost:8000/api/register", {
        username: userName.current?.value,
        first_name: firstName.current?.value,
        last_name: lastName.current?.value,
        email: regEmail.current?.value,
        password: password.current?.value,
      });
      if (response.status === 200) {
        navigate("/home");
      }
      return response;
    } else {
      console.log("password does not match");
    }
  };
  return (
    <>
      <h2> Register</h2>
      <form
        onSubmit={register}
        className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4"
      >
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
          className="bg-gradient-to-r from-orange-400 via-red-500 to-pink-500 text-white font-bold py-2 px-4 rounded-full"
          type="submit"
        >
          {" "}
          Register
        </button>
      </form>
    </>
  );
}
