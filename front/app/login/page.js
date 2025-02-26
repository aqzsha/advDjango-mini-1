'use client';
import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { setUser } from '../store/services/authSlice';
import { useRouter } from 'next/navigation';
import { useLoginMutation } from '../store/services/authApi';

export default function LoginPage() {
  const [form, setForm] = useState({ username: '', password: '' });
  const [login, { isLoading, error }] = useLoginMutation();
  const dispatch = useDispatch();
  const router = useRouter();

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const userData = await login(form).unwrap();
      dispatch(setUser({ user: form.username, token: userData.key }));
      router.push('/dashboard'); // Перенаправление после входа
    } catch (err) {
      console.error('Ошибка входа:', err);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h2 className="text-2xl font-bold">Вход</h2>
      <form
        onSubmit={handleSubmit}
        className="flex flex-col gap-4 w-80"
      >
        <input
          type="text"
          name="username"
          placeholder="Имя пользователя"
          value={form.username}
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="password"
          name="password"
          placeholder="Пароль"
          value={form.password}
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <button
          type="submit"
          disabled={isLoading}
          className="bg-blue-500 text-white p-2 rounded"
        >
          {isLoading ? 'Вход...' : 'Войти'}
        </button>
        {error && <p className="text-red-500">Ошибка: {error.data?.detail}</p>}
      </form>
    </div>
  );
}
