import { configureStore, Action, createSlice } from "@reduxjs/toolkit";
import { useDispatch } from "react-redux";
// import { applyMiddleware } from "redux";
// import { composeWithDevTools } from "redux-devtools-extension";
import thunk from "redux-thunk";
// import { userReducer } from "./reducers/userReducer";
import { ThunkAction } from "redux-thunk";
import { reducers } from "./index";
// interface User {
//   id: number;
//   username: string;
//   first_name: string;
//   last_name: string;
//   email: string;
//   access: string;
//   token: string;
// }

// interface UserSliceState {
//   user: User;
// }

// const initalState: UserSliceState = {
//   user: {
//     id: 0,
//     username: "",
//     first_name: "",
//     last_name: "",
//     email: "",
//     access: "",
//     token: "",
//   },
// };

// export const UserSlice = createSlice({
//   name: "user",
//   initalState,
//   reducers: {},
// });
const middleware = [thunk];

const store = configureStore({
  reducer: reducers,
  middleware,
});

// // Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<typeof store.getState>;
// // Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
// export type AppDispatch = typeof store.dispatch;
// export const useAppDispatch = () => useDispatch();
// export type AppThunk = ThunkAction<void, RootState, unknown, Action>;

export default store;
