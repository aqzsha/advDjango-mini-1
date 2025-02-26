import Providers from './providers';
import Link from 'next/link';
import './styles/globals.css';

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <Providers>
          <nav className="flex gap-4 p-4 bg-gray-100">
            <Link href="/login">Вход</Link>
            <Link href="/register">Регистрация</Link>
            <Link href="/dashboard">Панель</Link>
          </nav>
          {children}
        </Providers>
      </body>
    </html>
  );
}
