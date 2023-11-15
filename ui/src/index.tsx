import React from 'react';
import ReactDOM from 'react-dom/client';
// import './assets/fonts/Quicksand.ttf';

import AuthApp from './components/Auth';
import axios from 'axios';


const root = ReactDOM.createRoot(document.getElementById('root')!);
root.render(
  <React.StrictMode>
    <AuthApp />
  </React.StrictMode>
);

// export const axiosInstance = axios.create({
//   baseURL: 'http://localhost/api'
// });