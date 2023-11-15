import axios from 'axios';
import { Configuration, DefaultApi } from './generated';

export const axiosInstance = axios.create({
  baseURL: 'http://localhost:80'
});

// configuration, base path, axios instance

export default {
  Backend: new DefaultApi(new Configuration({ basePath: 'api' }), '/api', axiosInstance),
};
