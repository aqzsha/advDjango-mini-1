'use client';
import { useState } from 'react';
import { useRegisterMutation } from '../store/services/authApi';
import { useRouter } from 'next/navigation';

export default function RegisterPage() {
  const [form, setForm] = useState({
    username: '',
    email: '',
    password1: '',
    password2: '',
  });
  const [register, { isLoading, error }] = useRegisterMutation();
  const router = useRouter();

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (form.password1 !== form.password2) {
      alert('Пароли не совпадают!');
      return;
    }
    try {
      const response = await register(form).unwrap();
      console.log('Регистрация успешна:', response);
      router.push('/login'); // Перенаправление на логин
    } catch (err) {
      console.error('Ошибка регистрации:', err);

      // Если сервер вернул 500, сразу кидаем на логин
      if (err.originalStatus === 500) {
        router.push('/login');
      }
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h2 className="text-2xl font-bold">Регистрация</h2>
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
          type="email"
          name="email"
          placeholder="Email"
          value={form.email}
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="password"
          name="password1"
          placeholder="Пароль"
          value={form.password1}
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="password"
          name="password2"
          placeholder="Повторите пароль"
          value={form.password2}
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <button
          type="submit"
          disabled={isLoading}
          className="bg-green-500 text-white p-2 rounded"
        >
          {isLoading ? 'Регистрация...' : 'Зарегистрироваться'}
        </button>
        {error && error.data && (
          <p className="text-red-500">
            {typeof error.data === 'string'
              ? error.data
              : JSON.stringify(error.data)}
          </p>
        )}
      </form>
    </div>
  );
}
