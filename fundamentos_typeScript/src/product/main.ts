//archivo principal de ejecucion del programa
import {addProduct, products} from './product.service';

addProduct({
    title: 'Product1',
    createdAt: new Date(2023,6,12),
    stock:5
})

console.log(products)


