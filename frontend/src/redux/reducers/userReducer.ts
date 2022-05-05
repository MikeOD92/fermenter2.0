import { ActionType } from "../actions-types";
import { Action } from "../actions/index";

export const userReducer = (state: object = {}, action: Action) => {
  switch (action.type) {
    case ActionType.LOGIN:
      return { loading: false, loginInfo: action.payload };
    case ActionType.LOGOUT:
      return {};

    default:
      return state;
  }
};
