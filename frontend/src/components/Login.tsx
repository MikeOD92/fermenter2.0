import React, { useRef, SyntheticEvent } from "react";
import axios from "axios";
// import { useNavigate } from "react-router-dom";
// import { useAppDispatch } from "../hooks";
// import { login } from "../actions/userActions";
import { useDispatch, useSelector } from "react-redux";
import { bindActionCreators } from "@reduxjs/toolkit";
import { actionCreators } from "../redux";
import { State } from "../redux/reducers";

export default function Login() {
  const dispatch = useDispatch();

  const { login } = bindActionCreators(actionCreators, dispatch);
  const state = useSelector((state: State) => state);

  const loginUser = useRef<HTMLInputElement | null>(null);
  const loginPass = useRef<HTMLInputElement | null>(null);

  // const dispatch = useAppDispatch();
  // let navigate = useNavigate();
  // let dispatch = useAppDispatch();

  const userLogin = async (e: SyntheticEvent) => {
    e.preventDefault();
    if (loginUser.current !== null && loginPass.current !== null) {
      login(loginUser.current.value, loginPass.current.value);
    }

    // if (response.status === 200) {
    //   navigate("/home");
    // }
    // }
  };
  return (
    <>
      <h2> Sign in </h2>
      <form
        onSubmit={userLogin}
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
