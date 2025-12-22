interface Product {
  id: number;
  name: string;
  price: number;
  category: string;
  description?: string;
}
class ProductManager {
  private products: Product[] = [];

  createProduct(product: Product): void {
    this.products.push(product);
  }

  getProductById(id: number): Product | undefined {
    return this.products.find((p) => p.id === id);
  }

  updateProduct(id: number, update: Partial<Product>): void {
    const product = this.getProductById(id);
    if (product) {
      Object.assign(product, update);
    }
  }

  deleteProduct(id: number): void {
    this.products = this.products.filter((p) => p.id !== id);
  }

  getAllProducts(): Product[] {
    return this.products;
  }
}

const manager = new ProductManager();
manager.createProduct({ id: 1, name: "iPhone 12", price: 999, category: "Smartphone" });
manager.createProduct({ id: 2, name: "iPhone 13", price: 1099, category: "Smartphone" });
manager.createProduct({ id: 3, name: "iPhone 14", price: 1199, category: "Smartphone" });
manager.createProduct({ id: 4, name: "iPhone 15 Pro", price: 1399, category: "Smartphone" });
manager.createProduct({ id: 5, name: "iPhone SE (2022)", price: 499, category: "Smartphone" });

manager.updateProduct(2, { price: 799 });
manager.deleteProduct(1);

console.log("Qolgan mahsulotlar:", manager.getAllProducts());
