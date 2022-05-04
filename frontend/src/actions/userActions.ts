import axios from "axios";
import { useAppDispatch } from "../hooks";

function getErrorMsg(error: unknown) {
  if (error instanceof Error) return error.message;
  return String(error);
}
export const login = (username: string, password: string) => async () => {
  const dispatch = useAppDispatch();

  try {
    dispatch({
      type: "LOGIN_REQUEST",
    });
    const config = {
      headers: {
        "Content-type": "application/json",
      },
    };
    const { data } = await axios.post(
      "/api/login",
      {
        username: username,
        password: password,
      },
      config
    );

    dispatch({
      type: "LOGIN_SUCCESS",
      payload: data,
    });
  } catch (err) {
    dispatch({
      type: "LOGIN_FAILED",
      payload: getErrorMsg(err),
    });
  }
};
