'use client';
import { useDispatch, useSelector } from 'react-redux';
import { useLogoutMutation } from '../store/services/authApi';
import { logout } from '../store/services/authSlice';
import { useRouter } from 'next/navigation';

export default function Dashboard() {
  const dispatch = useDispatch();
  const [logoutApi] = useLogoutMutation();
  const router = useRouter();
  const { user } = useSelector((state) => state.auth);

  const handleLogout = async () => {
    await logoutApi();
    dispatch(logout());
    router.push('/login');
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h2 className="text-2xl font-bold">
        Добро пожаловать, {user || 'пользователь'}!
      </h2>
      <button
        onClick={handleLogout}
        className="bg-red-500 text-white p-2 rounded mt-4"
      >
        Выйти
      </button>
    </div>
  );
}
