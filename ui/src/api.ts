import axios from 'axios';
import { Configuration, DefaultApi } from './generated';

export const axiosInstance = axios.create();

// configuration, base path, axios instance

export default {
  Backend: new DefaultApi(new Configuration({ basePath: 'api' }), '/api', axiosInstance),
};
