import { PayloadAction } from "@reduxjs/toolkit";

export const userReducer = (state = {}, action: PayloadAction<object>) => {
  switch (action.type) {
    case "LOGIN_REQUEST":
      return { loading: true };
    case "LOGIN_SUCCESS":
      return { loading: false, loginInfo: action.payload };
    case "LOGIN_FAILED":
      return { loading: false, error: action.payload };
    case "LOGOUT":
      return {};

    default:
      return state;
  }
};
