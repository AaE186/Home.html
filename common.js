const API_URL = 'http://127.0.0.1:8000';

function getToken() {
  return localStorage.getItem('token');
}

function setToken(token) {
  localStorage.setItem('token', token);
}

function logout() {
  localStorage.removeItem('token');
}

async function login(email, password) {
  const form = new URLSearchParams();
  form.append('username', email);
  form.append('password', password);
  const res = await fetch(API_URL + '/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: form
  });
  if (!res.ok) throw new Error('Неверный email или пароль');
  const data = await res.json();
  setToken(data.access_token);
  return data;
}

async function register(email, password) {
  const res = await fetch(API_URL + '/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  });
  if (!res.ok) {
    const data = await res.json();
    throw new Error(data.detail || 'Ошибка регистрации');
  }
  return await res.json();
}

async function fetchWithAuth(url, options = {}) {
  const token = getToken();
  if (!token) throw new Error('Нет токена');
  options.headers = options.headers || {};
  options.headers['Authorization'] = 'Bearer ' + token;
  const res = await fetch(API_URL + url, options);
  if (res.status === 401) {
    logout();
    window.location.href = 'index.html';
    throw new Error('Требуется авторизация');
  }
  return res;
} 