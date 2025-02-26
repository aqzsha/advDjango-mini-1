import { createSlice } from '@reduxjs/toolkit';
import Cookies from 'js-cookie';

const initialState = {
  user: null,
  token: Cookies.get('token') || null,
};

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    setUser: (state, action) => {
      state.user = action.payload.user;
      state.token = action.payload.token;
      Cookies.set('token', action.payload.token, { expires: 7 });
    },
    logout: (state) => {
      state.user = null;
      state.token = null;
      Cookies.remove('token');
    },
  },
});

export const { setUser, logout } = authSlice.actions;
export default authSlice.reducer;
