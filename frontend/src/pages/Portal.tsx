import React, { useRef } from "react";
import axios from "axios";
import Register from "../components/Register";
import Login from "../components/Login";

export default function Portal() {
  return (
    <div className="w-full max-w-xl m-auto">
      <div id="registerFrom">
        <Register />
      </div>
      <div id="loginForm">
        <Login />
      </div>
    </div>
  );
}
