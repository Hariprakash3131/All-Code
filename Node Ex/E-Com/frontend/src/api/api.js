import axios from 'axios';
const BACKEND = import.meta.env.VITE_BACKEND_URL || 'http://localhost:5000';

export const backend = axios.create({
  baseURL: BACKEND + '/api',
});
