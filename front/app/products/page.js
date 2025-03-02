'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { useSelector } from 'react-redux';
import {
  useGetProductsQuery,
  useAddProductMutation,
  useDeleteProductMutation,
} from '../store/services/productsApi';
import { useForm } from 'react-hook-form';

export default function ProductsPage() {
  const router = useRouter();
  const token = useSelector((state) => state.auth.token);
  const { data: products, error, isLoading } = useGetProductsQuery();
  const [addProduct] = useAddProductMutation();
  const [deleteProduct] = useDeleteProductMutation();
  const { register, handleSubmit, reset } = useForm();

  useEffect(() => {
    if (!token) {
      router.push('/login');
    }
  }, [token, router]);

  const onSubmit = async (data) => {
    await addProduct(data);
    reset();
  };

  if (!token) return null;
  if (isLoading) return <p>Loading...</p>;
  if (error) return <p>Error loading products</p>;

  return (
    <div className="max-w-2xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Продукты</h1>
      <form
        onSubmit={handleSubmit(onSubmit)}
        className="mb-4 space-y-2"
      >
        <input
          {...register('name', { required: true })}
          placeholder="Название"
          className="border p-2 w-full"
        />
        <input
          {...register('price', { required: true })}
          placeholder="Цена"
          type="number"
          className="border p-2 w-full"
        />
        <button
          type="submit"
          className="bg-blue-500 text-white p-2 rounded w-full"
        >
          Добавить
        </button>
      </form>
      <ul>
        {products?.map((product) => (
          <li
            key={product.id}
            className="flex justify-between border p-2 mb-2"
          >
            <span>
              {product.name} - ${product.price}
            </span>
            <button
              onClick={() => deleteProduct(product.id)}
              className="text-red-500"
            >
              Удалить
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
