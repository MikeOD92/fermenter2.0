import { ActionType } from "../actions-types";
import { Dispatch } from "redux";
import { Action } from "../actions";
import axios from "axios";
// import { createAsyncThunk } from "@reduxjs/toolkit";

export const login = (username: string, password: string) => /* async () => */ {
  // const { data } = await axios.post("http://localhost:8000/api/login", {
  //   username: username,
  //   password: password,
  // });

  // console.log(data);

  return (dispatch: Dispatch<Action>) => {
    dispatch({
      type: ActionType.LOGIN,
      payload: { message: "issues with async" },
    });
  };
};
