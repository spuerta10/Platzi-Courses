// archivo donde se guarda el tratamiento de los datos
import { Product } from './product.model';


export const products:Product[] = []; //export para poder importar el array de productos en otros modulos

export const addProduct = (data:Product) => {
    products.push(data);
}

export const calckStock = ():number => {
    let total = 0;
    products.forEach((item) => {
        total += item.stock;
    });
    return total;
}