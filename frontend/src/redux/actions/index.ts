import { ActionType } from "../actions-types/index";

interface LoginAction {
  type: ActionType.LOGIN;
  payload: {};
}
interface LogoutAction {
  type: ActionType.LOGOUT;
}

export type Action = LoginAction | LogoutAction;
