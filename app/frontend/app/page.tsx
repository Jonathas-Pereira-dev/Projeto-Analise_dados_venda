export default async function Home() {
  const res = await fetch("http://localhost:8000/products", {
    cache: "no-store",
  });
  const products = await res.json();

  return (
    <main className="p-10">
      <h1 className="text-3xl font-bold mb-6">Loja de Terços</h1>

      <div className="grid grid-cols-3 gap-6">
        {products.map((p: any) => (
          <div key={p.id} className="border rounded p-4">
            <img src={p.image_url} className="h-40 object-cover mb-3" />
            <h2 className="text-xl">{p.title}</h2>
            <p>R$ {(p.price_cents / 100).toFixed(2)}</p>
            <button
              className="mt-2 bg-blue-600 text-white px-3 py-2 rounded"
            >
              Adicionar ao carrinho
            </button>
          </div>
        ))}
      </div>
    </main>
  );
}
