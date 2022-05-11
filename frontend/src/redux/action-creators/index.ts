import { ActionType } from "../actions-types";
import { Dispatch } from "redux";
import { Action } from "../actions";
import axios from "axios";
import { ThunkAction } from "redux-thunk";
import { RootState } from "../store";
import { AnyAction } from "@reduxjs/toolkit";

export const login = (
  username: string,
  password: string
): ThunkAction<void, RootState, unknown, AnyAction> => {
  return async (dispatch) => {
    const { data } = await axios.post("http://localhost:8000/api/login", {
      username: username,
      password: password,
    });
    localStorage.setItem("loginInfo", JSON.stringify(data));
    dispatch({
      type: ActionType.LOGIN,
      payload: data,
    });
  };
};
